"""
data_preparation.py

Gold Pathfinder ML Project – ELO2 (MIT Emerging Talent)

End-to-end data preparation pipeline for Milestone 2:
    - Load raw ALS assay CSV files
    - Clean and standardize per sample-type tables
    - Handle below-detection values (`<LOD`)
    - Harmonize column names and units
    - Export per-type cleaned datasets
    - Build a final merged dataset for analysis

This script is designed to be:
    - Reproducible
    - Explicit
    - Easy to adapt if raw file formats change

Usage (from project root):

    python 2_data_preparation/scripts/data_preparation.py

Requirements:
    - Python 3.9+
    - pandas
    - numpy
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Tuple, List

import numpy as np  # pylint: disable=import-error
import pandas as pd  # pylint: disable=import-error



# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "1_datasets" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "1_datasets" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Expected raw file names (adjust here if your filenames differ)
# Make sure these exist in: 1_datasets/raw/
CORE_FILES: List[str] = ["An1-Core.csv", "An7_Cores_DD.csv"]
RC_FILES: List[str] = ["An1-RC.csv"]
CHIP_FILES: List[str] = ["An6_Chip.csv", "An7_Chip.csv"]
TRENCH_FILES: List[str] = ["An6-Trenchs Result.csv"]
GRAB_FILES: List[str] = ["An6-Grap.csv", "An7_Grap.csv"]


# Output file names
CORE_OUT = PROCESSED_DIR / "core_assays_clean.csv"
RC_OUT = PROCESSED_DIR / "rc_assays_clean.csv"
CHIP_OUT = PROCESSED_DIR / "chip_assays_clean.csv"
TRENCH_OUT = PROCESSED_DIR / "trench_assays_clean.csv"
GRAB_OUT = PROCESSED_DIR / "grab_assays_clean.csv"
FINAL_OUT = PROCESSED_DIR / "gold_assays_final.csv"


# -----------------------------------------------------------------------------
# Logging configuration
# -----------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------


def parse_detection_limit(value: str | float | int) -> Tuple[float | np.nan, bool]:
    """
    Parse a single value that may represent a below-detection limit measurement.

    Examples:
        "<0.01" -> (0.01, True)
        "<10"   -> (10.0, True)
        "0.25"  -> (0.25, False)
        np.nan  -> (np.nan, False)

    We keep the numeric LOD instead of half LOD to remain conservative.
    If you prefer LOD/2, adjust the function accordingly.
    """
    if pd.isna(value):
        return np.nan, False

    if isinstance(value, (int, float)):
        return float(value), False

    s = str(value).strip()
    if not s:
        return np.nan, False

    if s.startswith("<"):
        try:
            lod = float(s[1:])
            return lod, True
        except ValueError:
            logging.warning("Could not parse detection-limit value: %r", value)
            return np.nan, True

    try:
        return float(s), False
    except ValueError:
        logging.warning("Could not parse numeric value: %r", value)
        return np.nan, False


def convert_numeric_with_flag(
    df: pd.DataFrame, numeric_cols: List[str]
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Convert specified columns to numeric, parsing detection-limit strings.

    Returns:
        - Updated dataframe
        - A boolean Series `below_detection` flagging any row with a <LOD value.

    """
    below_detection_flags = pd.Series(False, index=df.index)

    for col in numeric_cols:
        if col not in df.columns:
            continue

        parsed_vals = []
        flags = []

        for v in df[col]:
            val, flag = parse_detection_limit(v)
            parsed_vals.append(val)
            flags.append(flag)

        df[col] = parsed_vals
        below_detection_flags = below_detection_flags | pd.Series(flags, index=df.index)

    return df, below_detection_flags


def safe_read_csv(path: Path, **kwargs) -> pd.DataFrame:
    """
    Wrapper around pd.read_csv with logging and a helpful error if file is missing.
    """
    if not path.exists():
        raise FileNotFoundError(f"Expected raw file not found: {path}")
    logging.info("Reading raw file: %s", path)
    return pd.read_csv(path, **kwargs)


# -----------------------------------------------------------------------------
# Cleaning functions per sample type
# -----------------------------------------------------------------------------


def clean_core_assays() -> pd.DataFrame:
    """
    Clean and standardize core assay datasets.

    Assumes each core file has at least:
        - Field ID / Field_Id / Sample ID
        - Lab ID (optional)
        - X, Y coordinates (optional)
        - Au, As, Sb, Bi, Cu, Zn, Pb, Ag

    Adjust the column mappings if your header names differ.
    """
    dfs = []

    for fname in CORE_FILES:
        raw_path = RAW_DIR / fname
        if not raw_path.exists():
            logging.warning("Core file not found, skipping: %s", raw_path)
            continue

        df = safe_read_csv(raw_path)

        # Try to detect common column names
        col_map = {
            "Field ID": "sample_id",
            "Field_Id": "sample_id",
            "Sample ID": "sample_id",
            "Lab ID": "lab_id",
            "lab_id": "lab_id",
            "x": "easting",
            "X": "easting",
            "y": "northing",
            "Y": "northing",
            "Elevation From (m)": "elevation_from",
            "Elev_from": "elevation_from",
            "Elevation To (m)": "elevation_to",
            "Elev_to": "elevation_to",
            "Au": "au_ppm",
            "As": "as_ppm",
            "Sb": "sb_ppm",
            "Bi": "bi_ppm",
            "Cu": "cu_ppm",
            "Zn": "zn_ppm",
            "Pb": "pb_ppm",
            "Ag": "ag_ppm",
        }

        # Build an empty standardized frame
        clean = pd.DataFrame(index=df.index)

        for raw_col, standard in col_map.items():
            if raw_col in df.columns:
                clean[standard] = df[raw_col]

        # Metadata
        clean["sample_type"] = "core"
        clean["project_area"] = "Shamkya"
        # If anomaly is encoded in file name, you can parse from fname; for now, NaN
        clean["anomaly_id"] = np.nan

        # Derive interval if elevation_from & elevation_to are available
        if "elevation_from" in clean.columns and "elevation_to" in clean.columns:
            clean["interval_m"] = clean["elevation_from"] - clean["elevation_to"]
        else:
            clean["interval_m"] = np.nan

        # Convert numeric geochemical fields
        numeric_cols = [
            "au_ppm",
            "as_ppm",
            "sb_ppm",
            "bi_ppm",
            "cu_ppm",
            "zn_ppm",
            "pb_ppm",
            "ag_ppm",
        ]
        clean, bdl_flag = convert_numeric_with_flag(clean, numeric_cols)
        clean["below_detection"] = bdl_flag

        dfs.append(clean)

    if not dfs:
        logging.warning("No core datasets processed.")
        return pd.DataFrame()

    core_all = pd.concat(dfs, ignore_index=True)
    logging.info("Core assays cleaned: %d rows", len(core_all))
    return core_all


def clean_rc_assays() -> pd.DataFrame:
    """
    Clean and standardize RC assay datasets.

    Expected columns (adjust if needed):
        - Field No / Sample ID       -> sample_id
        - lab Serial / Lab ID       -> lab_id
        - x, y, z                   -> easting, northing, rl
        - Depth(m) / From_m         -> from_m
        - To(m) (or similar)        -> to_m
        - Au, As, Sb, Bi, Cu, Zn    -> element assays
    """
    dfs = []

    for fname in RC_FILES:
        raw_path = RAW_DIR / fname
        if not raw_path.exists():
            logging.warning("RC file not found, skipping: %s", raw_path)
            continue

        df = safe_read_csv(raw_path)

        clean = pd.DataFrame(index=df.index)

        # Map ID and coordinates
        id_map = {
            "Field No": "sample_id",
            "Sample ID": "sample_id",
            "lab Serial": "lab_id",
            "Lab ID": "lab_id",
            "x": "easting",
            "X": "easting",
            "y": "northing",
            "Y": "northing",
            "z": "rl",
            "Z": "rl",
            "Depth(m)": "from_m",
            "From_m": "from_m",
        }

        for raw_col, standard in id_map.items():
            if raw_col in df.columns:
                clean[standard] = df[raw_col]

        # Try to infer to_m (sometimes unnamed depth column)
        if "to_m" in df.columns:
            clean["to_m"] = df["to_m"]
        else:
            # attempt to find a second depth-like column
            depth_like = [
                c
                for c in df.columns
                if "to" in c.lower() or ("depth" in c.lower() and c != "Depth(m)")
            ]
            if depth_like:
                clean["to_m"] = df[depth_like[0]]
            else:
                clean["to_m"] = np.nan

        # Interval
        if "from_m" in clean.columns and "to_m" in clean.columns:
            with np.errstate(invalid="ignore"):
                clean["interval_m"] = clean["to_m"] - clean["from_m"]
        else:
            clean["interval_m"] = np.nan

        # Geochemistry
        geochem_map = {
            "Au": "au_ppm",
            "As": "as_ppm",
            "Sb": "sb_ppm",
            "Bi": "bi_ppm",
            "Cu": "cu_ppm",
            "Zn": "zn_ppm",
            "Pb": "pb_ppm",
            "Ag": "ag_ppm",
        }

        for raw_col, standard in geochem_map.items():
            if raw_col in df.columns:
                clean[standard] = df[raw_col]

        clean["sample_type"] = "rc"
        clean["project_area"] = "Shamkya"
        clean["anomaly_id"] = "An1"  # adjust if multiple anomalies later

        numeric_cols = [
            "au_ppm",
            "as_ppm",
            "sb_ppm",
            "bi_ppm",
            "cu_ppm",
            "zn_ppm",
            "pb_ppm",
            "ag_ppm",
        ]
        clean, bdl_flag = convert_numeric_with_flag(clean, numeric_cols)
        clean["below_detection"] = bdl_flag

        dfs.append(clean)

    if not dfs:
        logging.warning("No RC datasets processed.")
        return pd.DataFrame()

    rc_all = pd.concat(dfs, ignore_index=True)
    logging.info("RC assays cleaned: %d rows", len(rc_all))
    return rc_all


def clean_chip_assays() -> pd.DataFrame:
    """
    Clean and standardize chip sample assays.

    Assumes:
        - Feild ID / Field ID      -> sample_id
        - Lab ID (optional)       -> lab_id
        - x, y                    -> easting, northing
        - Au / Au_1               -> au_ppm
    """
    dfs = []

    for fname in CHIP_FILES:
        raw_path = RAW_DIR / fname
        if not raw_path.exists():
            logging.warning("Chip file not found, skipping: %s", raw_path)
            continue

        df = safe_read_csv(raw_path)

        clean = pd.DataFrame(index=df.index)

        # IDs
        id_candidates = ["Feild ID", "Field ID", "Sample ID"]
        for c in id_candidates:
            if c in df.columns:
                clean["sample_id"] = df[c]
                break

        if "Lab ID" in df.columns:
            clean["lab_id"] = df["Lab ID"]
        else:
            clean["lab_id"] = np.nan

        # Coordinates
        for raw_col, standard in [("x", "easting"), ("X", "easting")]:
            if raw_col in df.columns:
                clean["easting"] = df[raw_col]
                break

        for raw_col, standard in [("y", "northing"), ("Y", "northing")]:
            if raw_col in df.columns:
                clean["northing"] = df[raw_col]
                break

        # Au: prefer Au_1 if available, else Au
        if "Au_1" in df.columns:
            clean["au_ppm"] = df["Au_1"]
        elif "Au" in df.columns:
            clean["au_ppm"] = df["Au"]
        else:
            clean["au_ppm"] = np.nan

        # Other elements if present
        for raw_col, standard in [
            ("As", "as_ppm"),
            ("Sb", "sb_ppm"),
            ("Bi", "bi_ppm"),
            ("Cu", "cu_ppm"),
            ("Zn", "zn_ppm"),
            ("Pb", "pb_ppm"),
            ("Ag", "ag_ppm"),
        ]:
            if raw_col in df.columns:
                clean[standard] = df[raw_col]

        clean["sample_type"] = "chip"
        clean["project_area"] = "Shamkya"

        # Rough anomaly guess from filename
        if "An6" in fname:
            clean["anomaly_id"] = "An6"
        elif "An7" in fname:
            clean["anomaly_id"] = "An7"
        else:
            clean["anomaly_id"] = np.nan

        numeric_cols = [
            "au_ppm",
            "as_ppm",
            "sb_ppm",
            "bi_ppm",
            "cu_ppm",
            "zn_ppm",
            "pb_ppm",
            "ag_ppm",
        ]
        clean, bdl_flag = convert_numeric_with_flag(clean, numeric_cols)
        clean["below_detection"] = bdl_flag

        dfs.append(clean)

    if not dfs:
        logging.warning("No chip datasets processed.")
        return pd.DataFrame()

    chip_all = pd.concat(dfs, ignore_index=True)
    logging.info("Chip assays cleaned: %d rows", len(chip_all))
    return chip_all


def clean_trench_assays() -> pd.DataFrame:
    """
    Clean and standardize trench assays.

    Expected columns:
        - Field ID
        - Lab ID
        - Au or Au_1
        - As, Sb, Bi, Cu, Zn, Pb, Ag (if available)
    """
    dfs = []

    for fname in TRENCH_FILES:
        raw_path = RAW_DIR / fname
        if not raw_path.exists():
            logging.warning("Trench file not found, skipping: %s", raw_path)
            continue

        df = safe_read_csv(raw_path)

        clean = pd.DataFrame(index=df.index)

        if "Field ID" in df.columns:
            clean["sample_id"] = df["Field ID"]
        else:
            clean["sample_id"] = df.get("Sample ID", np.nan)

        clean["lab_id"] = df.get("Lab ID", np.nan)

        # Coordinates not available in this file as of current version
        clean["easting"] = np.nan
        clean["northing"] = np.nan

        # Au: prefer Au_1 if present
        if "Au_1" in df.columns:
            clean["au_ppm"] = df["Au_1"]
        elif "Au" in df.columns:
            clean["au_ppm"] = df["Au"]
        else:
            clean["au_ppm"] = np.nan

        for raw_col, standard in [
            ("As", "as_ppm"),
            ("Sb", "sb_ppm"),
            ("Bi", "bi_ppm"),
            ("Cu", "cu_ppm"),
            ("Zn", "zn_ppm"),
            ("Pb", "pb_ppm"),
            ("Ag", "ag_ppm"),
        ]:
            if raw_col in df.columns:
                clean[standard] = df[raw_col]

        clean["sample_type"] = "trench"
        clean["project_area"] = "Shamkya"
        clean["anomaly_id"] = "An6"

        numeric_cols = [
            "au_ppm",
            "as_ppm",
            "sb_ppm",
            "bi_ppm",
            "cu_ppm",
            "zn_ppm",
            "pb_ppm",
            "ag_ppm",
        ]
        clean, bdl_flag = convert_numeric_with_flag(clean, numeric_cols)
        clean["below_detection"] = bdl_flag

        dfs.append(clean)

    if not dfs:
        logging.warning("No trench datasets processed.")
        return pd.DataFrame()

    trench_all = pd.concat(dfs, ignore_index=True)
    logging.info("Trench assays cleaned: %d rows", len(trench_all))
    return trench_all


def clean_grab_assays() -> pd.DataFrame:
    """
    Clean and standardize grab sample assays.

    Expected columns:
        - Feild ID / Field ID
        - Lab ID
        - Au or Au.1
        - As, Sb, Bi, Cu, Zn, Pb, Ag (if available)
    """
    dfs = []

    for fname in GRAB_FILES:
        raw_path = RAW_DIR / fname
        if not raw_path.exists():
            logging.warning("Grab file not found, skipping: %s", raw_path)
            continue

        df = safe_read_csv(raw_path)

        clean = pd.DataFrame(index=df.index)

        id_candidates = ["Feild ID", "Field ID", "Sample ID"]
        for c in id_candidates:
            if c in df.columns:
                clean["sample_id"] = df[c]
                break
        else:
            clean["sample_id"] = np.nan

        clean["lab_id"] = df.get("Lab ID", np.nan)

        # Spatial info usually not present
        clean["easting"] = np.nan
        clean["northing"] = np.nan

        # Au: sometimes Au.1 is numeric, Au is lithology text
        if "Au" in df.columns and df["Au"].dtype != object:
            clean["au_ppm"] = df["Au"]
        elif "Au.1" in df.columns:
            clean["au_ppm"] = df["Au.1"]
        else:
            clean["au_ppm"] = np.nan

        for raw_col, standard in [
            ("As", "as_ppm"),
            ("Sb", "sb_ppm"),
            ("Bi", "bi_ppm"),
            ("Cu", "cu_ppm"),
            ("Zn", "zn_ppm"),
            ("Pb", "pb_ppm"),
            ("Ag", "ag_ppm"),
        ]:
            if raw_col in df.columns:
                clean[standard] = df[raw_col]

        clean["sample_type"] = "grab"
        clean["project_area"] = "Shamkya"

        if "An6" in fname:
            clean["anomaly_id"] = "An6"
        elif "An7" in fname:
            clean["anomaly_id"] = "An7"
        else:
            clean["anomaly_id"] = np.nan

        numeric_cols = [
            "au_ppm",
            "as_ppm",
            "sb_ppm",
            "bi_ppm",
            "cu_ppm",
            "zn_ppm",
            "pb_ppm",
            "ag_ppm",
        ]
        clean, bdl_flag = convert_numeric_with_flag(clean, numeric_cols)
        clean["below_detection"] = bdl_flag

        dfs.append(clean)

    if not dfs:
        logging.warning("No grab datasets processed.")
        return pd.DataFrame()

    grab_all = pd.concat(dfs, ignore_index=True)
    logging.info("Grab assays cleaned: %d rows", len(grab_all))
    return grab_all


# -----------------------------------------------------------------------------
# Final merge
# -----------------------------------------------------------------------------


def build_final_dataset(
    core_df: pd.DataFrame,
    rc_df: pd.DataFrame,
    chip_df: pd.DataFrame,
    trench_df: pd.DataFrame,
    grab_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Merge all cleaned per-type datasets into one unified dataset.

    Columns are harmonized: any column that appears in any dataset
    will be present (with NaN where not applicable in some sample types).
    """
    dfs = [core_df, rc_df, chip_df, trench_df, grab_df]
    dfs = [d for d in dfs if not d.empty]

    if not dfs:
        logging.error("No cleaned datasets to merge. Aborting final dataset build.")
        return pd.DataFrame()

    all_cols = sorted(set().union(*[d.columns for d in dfs]))
    aligned = [d.reindex(columns=all_cols) for d in dfs]

    final_df = pd.concat(aligned, ignore_index=True)
    logging.info("Final merged dataset built: %d rows, %d columns", *final_df.shape)
    return final_df


# -----------------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------------


def main() -> None:
    logging.info("Starting data preparation pipeline")

    core_df = clean_core_assays()
    rc_df = clean_rc_assays()
    chip_df = clean_chip_assays()
    trench_df = clean_trench_assays()
    grab_df = clean_grab_assays()

    if not core_df.empty:
        CORE_OUT.parent.mkdir(parents=True, exist_ok=True)
        core_df.to_csv(CORE_OUT, index=False)
        logging.info("Core assays saved to: %s", CORE_OUT)

    if not rc_df.empty:
        RC_OUT.parent.mkdir(parents=True, exist_ok=True)
        rc_df.to_csv(RC_OUT, index=False)
        logging.info("RC assays saved to: %s", RC_OUT)

    if not chip_df.empty:
        CHIP_OUT.parent.mkdir(parents=True, exist_ok=True)
        chip_df.to_csv(CHIP_OUT, index=False)
        logging.info("Chip assays saved to: %s", CHIP_OUT)

    if not trench_df.empty:
        TRENCH_OUT.parent.mkdir(parents=True, exist_ok=True)
        trench_df.to_csv(TRENCH_OUT, index=False)
        logging.info("Trench assays saved to: %s", TRENCH_OUT)

    if not grab_df.empty:
        GRAB_OUT.parent.mkdir(parents=True, exist_ok=True)
        grab_df.to_csv(GRAB_OUT, index=False)
        logging.info("Grab assays saved to: %s", GRAB_OUT)

    final_df = build_final_dataset(core_df, rc_df, chip_df, trench_df, grab_df)
    if not final_df.empty:
        FINAL_OUT.parent.mkdir(parents=True, exist_ok=True)
        final_df.to_csv(FINAL_OUT, index=False)
        logging.info("Final merged dataset saved to: %s", FINAL_OUT)

    logging.info("Data preparation pipeline completed successfully")


if __name__ == "__main__":
    main()

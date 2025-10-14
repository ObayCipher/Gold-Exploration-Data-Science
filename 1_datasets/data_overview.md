# 📊 Data Overview --- Gold Pathfinder ML Project

**Milestone 2 --- Data Collection & Preparation**  

------------------------------------------------------------------------

## 1. Purpose

This document describes the **data sources**, **structure**, and
**high-level characteristics** of the datasets used in the *Gold
Pathfinder ML Project*. It supports **Milestone 2** of the **ELO2
Framework (Data Collection & Preparation)**.

------------------------------------------------------------------------

## 2. Data Sources

### 2.1 ALS Laboratory Assay Data

The primary data source consists of **geochemical assay results**
provided by **ALS Laboratory** for a gold exploration project. The
datasets include:

- **Diamond core samples** (e.g., `An1-Core.xlsx`,
    `An7_Cores_DD.xlsx`)
- **RC drilling samples** (e.g., `An1-RC.xlsx`)
- **Chip samples** (e.g., `An6_Chip.xlsx`, `An7_Chip.xlsx`)
- **Trench and grab samples** (e.g., `An6-Trenchs Result.xlsx`,
    `An6-Grap.xlsx`, `An7_Grap.xlsx`)

These files contain:

- Sample identifiers and field IDs
- Spatial coordinates (Easting, Northing), where available
- Elevation or depth intervals
- Gold (Au) assay values
- Multi-element geochemistry (e.g., As, Sb, Bi, Cu, Zn, and others)

------------------------------------------------------------------------

## 3. Repository Location

Within this repository, the data is organized as follows:

``` text
1_datasets/
├── raw/                      # Original ALS Excel or CSV files (read-only)
├── processed/                # Cleaned, standardized CSV files for analysis
├── data_overview.md
├── data_dictionary.md
└── data_collection.md   # Milestone 2 report
```

- `raw/` contains **unaltered source files**.
- `processed/` contains **analysis-ready datasets** with consistent
    column names and data types.

------------------------------------------------------------------------

## 4. Data Modeling Approach

The data will be modeled in a **sample-centric tabular format**, where
each row represents a single sample interval. Columns are grouped as
follows:

### 4.1 Identification & Metadata

- `sample_id`
- `lab_id`
- `sample_type` (core, RC, chip, trench, grab)
- `project_area` or `anomaly_id` (if applicable)

### 4.2 Location & Geometry

- `easting`, `northing` (UTM or local grid)
- `elevation_from`, `elevation_to`
- `interval_m`

### 4.3 Lithology & Descriptive Fields (if available)

- `lithology`
- `sample_description`

### 4.4 Assay Results --- Gold

- `au_ppm` or `au_gpt`

### 4.5 Assay Results --- Multi-Element Geochemistry

Examples include:

- `as_ppm`, `sb_ppm`, `bi_ppm`, `cu_ppm`, `zn_ppm`, `pb_ppm`, etc.

### 4.6 QA/QC Fields (if present)

- `duplicate_flag`
- `standard_flag`
- `blank_flag`

------------------------------------------------------------------------

## 5. Data Quality Considerations

- Some source files contain **multiple header rows**; these will be
    normalized during data cleaning.
- **Detection limits and "below detection" values** will be handled
    explicitly (e.g., replaced with DL/2 and flagged).
- Not all sample types contain **complete spatial coordinate
    information**.
- Gold (Au) values may exhibit **strong positive skewness** due to the
    **coarse gold effect**; this will be addressed in later modeling
    stages.

------------------------------------------------------------------------

## 6. Outputs of Milestone 2

By the completion of Milestone 2, the following outputs will be
delivered:

- At least one **consolidated CSV file per sample type** (core, RC,
    chip/trench).
- A **unified and standardized column schema** across all processed
    datasets.
- A fully documented **data dictionary** (`data_dictionary.md`).
- All **processing workflows and transformations** documented in
    `2_data_preparation/`.

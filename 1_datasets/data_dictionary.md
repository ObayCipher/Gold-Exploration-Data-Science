# 📚 Data Dictionary — Gold Pathfinder ML Project  

**Milestone 2 --- Data Collection & Preparation**  

---

This data dictionary defines the **structure, meaning, units, QA/QC rules, and machine-learning role** of all variables used in the **processed datasets** stored under:

`1_datasets/processed/`

> 🔎 This is a **living document**. Column names may be refined during data cleaning, but definitions and units must remain consistent for scientific and ML integrity.

---

## 1. Purpose & Scope

This Data Dictionary ensures:

- Scientific reproducibility
- ALS laboratory audit traceability
- Machine-learning interoperability
- Compliance with international mineral reporting and geochemical standards:
  - **JORC Code (2012)**
  - **NI 43-101**
  - **ISO-17025 Laboratory Standards**
  - **USGS Geochemical Data Standards**

---

## 2. Data Source Summary

All raw datasets originate from **ALS Global Laboratories** analytical results and were exported from Excel to CSV without modification prior to cleaning.

| File Name | Sample Type | Description |
|----------|-------------|-------------|
| `An1-Core.csv` | Diamond Core | Subsurface core geochemical assays |
| `An1-RC.csv` | RC Drilling | Reverse circulation chip samples |
| `An6_Chip.csv` | Chip | Surface rock chip sampling |
| `An6-Grap.csv` | Grab | Selective grab samples |
| `An6-Trenchs Result.csv` | Trench | Channel & trench sampling |
| `An7_Chip.csv` | Chip | Additional surface sampling |
| `An7_Cores_DD.csv` | Diamond Core | Deep diamond drilling |
| `An7_Grap.csv` | Grab | Additional grab sampling |

Processed datasets are derived exclusively from these raw sources.

---

## 3. Identification & Metadata

| Column Name | Type | Description | Example |
|-------------|------|-------------|---------|
| `sample_id` | string | Unique identifier for each sample or interval | `BH1-001` |
| `lab_id` | string | ALS laboratory internal sample ID | `ALS123456` |
| `sample_type` | string | Sample medium (`core`, `rc`, `chip`, `grab`, `trench`) | `core` |
| `project_area` | string | Project or prospect name | `Shamkya` |
| `anomaly_id` | string | Local anomaly or zone identifier | `An1` |
| `batch_id` | string | ALS analytical batch identifier | `B2024-77` |

---

## 4. Location & Geometry (Spatial Features)

All coordinates are projected in **UTM, WGS-84 datum, meters**.

| Column Name | Type | Units | Description | Example |
|-------------|------|-------|-------------|---------|
| `easting` | float | m | UTM Easting | `498889.544` |
| `northing` | float | m | UTM Northing | `2144445.838` |
| `elevation_from` | float | m | Start depth/elevation of sampled interval | `330.93` |
| `elevation_to` | float | m | End depth/elevation of sampled interval | `327.93` |
| `interval_m` | float | m | Sample length (`to - from`) | `3.0` |

**ML role:** spatial predictors and geostatistical weighting variables.

---

## 5. Lithology & Geological Description

| Column Name | Type | Description | Example |
|-------------|------|-------------|---------|
| `lithology` | string | Dominant rock type or unit | `Quartz vein` |
| `alteration` | string | Alteration style | `Silicification` |
| `structure` | string | Structural observations | `Shear zone` |
| `sample_description` | string | Free-text geological notes | `Silicified granite` |
| `weathering` | string | Weathering state | `Oxidized` |

---

## 6. Gold Assay (Primary Target Variable)

| Column Name | Type | Units | Description | Example |
|-------------|------|-------|-------------|---------|
| `au_ppm` | float | ppm (g/t) | Gold concentration (Fire Assay) | `1.25` |

**Note:**  
Laboratory values reported as **g/t are numerically equivalent to ppm** for gold (1 g/t = 1 ppm).

**ML Role:** Primary regression and classification target variable.

---

## 7. Multi-Element Geochemistry (Predictor Features)

### 7.1 Pathfinder & Economic Elements

| Column Name | Type | Units | Geological Role | Example |
|-------------|------|-------|------------------|---------|
| `as_ppm` | float | ppm | Arsenic pathfinder for gold | `145` |
| `sb_ppm` | float | ppm | Antimony pathfinder | `12` |
| `bi_ppm` | float | ppm | Bismuth association | `3` |
| `cu_ppm` | float | ppm | Copper mineralization | `220` |
| `zn_ppm` | float | ppm | Zinc sulphides | `410` |
| `pb_ppm` | float | ppm | Lead sulphides | `85` |
| `ag_ppm` | float | ppm | Silver association | `2.3` |
| `mo_ppm` | float | ppm | Molybdenum indicator | `9` |
| `ni_ppm` | float | ppm | Mafic/ultramafic indicator | `61` |
| `co_ppm` | float | ppm | Hydrothermal zoning indicator | `22` |

---

### 7.2 Major Oxides (When Available)

| Column Name | Type | Units | Description |
|-------------|------|-------|-------------|
| `sio2_pct` | float | % | Silica |
| `al2o3_pct` | float | % | Alumina |
| `fe_pct` | float | % | Total iron |
| `mgo_pct` | float | % | Magnesium oxide |
| `cao_pct` | float | % | Calcium oxide |
| `na2o_pct` | float | % | Sodium oxide |
| `k2o_pct` | float | % | Potassium oxide |
| `tio2_pct` | float | % | Titanium dioxide |

---

## 8. Drilling-Specific Parameters (Core & RC)

| Column Name | Type | Units | Description |
|-------------|------|-------|-------------|
| `hole_id` | string | – | Drill hole identifier |
| `recovery_pct` | float | % | Core recovery |
| `rqd_pct` | float | % | Rock Quality Designation |

---

## 9. Surface Sampling Parameters (Chip, Grab, Trench)

| Column Name | Type | Units | Description |
|-------------|------|-------|-------------|
| `channel_length_m` | float | m | Channel length |
| `outcrop_type` | string | – | Float, in-situ, subcrop |

---

## 10. Detection Limits & Censored Data Handling

ALS reports values below analytical detection limits using symbols such as:

- `<0.01`, `<0.05`, `<0.1` ppm

**Cleaning rule applied in processed datasets:**

- Non-detects are converted to **½ detection limit**  
- These conversions are flagged using `below_detection = True`

| Symbol | Meaning |
|--------|---------|
| `<` | Below detection limit |
| `>` | Above upper calibration limit |

---

## 11. QA/QC & Control Flags

| Column Name | Type | Description | Example |
|-------------|------|-------------|---------|
| `is_duplicate` | bool | Field or lab duplicate sample | `True` |
| `is_standard` | bool | Certified reference material | `False` |
| `is_blank` | bool | Blank control sample | `False` |
| `below_detection` | bool | Originally reported as `<DL` | `True` |

---

## 12. Machine Learning Role of Variable Groups

| Variable Group | ML Role |
|----------------|--------|
| Gold (`au_ppm`) | Target variable |
| Trace elements | Pathfinder predictors |
| Major oxides | Lithochemical predictors |
| Coordinates | Spatial predictors |
| Lithology | Categorical encoded predictors |
| Alteration | Categorical encoded predictors |
| QA/QC flags | Data quality filters |

---

## 13. Data Quality & Laboratory Standards

- All assays performed by **ALS Global (ISO-17025 accredited)**
- Gold determined by **Fire Assay + AAS/ICP finish**
- Multi-element suites by **ICP-MS / ICP-AES**
- No chemical transformations applied to **raw datasets**
- All transformations occur only in:
  `1_datasets/processed/`

---

## 14. Regulatory & Technical Standards Referenced

- [JORC Code (2012) — Australasian Code for Reporting of Exploration Results.](https://www.jorc.org)  
- [NI 43-101 — Canadian Mineral Disclosure Standard.](https://www.osc.ca)  
- [ALS Global Analytical Methods Guide.](https://www.alsglobal.com)  
- [USGS Geochemical Data Standards.](https://www.usgs.gov)
- [ISO-17025 Testing Laboratory Accreditation.](https://www.iso.org)

---

## 15. Version Control

| Version | Date | Description |
|--------|------|-------------|
| 1.0 | 2025-10-18 | Initial unified data dictionary |

---

## 16. Responsible Use Statement

This dataset is intended solely for:

- Mineral exploration research  
- Machine-learning modeling  
- Academic and technical benchmarking  

It **must not** be used as a standalone resource or reserve estimation dataset under JORC or NI 43-101 regulations.

---

*Prepared for the Gold Pathfinder Machine Learning Project*  
*Milestone 2 — Data Collection & Preparation*

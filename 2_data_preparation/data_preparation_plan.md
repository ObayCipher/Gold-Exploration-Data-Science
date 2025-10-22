# 🧪 Data Preparation Plan --- Gold Pathfinder ML Project

**Milestone 2 --- Data Collection & Preparation**  

------------------------------------------------------------------------

## 1. Objective

This document defines the **systematic data preparation workflow**
applied to all geochemical datasets used in the Gold Pathfinder Machine
Learning Project. The purpose is to ensure that all datasets are:

- Clean\
- Consistent\
- Machine-learning ready\
- Fully auditable

This plan aligns with **ELO2: Data Collection & Preparation** standards.

------------------------------------------------------------------------

## 2. Data Input Sources

Raw datasets are stored under:

    1_datasets/raw/csv/

These include:

- Diamond core samples\
- RC drilling samples\
- Chip samples\
- Trench and grab samples

All raw datasets are treated as **read-only** and are never edited
directly.

------------------------------------------------------------------------

## 3. Data Preparation Workflow

### Step 1 --- Raw Data Validation

- File integrity checks\
- CSV structure verification\
- Header consistency validation\
- Duplicate file detection

### Step 2 --- Standardization

- Unified column naming convention\
- Standard units for assay values\
- Standard sample naming format\
- Unified coordinate reference system

### Step 3 --- Missing Data Handling

- Identification of null values\
- Controlled imputation where appropriate\
- Flagging of incomplete records\
- Removal of unusable samples

### Step 4 --- Outlier Detection

- Statistical screening (IQR, Z-score)\
- Geological validation of extreme values\
- Preservation of anomalous gold values

### Step 5 --- Data Type Normalization

- Numeric field coercion\
- Date-time format unification\
- Categorical field standardization

------------------------------------------------------------------------

## 4. Output Data Structure

Cleaned datasets are written to:

    1_datasets/cleaned/csv/

Final ML-ready datasets are written to:

    1_datasets/processed/csv/

Each transformation stage is **version-controlled**.

------------------------------------------------------------------------

## 5. Quality Control (QA/QC)

The following QA/QC checks are applied:

- Cross-file consistency checks\
- Duplicate sample detection\
- Laboratory detection limit review\
- Negative and zero-value screening\
- Coordinate range validation

------------------------------------------------------------------------

## 6. Reproducibility & Audit Trail

All preparation steps are:

- Logged using Git version control\
- Reproducible via Python scripts\
- Traceable through commit history\
- Documented according to ELO2 standards

------------------------------------------------------------------------

## 7. Responsible Roles

- **Data Engineer:** Pipeline implementation\
- **Geochemist:** Validation of chemical plausibility\
- **ML Engineer:** Feature readiness validation

------------------------------------------------------------------------

## ⚠️ WARNINGS

### Some data may gave error in the terminal messege and that due to Text not Value (Float)
<!--✅ This preparation plan ensures **full scientific, technical, and audit
compliance** for Milestone 2 under the ELO2 framework.-->
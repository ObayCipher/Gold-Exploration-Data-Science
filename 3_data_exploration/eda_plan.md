# 📊 Exploratory Data Analysis (EDA) Plan --- Milestone 3

**Gold Pathfinder ML Project -- MIT Emerging Talent (ELO2)**\
**Authors:** Obay Salih, Salih Adam\
**Date:** November 2025

------------------------------------------------------------------------

## 🎯 Purpose

The goal of this Exploratory Data Analysis (EDA) phase is to build a
clear understanding of the **geochemical patterns, distributions, and
correlations** within the processed ALS assay dataset.

This step prepares the foundation for **Milestone 4 (Data Analysis &
Modeling)** by identifying:

-   Data structure and completeness\
-   Distribution characteristics\
-   Potential geochemical pathfinder elements\
-   Relationships between gold (Au) and associated trace elements\
-   Suitability of the data for machine learning and anomaly detection

------------------------------------------------------------------------

## 📁 Dataset Used

**File:**

``` bash
1_datasets/processed/gold_assays_final.csv
```

**Contains:**

-   Gold values (Au ppm)
-   Multi-element geochemistry (As, Sb, Bi, Cu, Zn, Pb, Ag, Fe, etc.)
-   Sample metadata (`sample_id`, `sample_type`, `anomaly_id`,
    `project_area`)
-   Cleaned and standardized features from Milestone 2

------------------------------------------------------------------------

## 🔍 Key EDA Questions

### 1️⃣ Data Structure

-   How many samples and variables are present?\
-   Are there missing values, outliers, or below-detection anomalies?\
-   Which sample types dominate the dataset?

### 2️⃣ Distribution of Elements

-   Are Au and trace elements normally distributed or heavily skewed?\
-   Do logarithmic transformations improve interpretability?

### 3️⃣ Correlation Analysis

-   Which elements correlate positively or negatively with Au?\
-   Do known pathfinders (As, Sb, Bi, Cu) show meaningful
    relationships?\
-   Are there multi-element clusters indicating alteration zones?

### 4️⃣ Sample-Type Patterns

-   How do Au and pathfinders vary across sample types (core, chip,
    trench, RC)?\
-   Are certain sample types more anomalous than others?

### 5️⃣ Anomaly Detection & Geochemical Behavior

-   Are there natural clusters in the geochemical data?\
-   Are gold-rich samples grouped or dispersed spatially and chemically?

------------------------------------------------------------------------

## 📈 Planned EDA Outputs

### A. Summary & Structure

-   `missing_summary.csv`
-   `numeric_summary.csv`
-   Sample counts per sample type and anomaly

### B. Visualizations

-   Histograms and log-histograms for key elements\
-   Boxplots comparing sample types\
-   Correlation heatmap for all numeric elements\
-   Sorted correlation with Au (bar chart)\
-   Pairplots of Au vs top pathfinders

### C. Statistical Outputs

-   Pearson correlation matrix\
-   Element--gold correlation ranking\
-   Detection of skewness and kurtosis

------------------------------------------------------------------------

## 🧪 Tools & Methods

  Task                      Tools / Techniques
  ------------------------- ------------------------------------
  Basic summaries           `pandas`
  Numerical distributions   `matplotlib`, `seaborn`
  Correlations              `seaborn` heatmap, `pandas.corr()`
  Transformation tests      `log10`, `log1p`
  Saving outputs            CSV & PNG

All visualizations will be saved under:

``` text
3_data_exploration/outputs/
3_data_exploration/figures/
```

------------------------------------------------------------------------

## 📌 Deliverables for Milestone 3

  Deliverable      Location
  ---------------- -----------------------------------
  EDA Notebooks    `3_data_exploration/*.ipynb`
  Summary Tables   `3_data_exploration/outputs/`
  Figures          `3_data_exploration/figures/`
  EDA Report       `reports/milestone_3_analysis.md`
  Updated README   Root folder

------------------------------------------------------------------------

## 🚀 Outcome

This EDA stage will:

-   Identify the strongest candidate **pathfinder elements**
-   Reveal **data limitations** (skewness, outliers, missing values)
-   Confirm the **feasibility of machine learning classification**
-   Provide direction for **feature engineering and modeling** in
    Milestone 4

This phase establishes the analytical foundation for modeling **Au
anomalies and geochemical patterns** with confidence and scientific
rigor.

------------------------------------------------------------------------

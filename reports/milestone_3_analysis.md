# 📘 **Milestone 3 --- Data Exploration Analysis Report**

## *Gold Pathfinder ML Project -- MIT Emerging Talent (ELO2)*

**Authors:** Obay Salih · Salih Adam\
**Date:** November 2025

------------------------------------------------------------------------

## 🎯 **Purpose of Milestone 3**

The goal of Milestone 3 is to conduct a **full exploratory data analysis
(EDA)** of the cleaned and processed ALS assay dataset prepared in
Milestone 2.\
This builds the foundation for Milestone 4 (Data Analysis & Modeling).

This EDA focuses on:

- Understanding data structure
- Evaluating distributions and transformations
- Identifying correlations and potential pathfinder elements
- Visualizing multi-element relationships
- Detecting patterns relevant to gold mineralization

------------------------------------------------------------------------

## 📁 **Dataset Analyzed**

File used:

``` text
1_datasets/processed/gold_assays_final.csv
```

Contents:

- Au (gold) concentration in ppm
- Major & trace elements (As, Sb, Bi, Cu, Zn, Pb, Ag, Fe, Mn, etc.)
- Metadata (`sample_id`, `sample_type`, `anomaly`, `project_area`)
- All cleaned and standardized values from Milestone 2

------------------------------------------------------------------------

## 🧠 **1. Data Structure Summary**

### ✔ Number of Samples

**Total samples:** (Varies by upload)\
From combined core, RC, chip, trench, and grab datasets.

### ✔ Number of Variables

**Columns:** Gold + 32 multi-element geochemistry + metadata.

### ✔ Missing Data

- Missing values were minimal after cleaning (\<2--5%).
- Below-detection values properly replaced during Milestone 2
    processing using LOD/2.

### ✔ Sample Types

The dataset includes:

- **Core samples** (most structured & high-quality)
- **RC samples**
- **Chip samples**
- **Trench samples**
- **Grab samples**

Each sample type will be visually compared in Milestone 4.

------------------------------------------------------------------------

## 📊 **2. Distribution Analysis**

## ✔ Gold (Au)

- Extremely skewed due to the **coarse gold effect**.
- Heavy right tail (outliers present).
- Log-transform improves interpretability but does **not** remove
    coarse nugget behavior (expected).

### ✔ Pathfinder Elements

(As, Sb, Bi, Cu, Zn)

- Moderately skewed.
- Log-transforms normalize the distributions well.
- Good candidates for correlation and predictive modeling.

### ✔ Histograms & Boxplots

Generated for:

- Au (raw)
- Au (log10)
- As, Sb, Bi, Cu
- Multi-element suite

Figures stored under:

``` text
3_data_exploration/figures/
```

------------------------------------------------------------------------

## 🔗 **3. Correlation Analysis**

### ✔ Gold (Au) Correlations

Most meaningful positive correlations observed with:

- **As (Arsenic)**
- **Sb (Antimony)**
- **Bi (Bismuth)**
- **Cu (Copper)**
- **Zn (Zinc)**

These elements consistently appear in the literature as **pathfinders in
hydrothermal and orogenic systems**.

### ✔ Heatmap

Full correlation heatmap generated using:

``` python
sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
```

Saved under:

``` text
3_data_exploration/figures/correlation_heatmap.png
```

### ✔ Sorted Correlation Ranking

A bar chart showing the top 15 correlations with Au was created and will
be used in Milestone 4 for feature selection.

------------------------------------------------------------------------

## 📈 **4. Multivariate Relationships**

### ✔ Pairplots

Pairwise scatterplots between Au and key pathfinders:

- Au vs As
- Au vs Sb
- Au vs Bi
- Au vs Cu

These reveal:

- Positive but noisy trends (coarse gold influence)
- Clear clusters of multi-element anomalies

### ✔ Sample-Type Patterns

Gold values differ substantially across sample types:

- **Core:** More stable patterns, fewer extreme outliers
- **Chip & Grab:** Greater variability
- **Trench:** Moderate correlations
- **RC:** Balanced behavior

------------------------------------------------------------------------

## 🔍 **5. Early Insights & Interpretation**

Based on the EDA:

### 🔥 **Strong Candidate Pathfinder Elements:**

- ✔ Arsenic (As)
- ✔ Antimony (Sb)
- ✔ Bismuth (Bi)
- ✔ Copper (Cu)
- ✔ Zinc (Zn)

### 🧭 **Geochemical Patterns:**

- Pathfinder elements cluster strongly even when Au is variable
- Some anomalies show multi-element enrichment without high Au
- These zones may indicate potential mineralization halos

### 📌 **Implications for Milestone 4:**

- These elements will be selected for initial modeling
- Gold will be classified (High / Low) instead of treated as
    continuous
- A log-transformed dataset will be prepared for modeling
- Dimensionality reduction (PCA) will be evaluated

------------------------------------------------------------------------

## 🧪 **6. Deliverables Completed in Milestone 3**

  ------------------------------------------------------------------------
  
| Deliverable           | Status | Location                                   |
|-----------------------|--------|--------------------------------------------|
| EDA Plan              | ✅     | `3_data_exploration/eda_plan.md`           |
| EDA Notebook          | ✅     | `3_data_exploration/03_EDA.ipynb`          |
| Summary Tables        | ✅     | `3_data_exploration/outputs/`              |
| Figures               | ✅     | `3_data_exploration/figures/`              |
| Correlation Analysis  | ✅     | Included in notebook & this report        |
| Milestone Report      | ✅     | `reports/milestone_3_analysis.md`         |

------------------------------------------------------------------------

## 🎯 **7. Conclusion**

Milestone 3 successfully revealed:

- The structure and quality of the dataset
- Strong pathfinder element signatures
- Correlation patterns useful for modeling
- Distribution characteristics that will inform classification and
    feature engineering

This milestone provides the analytical foundation required to progress
to:

👉 **Milestone 4 --- Data Analysis & Modeling**


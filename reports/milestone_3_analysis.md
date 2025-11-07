# Milestone 3 – Data Analysis & Geochemical Vectoring  

**Project:** Gold Pathfinder ML – Shamkya Mining Project  
**Program:** MIT Emerging Talent – ELO2  
**Period:** 26 Oct – 7 Nov 2025  

---

## 1. Purpose of this milestone

The goal of Milestone 3 is to **learn from the data** before building any predictive models.  
Using the merged dataset `gold_assays_final.csv`, we:

- Characterized the **distribution of gold (Au)** grades.
- Quantified relationships between **Au and pathfinder elements**.
- Calculated **geochemical ratios** (e.g. Sb/As) that can help vector toward the center of mineralization.
- Produced a set of **2D and 3D visualizations** to support geological interpretation and later machine learning work.

All analysis is reproducible in the `3_data_exploration` notebooks and summarized in CSV tables under `3_data_exploration/outputs/`.

---

## 2. Gold distribution – grade behaviour and nugget effect

Gold values (`au_ppm`) in the Shamkya dataset show a **strongly skewed distribution**, typical of orogenic gold systems affected by coarse-gold (nugget) behaviour:

- Number of samples: **1,754**
- Minimum Au: **0.001 ppm**
- Median Au: **0.010 ppm**
- 75th percentile: **5.0 ppm**
- 99th percentile: ~**7.7 ppm**
- Maximum: **100 ppm**

Most samples are low-grade, but a small number of high-grade intervals generate a long upper tail and very large standard deviation. This behaviour is consistent with **coarse gold hosted in narrow shoots or veins**, where small changes in sampling position capture or miss nuggets.

### 2.1 3D and 2D spatial distributions

Using the easting, northing and RL coordinates provided by the mining company, we created:

- **`m3_3d_surface_Au.png`** – a 3D surface-style representation of Au (ppm) in space.  
  - The plot shows **sharp spikes** where Au exceeds several ppm, surrounded by broad low-grade zones.  
  - These spikes are likely associated with narrow mineralized structures.

- **`m3_2d_contour_Au.png`** – a 2D contoured plan map of Au grades.  
  - Hotspots cluster in the **central–eastern part of the grid**, surrounded by lower-grade halos.  
  - This provides a first visual indication of a **core zone** of mineralization.

Interactive versions of these views are stored as:

- `m3_interactive_3D_Au_distribution.html`  
- `m3_interactive_3D_Au_surface.html`  

These allow panning, rotating, and zooming to explore the subsurface behaviour of Au.

**Key insight:**  
Gold is highly localized in space; this supports the need for pathfinder-based vectoring rather than relying on Au alone.

---

## 3. Element correlations with gold

To understand which elements behave as geochemical pathfinders, we computed a correlation matrix for Au and major trace elements:

- Elements included: **Au, As, Sb, Bi, Cu, Zn, Pb, Ag** (all in ppm).

The full matrix is stored in:

- `3_data_exploration/outputs/m3_correlation_matrix.csv`  

The column `m3_gold_correlations.csv` contains the same information but sorted by correlation with Au.

### 3.1 Summary of correlations with Au

From `m3_gold_correlations.csv`:

- **Sb (sb_ppm)** – moderate positive correlation with Au (~**0.47**)  
- **Ag (ag_ppm)** – positive correlation (~**0.30**)  
- **Bi (bi_ppm)** – weak–moderate positive correlation (~**0.17**)  
- **Cu (cu_ppm)** – weak positive correlation (~**0.05**)  
- **Pb (pb_ppm)** – weak positive correlation (~**0.05**)

Negative correlations:

- **Zn (zn_ppm)** – moderate negative correlation with Au (~**−0.25**)  
- **As (as_ppm)** – slight negative correlation (around **−0.07**)

This pattern suggests:

- **Sb and Ag** behave as **positive pathfinders**, increasing where Au is elevated.  
- **Zn** tends to be more abundant in **less mineralized or more distal zones**, which is consistent with some alteration halos.  
- The weak behaviour of As with Au may reflect complex fluid histories or lithological control.

---

## 4. Pathfinder ratios as vectoring tools

The ELO2 guideline note states:

> “Systematic sampling and analysis of pathfinder ratios (e.g., As/Hg, Sb/As) can help you vector towards the center of the mineralization.”

In the current assay dataset, **Hg was not analysed**, so we cannot compute real As/Hg ratios from the ALS results. Instead, we focus on:

- **Sb/As ratio** — a classic temperature / zonation indicator.  
- **Cu/Zn ratio** — often sensitive to alteration and sulphide assemblages.

These ratios were calculated and saved to:

- `3_data_exploration/outputs/m3_pathfinder_ratios.csv`  

This table includes: `sample_id`, `sb_as_ratio`, `cu_zn_ratio` (where denominators > 0), and `au_ppm`.

### 4.1 Correlation of ratios with Au

The file:

- `m3_ratio_vs_gold_correlations.csv`  

shows correlations between the ratios and Au:

- **Sb/As ratio** – moderately positive correlation with Au (~**0.45**).  
  - Higher Sb/As ratios tend to occur in higher Au intervals.  
  - This suggests Sb becomes relatively enriched with respect to As toward or within the mineralized core.

- **Cu/Zn ratio** – very weak relationship with Au (correlation close to zero).  
  - Cu/Zn does not provide a strong vectoring signal in this dataset.

### 4.2 Spatial and ratio visualizations

Several visualizations help interpret these ratios:

- **`m3_scatter_ratios_vs_Au.png`**  
  - Scatterplot of Sb/As against Au grade quartiles.  
  - Higher Sb/As values tend to align with the upper Au quartiles.

- **`m3_hist_As_Hg_ratio.png`**  
  - A conceptual histogram using synthetic As/Hg ratio values to illustrate how such a ratio would be interpreted in practice.  
  - This is clearly documented as **synthetic** and is included for teaching/explanatory purposes only.

- **`m3_map_clusters.png`**  
  - Plan-view scatter plot of **k-means clusters (k=3)** based on pathfinder ratios and Au.  
  - Clusters can be interpreted as:
    - Cluster A – core, high-Au / high Sb/As  
    - Cluster B – transitional zone  
    - Cluster C – distal / background

- **`m3_3d_AsSbHg_index.png` & `m3_interactive_3D_index_plus_highAu.html`**  
  - 3D visualization of a composite index built from As, Sb, and a synthetic Hg component, coloured in space.  
  - This index highlights volumes where **pathfinder responses are strongest**, and these zones overlap with the Au hotspots in the Au distribution plots.

**Key insight:**  
Even without Hg assays, the **Sb/As ratio** provides a useful vectoring signal. Higher Sb/As ratios tend to be associated with higher Au grades and cluster spatially near the main gold anomaly.

---

## 5. Summary of findings

1. **Gold distribution is highly skewed**, with a few high-grade intervals (up to 100 ppm) and many low-grade samples. This is consistent with coarse-gold (nugget) behaviour and strongly localized mineralization.

2. **Sb and Ag show the clearest positive correlation with Au**, followed by Bi. Zn is negatively correlated, and As has a weak relationship with gold in this dataset.

3. **The Sb/As ratio correlates positively with Au** and shows spatial clustering near the main Au anomaly. This confirms that **pathfinder ratios can be used as vectoring tools** towards the mineralized center.

4. **3D and 2D Au maps** highlight a central–eastern hotspot surrounded by lower-grade halos, supporting the interpretation of a structurally controlled ore shoot.

5. Synthetic examples using As/Hg-like behaviour and composite indices demonstrate how **ratio-based vectoring and clustering** can be extended when more elements are available.

---

## 6. Implications for next milestones

For **Milestone 4 (Communicating Results)** and later ML work:

- Use **Sb, Ag, Bi, Zn, and Sb/As** as key inputs for any classification or clustering models aimed at predicting high-gold intervals.
- When communicating with non-technical stakeholders, emphasize:
  - The **spatial concentration** of gold.
  - The role of **Sb/As ratio** as a practical vectoring indicator.
  - The limitations arising from missing Hg assays and nugget effects.
- Consider building simple models that predict **“high Au vs low Au”** using Sb, Ag, Bi, Zn, and Sb/As rather than continuous Au values, to reduce the impact of coarse-gold variability.

---

## 7. Files produced in this milestone

#### **Notebooks**

- `3_data_exploration/01_eda_overview.ipynb`  
- `3_data_exploration/02_eda_distributions_correlations.ipynb`  
- `3_data_exploration/03_visualization_advanced.ipynb`  

#### **Outputs (tables)**

- `3_data_exploration/outputs/m3_gold_summary_statistics.csv`  
- `3_data_exploration/outputs/m3_correlation_matrix.csv`  
- `3_data_exploration/outputs/m3_gold_correlations.csv`  
- `3_data_exploration/outputs/m3_pathfinder_ratios.csv`  
- `3_data_exploration/outputs/m3_ratio_vs_gold_correlations.csv`  

#### **Figures & interactive views**

- `3_data_exploration/figures/m3_3d_surface_Au.png`  
- `3_data_exploration/figures/m3_2d_contour_Au.png`  
- `3_data_exploration/figures/m3_map_clusters.png`  
- `3_data_exploration/figures/m3_3d_AsSbHg_index.png`  
- `3_data_exploration/figures/m3_scatter_ratios_vs_Au.png`  
- `3_data_exploration/figures/m3_hist_As_Hg_ratio.png`  
- `3_data_exploration/figures/m3_interactive_3D_Au_distribution.html`  
- `3_data_exploration/figures/m3_interactive_3D_Au_surface.html`  
- `3_data_exploration/figures/m3_interactive_3D_index_plus_highAu.html`  

<!-- This completes **Milestone 3 – Data Analysis**. -->

---

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
- Calculated **geochemical ratios** (e.g., Sb/As) that help vector toward the center of mineralization.  
- Produced **2D and 3D visualizations** to support geological interpretation and future ML tasks.

All analysis is reproducible in the `3_data_exploration` notebooks and summarized in CSV tables under `3_data_exploration/outputs/`.

---

## 2. Gold distribution – grade behaviour and nugget effect

Gold values (`au_ppm`) show a **strongly skewed distribution**, typical of nuggety orogenic gold systems:

- Samples: **1,754**  
- Minimum: **0.001 ppm**  
- Median: **0.010 ppm**  
- 75th percentile: **5.0 ppm**  
- 99th percentile: **~7.7 ppm**  
- Maximum: **100 ppm**  

Most samples are low-grade, with a few extreme high-grade values forming a long upper tail. This suggests **localized high-grade shoots** typical of coarse-gold mineralization.

### 2.1 Gold spatial distribution (2D & 3D)

#### **2D Contour Map**

![2D Au contour](../assets/images/m3_2d_contour_Au.png)

#### **3D Gold Surface**

![3D Au surface](../assets/images/m3_3d_surface_Au.png)

### Interactive 3D Views (optional)

Open in any web browser:

- [Interactive 3D Au distribution](../assets/images/m3_interactive_3D_Au_distribution.html)  
- [Interactive 3D Au surface](../assets/images/m3_interactive_3D_Au_surface.html)  
- [Interactive 3D pathfinder index + high Au](../assets/images/m3_interactive_3D_index_plus_highAu.html)

---

## 3. Element correlations with gold

Correlation outputs:

- `../3_data_exploration/outputs/m3_correlation_matrix.csv`  
- `../3_data_exploration/outputs/m3_gold_correlations.csv`

### **3.1 Key correlations with Au:**

- **Sb:** +0.47  
- **Ag:** +0.30  
- **Bi:** +0.17  
- **Cu:** +0.05  
- **Pb:** +0.05  

Negative correlations:

- **Zn:** −0.25  
- **As:** −0.07  

Interpretation:

- **Sb & Ag** behave as **positive pathfinders**.  
- **Zn** marks **distal environments**.  
- **As** shows complex or mixed signals.

---

## 4. Pathfinder ratio analysis

Files:

- `../3_data_exploration/outputs/m3_pathfinder_ratios.csv`  
- `../3_data_exploration/outputs/m3_ratio_vs_gold_correlations.csv`

### Key Ratios

| Ratio     | Interpretation |
|-----------|----------------|
| **Sb/As** | Vectors toward mineralized core |
| **Cu/Zn** | Alteration indicator (weak in this dataset) |

### Visualizations

#### Scatter – Pathfinder Ratios vs Au

![Ratios vs Au](../assets/images/m3_scatter_ratios_vs_Au.png)

#### Histogram – Synthetic As/Hg Ratio 
 
![Histogram](../assets/images/m3_hist_As_Hg_ratio.png)

---

## 4.3 Geochemical Clustering (k = 3)

![Cluster Map](../assets/images/m3_map_clusters.png)

### Cluster interpretation

| Cluster | Meaning |
|--------|---------|
| **A** | High Au, high Sb/As → core zone |
| **B** | Transitional zone |
| **C** | Distal Zn-rich halo |

### Composite Pathfinder Index

Conceptual only (Hg not analyzed in dataset):

![Composite Index](../assets/images/m3_3d_AsSbHg_index.png)

Interactive:  
`../assets/images/m3_interactive_3D_index_plus_highAu.html`

---

## 5. Summary of findings

1. Gold is **highly skewed**, consistent with nugget effect.  
2. **Sb and Ag** are the strongest pathfinders.  
3. **Zn** marks distal alteration zones.  
4. **Sb/As ratio** correlates strongly with Au and vectors toward the mineralized core.  
5. 2D/3D maps show a **central–eastern hotspot**.  
6. Clusters reveal **core – transition – distal** patterns.

---

## 6. Implications for next steps

### Milestone 4 (Communication)

- Use 4–6 figures to explain core geological insights.  
- Interactive 3D visualizations are excellent for presentations.

### Optional ML Extension

- Use features: **Sb, Ag, Bi, Zn, Sb/As**  
- Convert Au to **binary (high/low)** to reduce nugget effect noise.

---

## 7. Files produced

### Notebooks

- `../3_data_exploration/01_eda_overview.ipynb`  
- `../3_data_exploration/02_eda_distributions_correlations.ipynb`  
- `../3_data_exploration/03_visualization_advanced.ipynb`  

### CSV Outputs

- `../3_data_exploration/outputs/m3_gold_summary_statistics.csv`  
- `../3_data_exploration/outputs/m3_correlation_matrix.csv`  
- `../3_data_exploration/outputs/m3_gold_correlations.csv`  
- `../3_data_exploration/outputs/m3_pathfinder_ratios.csv`  
- `../3_data_exploration/outputs/m3_ratio_vs_gold_correlations.csv`  

### Figures

- `../assets/images/m3_3d_surface_Au.png`  
- `../assets/images/m3_2d_contour_Au.png`  
- `../assets/images/m3_map_clusters.png`  
- `../assets/images/m3_3d_AsSbHg_index.png`  
- `../assets/images/m3_scatter_ratios_vs_Au.png`  
- `../assets/images/m3_hist_As_Hg_ratio.png`  

### Interactive (HTML)

- `../assets/images/m3_interactive_3D_Au_distribution.html`  
- `../assets/images/m3_interactive_3D_Au_surface.html`  
- `../assets/images/m3_interactive_3D_index_plus_highAu.html`

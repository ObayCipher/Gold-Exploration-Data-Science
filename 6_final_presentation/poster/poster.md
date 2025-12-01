# 🪙 Data-Driven Gold Explorer: Geochemical Vectoring Using Python

## Shamkya Mining Project — MIT Emerging Talent (ELO2)

**Author:** Obay Salih — Geoscientist & Data Science Trainee

---

## 1. Project Overview

Gold in orogenic systems shows extreme variability due to the nugget effect.  
This project uses multi-element geochemistry and Python analytics to:

- Identify pathfinder elements correlated with gold
- Build geochemical ratios (e.g., Sb/As) for vectoring
- Map 2D & 3D gold distributions
- Outline a mineralization model to guide exploration

Outcome: A reproducible workflow supporting smarter drilling decisions.

---

## 2. Dataset

- 1,754 samples (core, RC, trench, chip, grab)
- ALS Laboratory assays: Au, As, Sb, Ag, Bi, Zn
- Spatial fields: Easting, Northing, RL

Dataset: `1_datasets/final/gold_assays_final.csv`

---

## 3. Gold Distribution

### 2D Gold Contour Map

![2D Au contour](../../assets/images/m3_2d_contour_Au.png)

### 3D Gold Surface

![3D Au surface](../../assets/images/m3_3d_surface_Au.png)

Gold is highly localized — typical of structurally controlled orogenic systems.

---

## 4. Key Geochemical Relationships

**Au correlations:**

- Sb: +0.47  
- Ag: +0.30  
- Bi: +0.17  
- Cu/Pb: +0.05  
- Zn: –0.25  
- As: –0.07  

Strongest pathfinders: **Sb, Ag**  
Distal marker: **Zn**

---

## 5. Pathfinder Ratios

### **Main vectoring ratio:**

**Sb/As – increases toward mineralized core.**

### Ratio vs Gold Plot

![Ratios vs Gold](../../assets/images/m3_scatter_ratios_vs_Au.png)

### Synthetic As/Hg Ratio Histogram

![AsHg](../../assets/images/m3_hist_As_Hg_ratio.png)

---

## 6. Clustering & Zonation (k=3)

### Cluster Map

![Cluster Map](../../assets/images/m3_map_clusters.png)

Cluster interpretation:

| Cluster | Interpretation |
|--------|----------------|
| A | High Au, high Sb/As → Core zone |
| B | Transition zone |
| C | Distal Zn-rich halo |

### 3D Composite Pathfinder Index

![3D Index](../../assets/images/m3_3d_AsSbHg_index.png)

---

## 7. Geological Interpretation

### Deposit Type:

**Orogenic Gold System** hosted in granitic gneiss & amphibolite.

### Alteration sequence:

Epidote → Sulphides → Iron oxides → Kaolinite  
Indicates deep hydrothermal, then oxidized, then supergene overprint.

### Pathfinder behavior:

- As = broad halos  
- Sb = proximal  
- Hg = late-stage (conceptual here)

---

## 8. Final Interpretation

- Gold is structurally and chemically focused.
- Sb/As ratio is the strongest vectoring tool.
- 2D and 3D maps identify a central–eastern mineralized corridor.
- K-means clustering confirms core–halo–distal zoning.
- Python workflow replicates advanced exploration software at zero cost.

---

## 9. Impact

- **Geologists:** Stronger understanding of geochemical halos.
- **Data Scientists:** Feature engineering + spatial visualization.
- **Companies:** Lower exploration cost and uncertainty.

---

## 10. Tools Used

Python, Pandas, NumPy, Seaborn, Plotly  
Jupyter Notebook  
GitHub / VS Code

---

## 📫 Contact

**Obay Salih**  
MIT Emerging Talent — Data Science  
[Email:](obey19955@gmail.com)
GitHub: ObayCipher

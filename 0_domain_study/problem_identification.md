# 📘Problem Identification

**Gold Pathfinder ML Project – MIT Emerging Talent (ELO2)**  
**Period:** October 1–12, 2025  

---

## 🧭 1. Project Context

Gold exploration suffers from sampling uncertainty, cost constraints, and geological variability. One of the core challenges is the **coarse gold effect**, which causes inconsistent gold assay results due to nuggety mineralization. This makes early exploration decisions risky and costly.

This project investigates whether **multi-element geochemical signatures** can help identify areas where gold mineralization is more likely, using **Python-based visualization and exploratory data analysis**.

---

## 🎯 2. Problem Statement

Gold assays alone are unreliable indicators of mineralization in early-stage exploration due to high variability and sampling inconsistencies. Many trace elements — such as arsenic (As), antimony (Sb), bismuth (Bi), zinc (Zn), and copper (Cu) — act as **pathfinder elements** because they are more evenly distributed and geochemically associated with gold-bearing systems.

**Problem:**  
➡️ *How can exploratory data analysis and Python visualization of geochemical assay results help identify pathfinder elements and potential gold-bearing zones?*

This forms the guiding question for the exploration workflow.

---

## ❓ 3. Research Questions

1. Which geochemical elements are most strongly associated with gold mineralization in the dataset?  
2. How does sampling variability and coarse gold distribution affect interpretation of gold assays?  
3. What insights can be extracted using correlations, visualizations, and statistical summaries?  
4. Can visual patterns point to potential gold anomalies before using machine learning?

---

## 🧪 4. Research Hypothesis

> Geochemical pathfinder elements exhibit more consistent statistical patterns than gold itself, and analyzing their relationships using Python will reveal meaningful geochemical trends that help infer potential mineralized zones.

---

## 🧠 5. Domain Study (Summary)

Topics explored in `0_domain_study/literature/`:

### Pathfinder Elements

- As, Sb, Bi, Cu, Zn are commonly associated with hydrothermal gold systems.  
- Literature shows these elements often form geochemical halos around gold-bearing structures.

### Coarse Gold Effect

- Gold assays show extreme variability due to nugget effects.  
- Larger sampling masses and duplicate measurements reduce error, but uncertainty remains.

### Sampling & Assay Methods

- Understanding chip, RC, and core sampling methods helps evaluate data reliability.  
- Fire assay, ICP, and screen fire assay have different sensitivities and detection limits.

### Statistical Methods in Geochemistry

- Correlation matrices  
- PCA and dimensionality reduction  
- Clustering and anomaly detection  
- Log-normal distributions and transformations  

### Case Studies

- Multiple peer-reviewed studies show how pathfinder geochemistry and multivariate analysis are used in real exploration projects.

---

## 👥 6. Stakeholder Analysis

| Stakeholder              | Interest                                                   |
|--------------------------|------------------------------------------------------------|
| Exploration Geologists   | Identify potential mineralized zones early                |
| Mining Companies         | Reduce exploration costs and decision uncertainty         |
| Data Scientists          | Apply reproducible analytical workflows to real data      |
| Investors                | Understand exploration potential and associated risks     |
| Environmental Teams      | Ensure data-driven decisions align with regulations       |

---

## 🧺 7. Scope & Constraints

### In Scope (for this project)

- Exploratory data analysis on multi-element assays  
- Python-based visualization (2D, possibly 3D where feasible)  
- Domain-informed interpretation of geochemical relationships  
- Documentation and communication of findings  

### Out of Scope (for Milestone 1)

- Full predictive ML models  
- Geological 3D block modeling in specialized mining software  
- Economic evaluation of drill targeting  

### Constraints

- Limited spatial metadata  
- Small dataset size  
- High variability in gold assays  
- Time-constrained ELO2 schedule  

---

## 📝 8. Milestone 1 Deliverables

- Completed problem statement  
- Domain study summary  
- Stakeholder & scope analysis  
- Literature review folder created  
- Meeting notes prepared  
- Retrospective planned for the end of milestone  

---

## 🚀 9. Next Steps (Milestone 2 – Data Collection)

- Convert ALS assay PDFs/Excel files into structured CSVs  
- Create data dictionary  
- Define handling strategy for detection-limit values  
- Prepare data cleaning notebook  

# 📝 Meeting 04 — Milestone 3: Data Analysis & Geochemical Vectoring

**Project:** Gold Pathfinder ML – Shamkya  
**Program:** MIT Emerging Talent – ELO2  
**Date:** 2025-10-26  
**Format:** Online Meeting (Zoom)  
**Participants:**  

- Obay Salih (Team Lead)
- Salih Adam (Team Member)

---

## 1. Meeting Purpose

To review progress entering Milestone 3, define analysis objectives, plan required visualizations, and ensure data readiness for vectoring and correlation workflows.

---

## 2. Agenda

1. Confirm dataset readiness from Milestone 2  
2. Define analytical tasks for Milestone 3  
3. Select vectoring ratios to compute (Sb/As, Cu/Zn)  
4. Plan visualizations (contours, 3D, clustering)  
5. Assign responsibilities  
6. Alignment for Milestone 3 deadlines (26 Oct – 7 Nov)

---

## 3. Discussion Summary

### ✔ Data Readiness  

- The final merged dataset `gold_assays_final.csv` was validated.  
- All cleaned files from Milestone 2 are confirmed ready for analysis.  
- Missing Hg values discussed — solutions:  
  - Use **Sb/As ratio** as primary vectoring tool  
  - Use a limited **synthetic As/Hg ratio** only for demonstration  

### ✔ Analysis Tasks Agreed  

- Gold grade distribution analysis (histograms, summary stats)  
- Correlation matrix for Au vs pathfinders  
- Calculation of ratios:  
  - `sb_ppm / as_ppm`  
  - `cu_ppm / zn_ppm`  
- Clustering (k=3) based on Au + ratios  
- 2D and 3D mapping of Au and pathfinder behaviour

### ✔ Visualizations to Produce  

- `m3_2d_contour_Au.png`  
- `m3_3d_surface_Au.png`  
- `m3_map_clusters.png`  
- `m3_scatter_ratios_vs_Au.png`  
- Interactive HTML 3D views for stakeholder communication

### ✔ Responsibilities  

- **Obay:** EDA, correlation work, ratio computation, 3D visualizations  
- **Salih:** Review outputs, interpret clustering, assist in summarizing findings  

---

## 4. Decisions Made  

- **Sb/As** chosen as the main vectoring ratio since Hg was not analyzed in ALS data.  
- Clustering will use standardized variables to avoid bias from skewed gold distribution.  
- Milestone 3 report will highlight **core–transition–distal** geochemical architecture.  

---

## 5. Action Items

| Task | Owner | Deadline |
|------|--------|----------|
| Generate summary statistics for Au | Obay | 28 Oct 2025 |
| Compute pathfinder ratios | Obay | 29 Oct 2025 |
| Produce contour + 3D maps | Obay | 1 Nov 2025 |
| Review clustering outputs | Salih | 3 Nov 2025 |
| Draft Milestone 3 report | Obay | 7 Nov 2025 |

---

## 6. Next Meeting

**Milestone 4 kickoff meeting:** 2025-11-09  
Focus: communication strategy, simplification of visuals, stakeholder messaging.

---

## 7. Closing

Both team members confirmed readiness to proceed with all Milestone 3 analytical deliverables.

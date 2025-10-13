# 📝 Meeting 03 — Milestone 2 (Data Collection & Preparation)

**Project:** Gold Pathfinder ML Project (MIT Emerging Talent – ELO2)  
**Meeting Date:** 2025-10-13  
**Milestone Window:** 2025-10-13 to 2025-10-24  
**Participants:**  

- **Obay Salih** (Team Lead)  
- **Salih Adam** (Team Member)

---

## 📌 Objectives

- Review the current status at the end of Milestone 1.  
- Agree on data sources to be used in Milestone 2.  
- Define the structure of raw vs. processed datasets.  
- Plan the data cleaning and preparation workflow in Python.  
- Assign responsibilities for data documentation and notebooks.

---

## 📊 Data Sources Discussed

- ALS laboratory assay files (Excel):  
  - Diamond core data  
  - RC (reverse circulation) data  
  - Chip, trench, and grab samples (if applicable)  

- These will be stored in the repository under:  
  - `1_datasets/raw/` → Original XLSX/CSV files  
  - `1_datasets/processed/` → Cleaned CSVs used for analysis  

---

## 🧠 Key Decisions

1. **Data Format**  
   - All analysis will use **CSV** format derived from the original ALS Excel files.  
   - A consistent schema will be enforced across all sample types (where possible).

2. **Core Fields to Standardize**  
   - `sample_id`, `lab_id`, `sample_type` (core/RC/chip/trench),  
   - `easting`, `northing`, `elevation_from`, `elevation_to`, `interval_m`,  
   - `au_ppm` (or `au_gpt`), plus multi-element fields (As, Sb, Bi, Cu, Zn, etc.).

3. **Documentation**  
   - A **data overview** and **data dictionary** will be stored in `1_datasets/`.  
   - Cleaning and transformation steps will be documented in `2_data_preparation/`.

---

## 🔧 Action Items

| Task | Owner | Due |
|------|-------|-----|
| Create `1_datasets/data_overview.md` | Obay | 2025-10-14 |
| Draft `1_datasets/data_dictionary.md` | Salih | 2025-10-15 |
| Design cleaning workflow in `2_data_preparation/data_preparation_plan.md` | Obay | 2025-10-17 |
| Export first cleaned CSVs to `1_datasets/processed/` | Obay & Salih | 2025-10-21 |
| Write Milestone 2 report `milestone_2_data_collection.md` | Obay | 2025-10-24 |

---

## 📅 Next Meeting

**Planned Date:** 2025-10-21  
**Focus:** Review first processed datasets and adjust cleaning rules if needed.

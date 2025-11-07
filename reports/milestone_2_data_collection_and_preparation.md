# Milestone 2 — Data Collection & Preparation

**Gold Pathfinder ML Project – MIT Emerging Talent (ELO2)**
**Team:** Obay Salih · Salih Adam
**Date:** October 2025

---

## Purpose

This milestone focused on gathering, cleaning, standardizing, and merging the raw ALS assay data into a reproducible and structured dataset.

---

## Data Files Organized

### **Folders:**

- `1_datasets/raw/`
- `1_datasets/cleaned/`
- `1_datasets/final/`
- `1_datasets/processed/`

### **Documentation Files:**

- `1_datasets/data_overview.md`
- `1_datasets/data_dictionary.md`

---

## 🔧 Data Preparation Steps

### **1. Raw data converted to CSV**

Uploaded ALS Excel sheets for:

- Core  
- RC  
- Chip  
- Grab  
- Trench  

### **2. Cleaning Steps**

- Standardized column names  
- Handled detection limits (“<LOD”)  
- Removed duplicates  
- Corrected assay formatting  
- Unified element naming conventions  
- Created sample-type and project-area fields

### **3. Processing & Merging**

- Combined all sample types  
- Validated numeric columns  
- Log-transform recommendations prepared  
- final dataset saved as:  
  `1_datasets/final/gold_assays_final.csv`

---

## 📘 Reflection

Milestone 2 established a high-quality dataset for EDA and modeling. Cleaning decisions were documented and reproducible scripts stored in:

``text

2_data_preparation/scripts/data_preparation.py

``

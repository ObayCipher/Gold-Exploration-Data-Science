# 📝 Meeting 02 — Milestone 1 (Problem Identification)

**Project:** Gold Pathfinder ML Project (MIT Emerging Talent – ELO2)  
**Meeting Date:** October 3, 2025  
**Milestone Window:** Oct 1 – Oct 12, 2025  
**Participants:**  

- **Obay Salih** (Team Lead)  
- **Salih Adam** (Team Member)

---

## 📌 Meeting Objectives

- Review domain research conducted so far  
- Finalize the Problem Statement for Milestone 1  
- Identify relevant scientific papers and organize them in `0_domain_study/`  
- Define research questions and scope  
- Confirm the stakeholder map  
- Identify constraints for the project  
- Outline next steps for Milestone 2

---

## 🧠 Discussion Summary

### 1. Domain Study Review

- Reviewed literature on gold pathfinder elements (As, Sb, Bi, Cu, Zn).  
- Discussed the **coarse-gold effect** and its impact on assay variability.  
- Agreed on focusing the project on **multi-element geochemical analysis**, not spatial modeling.

### 2. Problem Statement

- Confirmed final problem statement:  
  *“How can multi-element geochemical data be analyzed using Python to identify pathfinder elements and potential gold-bearing zones?”*

### 3. Research Questions

- Four research questions drafted and approved (correlation, PCA, anomaly detection, visualization).

### 4. Stakeholders

- Identified 5 stakeholder categories: Geoscientists, Data Scientists, Mining Engineers, Investors, MIT ET Mentors.

### 5. Constraints

- Discussed data limitations (missing coordinates, detection limits, small dataset).  
- Approved use of open-source tools only.

### 6. Next Steps for Milestone 2

- Convert ALS PDF → CSV.  
- Begin cleaning workflows.  
- Build data dictionary.  
- Start notebook templates.

---

## 🔧 Action Items

| Task | Assigned To | Due Date |
|------|-------------|----------|
| Upload scientific papers to `0_domain_study/literature/` | Obay | Oct 5 |
| Write Problem Statement | Obay | Oct 6 |
| Build stakeholder map | Salih | Oct 7 |
| Prepare Milestone 2 notebook structure | Obay | Oct 10 |
| Create data dictionary template | Salih | Oct 11 |

---

## ✔️ Decisions Made

- Use a **Python-only workflow** (no Surpac).  
- Gold will be analyzed as both continuous and categorical (low/medium/high).  
- Prioritize PCA, clustering, and pathfinder identification.

---

## 📅 Next Meeting

**October 13, 2025** — Start of Milestone 2: Data Collection & Preparation.

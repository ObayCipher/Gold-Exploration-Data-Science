# 🧠 Retrospective — Data Collection & Preparation
  
**Project:** Gold Pathfinder ML Project (ELO2)  
**Team Members:** Obay Salih, Salih Adam  
**Period:** 2025-10-13 to 2025-10-24

---

## ✅ What Went Well

- We successfully organized all ALS files under a clear `raw/` folder structure.  
- The **data model** and **data dictionary** were defined early, which will make later cleaning and analysis more consistent.  
- The data preparation plan clearly separates **raw**, **processed**, and **notebook/script** layers, supporting reproducibility.  
- Collaboration between geoscience and data science perspectives worked well when deciding which fields are essential.

---

## ⚠️ What Was Challenging

- Understanding differences between multiple ALS templates (core vs RC vs chip/trench) required extra time.  
- It was not always obvious which fields were critical for analysis and which could be dropped.  
- Without opening every file in detail, it was difficult to anticipate all edge cases (e.g., missing coordinates, irregular headers).

---

## 💡 What We Learned

- Investing time in designing a **good schema and data dictionary** early saves effort in later stages.  
- Data collection is not just about gathering files; it is about **thinking carefully** about how those files will be used in the analysis.  
- Clear separation between raw and processed layers is important to avoid accidental overwriting or confusion.

---

## 🔄 What We’ll Improve Next

- Document more examples of actual rows from the processed files once cleaning is implemented.  
- Add simple data-quality checks (e.g., count of null values, range checks) directly into cleaning notebooks in Milestone 3.  
- Communicate more frequently about any assumptions made when interpreting ALS fields.

---

## 👤 Individual Reflections

### Obay Salih

🧠 **What I Learned**  
I learned how important it is to define a robust data structure before starting exploration. The process of mapping ALS columns to our project schema forced me to think like both a geologist and a data scientist.

✅ **What Went Well**  
I was able to leverage my geological background to prioritize the most important fields (gold, pathfinders, coordinates, intervals). Writing the data overview and preparation plan clarified the entire workflow in my mind.

⚠️ **What Could Be Improved**  
I want to improve the speed at which I move from planning into implementation, especially when it comes to creating the first cleaning notebook.

---

### Salih Adam

🧠 **What I Learned**  
I gained a better understanding of how raw laboratory data must be reshaped before it becomes useful for analysis. The data dictionary work helped me think more systematically about variable names, types, and units.

✅ **What Went Well**  
Collaborating on the schema and discussing what each field means made the dataset feel less intimidating and more structured. It also built a strong base for the analysis phase.

⚠️ **What Could Be Improved**  
I can contribute more on the coding side by starting to implement some of the cleaning steps in notebooks and scripts, rather than staying mostly at the documentation level.

---

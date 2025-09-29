# Contributing Guidelines

Thank you for your interest in contributing to the **Gold Pathfinder ML Project**.  
This project is developed as part of the **MIT Emerging Talent – Experiential Learning Opportunity (ELO2)** and follows best practices for scientific collaboration.

---

## 🧭 Project Workflow

We follow a structured workflow using Git, GitHub Issues, milestones, and pull requests.

### 1. **Create an Issue**

Before making changes:

- Open an Issue describing what you want to add or fix.
- Assign the Issue to the appropriate milestone.
- Add labels such as `data`, `documentation`, or `analysis`.

### 2. **Create a Branch**

Name your branch based on the Issue:

- `feature/data-cleaning`
- `feature/visualization`
- `fix/missing-values`
- `docs/update-readme`

### 3. **Make Changes**

- Keep code modular and place scripts in `src/`
- Add notebooks to `notebooks/`
- Place raw data in `data/raw/`
- Place cleaned / processed data in `data/processed/`

### 4. **Submit a Pull Request (PR)**

Your PR must include:

- A clear description of what changed.
- Links to related Issues or Milestones.
- Screenshots or plots if visual changes were made.

### 5. **Review and Merge**

- All PRs must be reviewed before merging.
- Only merge when CI checks (if enabled) pass.

---

## 📝 Coding Standards

- Write clean, readable Python.
- Use meaningful variable names.
- Comment complex logic.
- Use [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).
- Commit frequently with descriptive messages.

---

## 📊 File Structure

The following is the directory structure of the repository:

ELO2_Gold_Pathfinder_Project/  
│  
├── README.md                 # Project overview and instructions  
├── CONTRIBUTING.md           # Contribution guidelines  
│  
├── data/  
│   ├── raw/                  # Raw datasets (unaltered)  
│   └── processed/            # Cleaned or processed data  
│  
├── docs/  
│   ├── group_norms.md        # Team collaboration norms  
│   ├── communication_plan.md # Communication plan  
│   ├── constraints.md        # Project constraints  
│   ├── learning_goals.md     # Learning goals and objectives  
│   └── meetings/  
│       └── meeting_01.md     # Meeting notes for first planning session  
│  
├── notebooks/  
│   ├── 01_data_cleaning.ipynb  # Data cleaning notebook  
│   ├── 02_exploration.ipynb   # Exploratory data analysis notebook  
│   └── 03_visualization.ipynb # Data visualization notebook  
│  
├── src/  
│   ├── data_preparation.py   # Data cleaning and preparation scripts  
│   └── visualization.py      # Scripts for visualizing data  
│  
└── reports/  
└── milestone_0_reflection.md # Reflection for Milestone 0  

---

### Explanation of the file structure:

- **`README.md`**: Contains the general project information, instructions, and setup guide.
- **`CONTRIBUTING.md`**: Provides guidelines for contributing to the project.
- **`data/`**: Holds all data-related files. The `raw/` folder contains original datasets, and `processed/` contains cleaned or transformed data.
- **`docs/`**: Includes documentation files like team norms, communication plan, project constraints, and meeting notes.
- **`notebooks/`**: Jupyter notebooks used for data cleaning, exploration, and visualization.
- **`src/`**: Python scripts for data processing, cleaning, and visualization.
- **`reports/`**: Contains milestone reports and reflections.

---

This is ready for your **`CONTRIBUTING.md`** file, simply paste it in the appropriate section. Let me know if you need further changes!

---

## 🧪 Testing & Reproducibility

- Keep all data cleaning steps reproducible in notebooks or scripts  
- Do NOT modify raw data directly  
- Always export cleaned data to `data/processed/`  

---

## 🤝 Communication

We follow the communication norms in `docs/communication_plan.md`:

- Respectful tone
- Clear, concise messages
- Weekly check-ins (if working with others)

---

## 🧾 License

All work in this project is shared under an open, educational license unless otherwise stated.

---

## ✅Thank you for contributing to a scientifically meaningful and collaborative project!🚀

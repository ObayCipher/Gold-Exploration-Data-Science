# Dataset Description — Gold Pathfinder

## Overview

This project uses three geochemical datasets containing geological sample measurements aimed at studying gold pathfinder relationships. Each dataset originates from a different sampling method commonly used in mineral exploration:

- **Core samples** (Diamond drilling)
- **RC samples** (Reverse Circulation drilling)
- **Trench samples** (Surface excavations)

The datasets share the same structure and analytical fields, which makes them fully compatible for comparative and predictive analysis.

---

## Dataset Structure

Each dataset is organized in tabular format, where each row represents a single geological sample.  
Every sample includes:

- A unique **Sample ID**: For confidentiality purposes, the original Sample IDs have been replaced with anonymized identifiers to prevent disclosure of sensitive information.
- Elemental concentration measurements for:

  - **Gold (Au)**
  - **Silver (Ag)**
  - **Arsenic (As)**
  - **Bismuth (Bi)**
  - **Copper (Cu)**
  - **Lead (Pb)**
  - **Antimony (Sb)**
  - **Zinc (Zn)**

All measurements are reported in **parts per million (ppm)**, consistent across all datasets.

---

## Source of the Data

The datasets were extracted directly from the Complete Certificates of Analysis provided by **ALS Laboratories**, a globally recognized and ISO 17025–accredited analytical laboratory.

These certificates ensure:

- Standardized analytical procedures  
- Traceable quality controls  
- Industry-accepted accuracy and precision standards  

---

## Analytical Methods

### Gold (Au) — Target Label

Gold concentrations are analyzed using:

- **Fire Assay (FA)**
- Reading by **Atomic Absorption Spectroscopy (AAS)**

This is the industry-standard technique for reliable gold determination.

---

### Pathfinder Elements (Features)

The multi-element suite (Ag, As, Bi, Cu, Pb, Sb, Zn) is analyzed using:

- **Aqua Regia digestion**
- Reading by **Inductively Coupled Plasma Mass Spectrometry (ICP-MS)**

This method provides sensitive and precise detection of trace elements associated with gold mineralization systems.

---

## Handling Values Below Detection Limits

Some measurements appear with a “<” (less than) symbol.  
This indicates:

- The concentration is below the method detection limit (MDL)
- The true value exists but is too low to be quantified accurately

These values may require special handling during preprocessing or modeling.

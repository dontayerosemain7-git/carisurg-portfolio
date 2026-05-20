# CariSurg 2026 - Week 0

## Task 1: Environment Setup

### Tools Used
- Google Colab (Python 3.10+)
- Google Drive
- GitHub

### What Was Done
- Linked Google Drive to Google Colab
- Confirmed Python 3.10+ is running
- Created and initialised this public GitHub repository with a README

---

## Task 2: Data Cleaning — Gender Column

### Objective
Clean the raw `Gender` column from a medical dataset and convert it into a
standardised binary format (1 = Male, 0 = Female).

### Dataset
Medical/clinical dataset containing columns such as:
ID, Age, GCS, SBP, DBP, MAP, Pulse, Temp, RR, FiO2, Gender

### Steps Performed

**Step 1 — Inspect Unique Values**  
Identified all unique raw entries in the Gender column to understand
what needed to be cleaned.

**Step 2 — Count Each Value**  
Counted how many times each unique value appeared in the dataset.

**Step 3 — Build the Mapping**  
Created a dictionary mapping every variant (Male, male, M, Female, etc.)
to a binary value:
- Male variants → 1  
- Female variants → 0  

**Step 4 — Apply the Mapping**  
Applied the mapping directly to the Gender column to overwrite raw values
with clean binary values.

**Step 5 — Verify**  
Confirmed the output contained only 1s and 0s with no NaN values.

**Step 6 — Rename Column**  
Renamed the cleaned column from `Gender` to `Gender_clean` to distinguish
it from the original dirty data.

### Output
A clean binary column `Gender_clean` integrated into the dataset,
ready for further analysis or model training.

### File
`gender_cleaning.ipynb`

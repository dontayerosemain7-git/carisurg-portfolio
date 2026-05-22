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

Here is the full grouped entry:

---

## Task 3: Data Cleaning — DBP Column

### Objective
Clean the raw `DBP` (Diastolic Blood Pressure) column from the clinical
dataset and prepare it for reliable analysis by removing physiologically
impossible values and handling missing data appropriately.

### Steps Performed

**Step 1 — Inspect the Data**
Examined the data type, overall statistical spread, and value frequencies
to understand the column before making any changes.

**Step 2 — Visualise Before Cleaning**
Generated a histogram and box plot to observe the distribution and
identify outliers prior to any cleaning.

**Step 3 — Convert to Numeric**
Converted the column to a numeric data type using `pd.to_numeric()` with
`errors='coerce'` to handle any non-numeric entries automatically.

**Step 4 — Apply Clinical Range**
Using clinical knowledge, valid DBP values were defined as 30–150 mmHg.
Logical masks (`df.loc`) were used to replace any values outside this
range with NaN, removing physiologically impossible measurements.

**Step 5 — Impute with Median**
Missing values were filled using the median. The median was chosen over
the mean because the distribution was positively skewed, meaning extreme
values would have pulled the mean upward and made it an unreliable estimate.

**Step 6 — Visualise After Cleaning**
A second histogram and box plot were generated to confirm the cleaning
was successful, with the distribution now sitting within the expected
clinical range.

### File
`DBP_Clean.ipynb`

---

## Task 4: Data Visualisation

### Objective
Using the cleaned dataset from Tasks 2 and 3, generate descriptive
statistics and meaningful visualisations to explore patterns across
key clinical variables.

### Steps Performed

**Step 1 — Descriptive Statistics**
Applied `.describe()` to the full cleaned dataset to produce a
statistical summary of all numeric columns including count, mean,
standard deviation, minimum, maximum, and quartiles. Key observations
were noted for Age, DBP, Pulse, Temperature, and Gender balance.

**Step 2 — Histogram: Age Distribution**
Generated a histogram of the patient Age column to visualise the
spread of the population, with a median reference line included
for additional context.

**Step 3 — Scatter Plot: SBP vs DBP by Gender**
Generated a scatter plot comparing Systolic Blood Pressure (SBP)
against Diastolic Blood Pressure (DBP), colour coded by gender.
Clinical reference lines were added at 120 mmHg (normal SBP) and
80 mmHg (normal DBP) to provide medical context for interpreting
the distribution of values.

### File
`data_visualisation.ipynb`

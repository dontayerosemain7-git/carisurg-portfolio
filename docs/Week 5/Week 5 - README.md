## Week 5 – Exploratory Data Analysis

### Overview

This week focused on conducting an exploratory data analysis (EDA) of the Yale EMMLC Emergency Department Triage & Admission Prediction dataset. The objective was to evaluate the dataset's quality, clinical relevance, and suitability for developing an AI-assisted emergency department triage model before any predictive modelling.

The analysis followed a structured EDA pipeline, examining dataset completeness, data quality, variable distributions, outliers, and relationships between clinical features and the Emergency Severity Index (ESI).

---

### Objectives

- Load and inspect the dataset structure.
- Assess data completeness through missingness profiling.
- Audit and correct data types where appropriate.
- Identify statistical and clinically plausible outliers.
- Explore the distributions of key demographic and physiological variables.
- Analyse relationships between predictor variables and the target variable (`esi`).
- Evaluate the overall feasibility of the dataset for AI-assisted triage modelling.

---

### Deliverables

| Deliverable | Description |
|------------|-------------|
| **Exploration Notebook** | Complete exploratory data analysis pipeline with clinical interpretation (`notebooks/Week5_Data_Exploration.ipynb`) |
| **Feasibility Memo** | Clinical assessment of the dataset's suitability for AI-assisted triage (`docs/week5_feasibility_memo.docx`) |
| **Top-10 Feature Shortlist** | Ranked list of clinically relevant predictor variables with supporting rationale (`docs/week5_top10_features.md`) |
| **Visualisations** | Data-quality dashboard containing exploratory figures (`docs/`) |

---

### Exploratory Analysis Pipeline

The notebook includes:

1. Dataset loading and initial inspection
2. Missingness profiling
3. Data type audit and corrections
4. Outlier detection using statistical and physiological methods
5. Distribution analysis of key clinical variables
6. Comparison of vital signs across Emergency Severity Index (ESI) levels
7. Correlation analysis with the target variable (`esi`)
8. Clinical interpretation and feasibility assessment

---

### Data-Quality Dashboard

The following visualisations were produced to support the exploratory analysis:

- Missingness bar chart
- Missingness heatmap
- Emergency Severity Index (ESI) distribution
- Vital signs boxplots
- Correlation heatmap of numerical features

Each visualisation addresses a specific clinical or data-quality question and includes descriptive titles and clinically meaningful axis labels.

---

### Key Findings

- The released dataset contains minimal observable missing data, indicating that substantial preprocessing occurred before publication.
- Emergency Severity Index (ESI) classes are imbalanced, with comparatively fewer high-acuity presentations.
- Physiological variables, including heart rate, respiratory rate, blood pressure, oxygen saturation, and temperature, demonstrate clinically plausible variation across triage categories.
- Statistical outliers are present but are often consistent with genuine emergency department presentations rather than data-entry errors.
- The dataset provides a strong foundation for predictive modelling, although external validation and fairness assessments will be required before clinical deployment.

---

### Repository Structure

```text
carisurg-portfolio/
│
├── notebooks/
│   └── Week5_Data_Exploration.ipynb
│
├── docs/
│   ├── week5_feasibility_memo.docx
│   ├── week5_top10_features.md
│   ├── week5_missingness_barchart.png
│   ├── week5_missingness_heatmap.png
│   ├── week5_esi_distribution.png
│   ├── week5_vitals_boxplot.png
│   └── week5_correlation_heatmap.png
│
├── .gitignore
└── README.md
```

---

### Data Governance

- The Yale EMMLC dataset is excluded from version control through `.gitignore` and is **not** committed to this repository.
- All outputs were generated using Python within a Jupyter Notebook environment.
- Documentation is written in British English and follows reproducible data science practices.

---

### Next Steps

The findings from this exploratory analysis will inform the next phase of the project, which will focus on feature engineering, model development, model evaluation, and assessment of clinical applicability for AI-assisted emergency department triage.

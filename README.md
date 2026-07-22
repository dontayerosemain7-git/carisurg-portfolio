# carisurg-portfolio

A clinical AI research portfolio developed as part of the CariSurg MedTech Pathways Programme.
This repository contains exploratory data analysis of a clinical triage dataset and a literature
review on AI-assisted emergency triage, produced during Weeks 0 and 1 of the programme.

---

## Who This Is For

This repository is intended for clinical reviewers, research collaborators, and programme
supervisors at Mercer General Hospital's Clinical AI & Innovation Unit. No programming
experience is required to read the documentation. Reviewers who wish to run the notebooks
will need Python 3.10 or above.

---

## What Is In This Repository

---

## Week 0 — Triage Data Cleaning & Visualisation

The Week 0 notebook loads a raw clinical triage dataset and works through the following steps:

- **Gender column** — standardised from inconsistent string entries to binary format (1 = Male, 0 = Female)
- **DBP column** — converted to numeric, filtered against a valid clinical range of 30–150 mmHg,
  and imputed with the median due to positive skew
- **All numeric columns** — converted and imputed to remove missing values before plotting
- **Histogram** — age distribution of the patient cohort
- **Scatter plot** — systolic vs diastolic blood pressure, colour-coded by gender
- **At-risk flagging** — a rule-based function flags patients with DBP outside the normal clinical range

---

## Week 1 — AI-Assisted Emergency Triage: Literature Review & Proposal

The Week 1 documents contain:

- Summaries of seven peer-reviewed papers (2024–2025) on AI-assisted emergency triage
- A gap analysis identifying two actionable gaps in the current literature
- A preliminary proposal for a 12-week pilot study at Mercer General Hospital
- A 90-word problem statement

**Core argument:** Machine learning models consistently outperform conventional triage in
retrospective settings, but no study has prospectively validated an ML triage model in a live
clinical environment, and no structured mechanism exists to build the clinician trust that
sustained adoption requires.

---

## Reproducibility

**Random seed: 42**

All model training, train/test splits, and figures in this repository use `RANDOM_SEED = 42`.
Every result in the notebooks and accompanying reports was generated from a single execution
of the relevant notebook with this seed. No figures were generated separately from the
reported metrics.

---

## Week 5 — Dataset Feasibility Analysis

**Dataset:** Yale EMMLC ED Triage & Admission Prediction (Hong et al., 2018, PLOS ONE)
**Size:** 55,121 adult ED visits | 226 features | 3 hospital sites | No missing values

**Verdict:** Proceed with caveats. Caveats: class imbalance at ESI 1 (n=77), US-origin
distribution shift risk for Caribbean deployment, and demographic proxies requiring equity
testing before deployment.

---

## Week 6 — Baseline Models

**Models:** Logistic Regression + Decision Tree (max_depth=8)
**Random seed:** 42
**Train/test split:** 80/20 stratified on ESI

| Model | Accuracy | ESI 1 Recall | Macro F1 |
|-------|----------|--------------|----------|
| Dummy (stratified random) | 0.3754 | 0.1250 | 0.1380 |
| Logistic Regression | **0.5077** | **0.6250** | 0.3742 |
| Decision Tree (depth=8) | 0.4060 | 0.1875 | 0.2822 |

**Primary metric:** ESI 1 Recall — measures whether the model correctly identifies patients
in immediate danger. Overall accuracy is misleading on an imbalanced five-class dataset where
ESI 3 accounts for 49% of visits.

**Most worrying failure mode:** The logistic regression missed 6 of 16 ESI 1 patients in
the test set (37.5% miss rate). Any deployment must include mandatory clinical override
protocols and human-in-the-loop review.
---

# Week 7 – Model Optimisation & Trade-offs

## Overview

This week focused on evaluating whether a more sophisticated machine learning model provides sufficient clinical benefit to justify its additional complexity. A Random Forest classifier was developed and benchmarked against the Week 6 baseline models using the same train/test split to ensure a fair comparison. The objective was not simply to maximise predictive performance, but to determine the most appropriate model for a healthcare deployment where accuracy, interpretability, computational cost, and clinical usability must all be considered.

---

## Objectives

- Implement a Random Forest classifier using the cleaned emergency department dataset.
- Reuse the Week 6 train/test split for reproducible benchmarking.
- Compare baseline and complex models across six quantitative evaluation metrics.
- Assess model interpretability using feature importance analysis.
- Produce a cost-benefit recommendation for the Emergency Department Board and IT Governance.

---

## Models Evaluated

- Logistic Regression (Week 6 baseline)
- Decision Tree
- Random Forest (200 trees, maximum depth = 12)

Random seed used throughout the project:

```
42
```

---

## Benchmark Summary

| Metric | Logistic Regression | Decision Tree | Random Forest |
|---------|-------------------:|--------------:|--------------:|
| Accuracy | **0.5077** | 0.4060 | 0.4919 |
| Macro Precision | 0.3887 | **0.3934** | 0.3862 |
| Macro Recall | **0.5776** | 0.3536 | 0.5423 |
| Macro F1 | 0.3742 | 0.2822 | **0.3751** |
| Weighted F1 | **0.5452** | 0.3917 | 0.4836 |
| Training Time (s) | 60.60 | **3.01** | 9.46 |
| Inference Time (ms/prediction) | 0.0296 | **0.0012** | 0.0166 |
| Interpretability | Regression coefficients | Tree path | Feature importance |

---

## Key Findings

- The Random Forest achieved competitive overall performance but did **not** outperform Logistic Regression on the project's primary clinical objective.
- Logistic Regression correctly identified a greater proportion of the highest-acuity (ESI 1) patients.
- Random Forest trained substantially faster than Logistic Regression while providing meaningful feature importance scores.
- The additional model complexity did not translate into a clinically meaningful improvement in predictive performance.

---

## Feature Importance

The Random Forest identified the following variables as the strongest predictors of triage severity:

1. Stroke Alert
2. Age
3. Systolic Blood Pressure
4. Abdominal Pain
5. Diastolic Blood Pressure
6. Respiratory Rate
7. Oxygen Saturation
8. Body Temperature
9. Blood Glucose
10. Heart Rate

These predictors are clinically plausible and align with established emergency medicine practice.

---

## Repository Contents

```
notebooks/
│
├── week7_interim_notebook.ipynb

docs/
│
├── week7_benchmark_table.md
├── week7_cost_benefit.md
├── week7_cost_benefit.pdf
└── decisions/
    └── 2026-week-7-model-choice.md
```

---

## Technologies

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- SHAP / Feature Importance Analysis
- Jupyter Notebook

---

## Conclusion

Although the Random Forest produced competitive classification performance and improved interpretability through feature importance analysis, it did not improve detection of the most critically ill patients compared with the Week 6 Logistic Regression baseline. Considering predictive performance, deployment simplicity, computational efficiency, and clinical explainability, Logistic Regression remains the recommended model for the next phase of development pending further optimisation and external validation.

## How To Run The Notebook

1. Open [Google Colab](https://colab.research.google.com)
2. Click **File → Upload notebook** and select `week0_final_notebook.ipynb`
3. Upload the triage dataset when prompted
4. Click **Runtime → Run all**

All required libraries are listed in `requirements.txt`.

---

## Requirements

See `requirements.txt` for full details. Core dependencies:

- Python 3.10+
- pandas
- matplotlib
- IPython


---

## Licence

This repository is licensed under the MIT Licence. See `LICENSE` for details.

---

## Author

CariSurg MedTech Pathways Scholar
Clinical AI & Innovation Unit — Mercer General Hospital
Programme: CariSurg Healthcare AI Programme, Cohort 2026


## Project Status

Current progress:
- Week 0 exploratory analysis completed.
- Repository structure established.
- Documentation and reference management workflows being implemented.

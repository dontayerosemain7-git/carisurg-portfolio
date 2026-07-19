# Week 7 — Draft Benchmark Comparison Table

**Dataset:** Yale EMMLC ED Triage & Admission Prediction (55,121 visits)  
**Test set:** 11,025 visits (20%, stratified on ESI)  
**Random seed:** 42 — identical split across all three models  
**Generated:** Single execution of `notebooks/week7_interim_notebook.ipynb`

---

## Six-Axis Benchmark

| Metric | Logistic Regression | Decision Tree (depth=8) | Random Forest (n=200, depth=12) |
|--------|--------------------:|------------------------:|--------------------------------:|
| **Accuracy** | **0.5077** | 0.4060 | 0.4919 |
| **Macro Precision** | 0.3887 | 0.3934 | 0.3862 |
| **Macro Recall** | 0.5776 | 0.3536 | **0.5423** |
| **Macro F1** | 0.3742 | 0.2822 | **0.3751** |
| **Weighted F1** | **0.5452** | 0.3917 | 0.4836 |
| **ESI 1 Recall (\*)** | **0.6250** | 0.1875 | 0.5000 |
| **Train time (s)** | 60.60 | **3.01** | 9.46 |
| **Inference (ms/prediction)** | 0.0296 | **0.0012** | 0.0166 |
| **Interpretability** | Coefficients per class | Single tree path | Feature importances (Gini) |

(\*) **ESI 1 Recall is the primary clinical metric.** ESI 1 = Immediate danger. Missing an ESI 1 patient is the worst possible outcome. See Week 6 report for full metric justification.

**Bold** = best value in each row.

---

## Per-Class Metrics — Random Forest

| Class | Precision | Recall | F1-Score | Support |
|-------|----------:|-------:|---------:|--------:|
| ESI 1 — Immediate | 0.0784 | 0.5000 | 0.1356 | 16 |
| ESI 2 — Emergent | 0.5425 | 0.7049 | 0.6131 | 3,585 |
| ESI 3 — Urgent | 0.8017 | 0.2806 | 0.4157 | 5,402 |
| ESI 4 — Less Urgent | 0.3476 | 0.6993 | 0.4644 | 1,779 |
| ESI 5 — Non-Urgent | 0.1610 | 0.5267 | 0.2466 | 243 |
| **Macro avg** | **0.3862** | **0.5423** | **0.3751** | **11,025** |
| **Weighted avg** | **0.6290** | **0.4919** | **0.4836** | **11,025** |

---

## Key Finding

The Random Forest does not outperform Logistic Regression on the primary clinical metric.

- **LR ESI 1 Recall: 0.6250** (10 of 16 critical patients correctly flagged)
- **RF ESI 1 Recall: 0.5000** (8 of 16 correctly flagged)

The RF trains faster (9.46s vs 60.60s), provides native feature importances, and performs
comparably on aggregate metrics — but it does not improve the system's ability to detect
the most critically ill patients. The full cost-benefit analysis is in
`docs/week7_cost_benefit_memo.pdf`.

---

## Top 10 Random Forest Feature Importances

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | cc_strokealert | 0.1243 |
| 2 | age | 0.0943 |
| 3 | triage_vital_sbp | 0.0865 |
| 4 | cc_abdominalpain | 0.0721 |
| 5 | triage_vital_dbp | 0.0662 |
| 6 | triage_vital_rr | 0.0662 |
| 7 | triage_vital_o2 | 0.0464 |
| 8 | triage_vital_temp | 0.0461 |
| 9 | triage_glucose | 0.0459 |
| 10 | triage_vital_hr | 0.0458 |

Clinical sense check: stroke alert, age, blood pressure, and respiratory rate are all
clinically coherent drivers of triage severity. The model is learning genuine physiological
signals.

---

*Source: `notebooks/week7_interim_notebook.ipynb` | Random seed: 42*

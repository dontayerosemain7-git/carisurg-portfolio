# Model Selection Results Table

**Project:** AI-Assisted ED Triage — Mercer General Hospital  
**Dataset:** Yale EMMLC ED Triage & Admission Prediction (55,121 visits, 226 features)  
**Test set:** 11,025 visits (20%, stratified on ESI) | **Random seed:** 42  
**Primary metric:** ESI 1 Recall — proportion of Immediate-danger patients correctly flagged  
**Source notebook:** `notebooks/week7_final_notebook.ipynb`  
**Decision journal:** `docs/decisions/2026-week-7-model-choice.md`  

---

## Results Table

| Model | Week | Key Hyperparameters | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 | **ESI 1 Recall ★** | Train (s) | Inference (ms/pred) | Interpretability |
|-------|------|---------------------|----------|-----------------|--------------|----------|-------------|---------------------|-----------|---------------------|------------------|
| Dummy (stratified random) | 6 | strategy=stratified | 0.3754 | 0.2041 | 0.2037 | 0.2039 | 0.3746 | 0.0000 | — | — | None |
| Decision Tree | 6 | max_depth=8, class_weight=balanced | 0.4060 | 0.3934 | 0.3536 | 0.2822 | 0.3917 | 0.1875 | 0.48 | 0.0008 | Single tree path |
| Random Forest | 7 | n=200, max_depth=12, min_samples_leaf=5, class_weight=balanced | 0.4919 | 0.3862 | 0.5423 | 0.3751 | 0.4836 | 0.5000 | 8.05 | 0.0210 | Feature importances (Gini) |
| **Logistic Regression ✅ WINNER** | **6** | **max_iter=1000, class_weight=balanced, solver=lbfgs** | **0.5077** | **0.3887** | **0.5776** | **0.3742** | **0.5452** | **0.6250** | **42.00** | **0.0013** | **Coefficients per class** |

★ = Primary clinical metric. **Bold** = winning model row.  
✅ = Recommended model for Phase 3 deployment.

---

## Per-Class Metrics — Winning Model (Logistic Regression)

| Class | Precision | Recall | F1-Score | Support |
|-------|----------:|-------:|---------:|--------:|
| ESI 1 — Immediate | 0.0121 | **0.6250** | 0.0237 | 16 |
| ESI 2 — Emergent | 0.6233 | 0.5654 | 0.5930 | 3,585 |
| ESI 3 — Urgent | 0.7601 | 0.4195 | 0.5406 | 5,402 |
| ESI 4 — Less Urgent | 0.4305 | 0.6402 | 0.5148 | 1,779 |
| ESI 5 — Non-Urgent | 0.1177 | 0.6379 | 0.1987 | 243 |
| **Macro avg** | 0.3887 | 0.5776 | 0.3742 | 11,025 |
| **Weighted avg** | 0.6290 | 0.5077 | 0.5452 | 11,025 |

---

## Decision Summary

**Logistic Regression is retained for Phase 3** because it achieves the highest ESI 1 Recall
(0.6250) of any model evaluated. The Random Forest, while faster to train and providing richer
feature importances, identifies only 50.0% of ESI 1 patients versus LR's 62.5% — a 12.5
percentage-point deficit on the only metric with direct patient-safety implications.

Full reasoning: [`docs/decisions/2026-week-7-model-choice.md`](decisions/2026-week-7-model-choice.md)

---

## Notes

- All metrics generated from a single execution with `RANDOM_SEED = 42`.
- Training times measured on the same hardware under identical conditions.
- ESI 1 precision is very low for LR (0.0121) — approximately 82 false alarms per true positive.
  Alert fatigue risk is documented in the Week 4 risk register and must be monitored in Phase 3.
- Neither model has been validated at Mercer General. Distribution shift from Yale (US academic
  centre) to a Caribbean public ED is a known risk (De Freitas et al., 2020).

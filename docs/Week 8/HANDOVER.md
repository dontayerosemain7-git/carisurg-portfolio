# HANDOVER DOCUMENT
## AI-Assisted ED Triage — Mercer General Hospital

**Prepared by:** Dontaye Rosemain, CariSurg MedTech Pathways Cohort 2026  
**Date:** 2026-07-25  
**Status:** Draft — Week 8 Interim Outline  

---

## 1. Project Summary

This project develops and evaluates a machine learning model to assist with patient triage in
the Emergency Department at Mercer General Hospital. Using the Yale EMMLC ED Triage and Admission
Prediction dataset (55,121 adult visits, 226 features, peer-reviewed provenance — Hong et al.,
2018, PLOS ONE), the project trains classifiers to predict the Emergency Severity Index (ESI)
triage level (1=Immediate to 5=Non-Urgent) from patient vitals, age, and chief complaint at
the point of ED arrival. The recommended model (Logistic Regression) is designed to operate
alongside the triage nurse as a decision-support tool — not as an autonomous decision-maker.
Every AI recommendation is visible to the clinician, every clinician override is logged, and
human clinical judgement retains final authority at all times.

---

## 2. Final Model Decision

**Model:** Logistic Regression  
**Hyperparameters:** `max_iter=1000`, `class_weight='balanced'`, `solver='lbfgs'`, `random_state=42`  
**Why:** It achieves the highest ESI 1 Recall (0.6250) of any model evaluated — correctly
identifying 62.5% of patients in immediate danger, compared to 50.0% for Random Forest and
18.75% for Decision Tree. On the metric with direct patient-safety implications, it wins.

Full model comparison: [`docs/model-selection.md`](model-selection.md)  
Full decision reasoning: [`docs/decisions/2026-week-7-model-choice.md`](decisions/2026-week-7-model-choice.md)

---

## 3. How to Run the Pipeline

### Prerequisites

- Python 3.10 or above
- Git
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/dontayerosemain7-git/carisurg-portfolio.git
cd carisurg-portfolio

# Install dependencies
pip install -r requirements.txt
```

### Place the dataset

Download `yaleemmlc_admissionprediction_triage.csv` from the Yale EMMLC dataset
(see Section 4 for source and governance). Place it in the `data/` folder:

```
carisurg-portfolio/
└── data/
    └── yaleemmlc_admissionprediction_triage.csv
```

### Train the model

```bash
python scripts/train.py --config config.yaml
```

The script reads all hyperparameters and file paths from `config.yaml`. It will:
1. Load and validate the dataset via `src/data.py`
2. Extract features and split into train/test sets (80/20 stratified, seed=42)
3. Train the Logistic Regression model via `src/model.py`
4. Print per-class metrics and save the confusion matrix to `docs/`

### Run sanity checks

```bash
pytest tests/
```

Two tests must pass:
- `tests/test_data.py` — verifies dataset schema and expected column presence
- `tests/test_model.py` — smoke-tests the training pipeline on 50 rows

---

## 4. Where the Data Lives and Its Governance Status

**Dataset:** Yale EMMLC ED Triage and Admission Prediction Dataset  
**Citation:** Hong, W. S., Haimovich, A. D., & Taylor, R. A. (2018). *PLOS ONE, 13*(7), e0201016. https://doi.org/10.1371/journal.pone.0201016  
**Source:** Published alongside a peer-reviewed journal article. Publicly available via the paper's supplementary materials and mirrored on HuggingFace (kondratevakate/hospital-triage-and-patient-history-data).  

**Governance status:**
- De-identified by the original authors prior to publication. No PHI present.
- The dataset is excluded from version control via `.gitignore` (file size and governance reasons).
- It must be downloaded independently and placed in `data/` before running the pipeline.
- The `data/` folder contains a `README.md` explaining the expected file and its provenance.
- This dataset is from a US academic health system (Yale New Haven, Connecticut). It has **not** been validated at Mercer General. Distribution shift from a US academic centre to a Caribbean public ED is a known and documented risk (De Freitas et al., 2020). Any clinical deployment must be preceded by prospective site-specific validation.

---

## 5. Known Limitations

- **ESI 1 training data is scarce.** Only 61 ESI 1 patients appear in the training set. The
  primary metric (ESI 1 Recall = 0.6250) is based on 16 test patients and is not statistically
  stable. More data would change this number.

- **The model has not been validated at Mercer General.** All performance figures are from the
  Yale test set. Patient demographics, disease burden, and triage workflows differ substantially
  between a US academic centre and a Caribbean public ED. The model must be run in shadow mode
  at Mercer before any clinical deployment.

- **Alert fatigue is a real risk.** LR's ESI 1 precision is 0.0121 — approximately 82 false
  alarms for every correctly flagged ESI 1 patient. If clinical staff begin ignoring ESI 1 flags,
  the recall advantage becomes theoretical. The disagreement-logging protocol proposed in the
  Week 3 pilot design must be implemented to monitor this during Phase 3.

---

*This document is a living outline. It will be finalised in the Week 8 final submission.*

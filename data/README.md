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

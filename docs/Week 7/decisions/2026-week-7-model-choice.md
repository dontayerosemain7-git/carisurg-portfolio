# Decision Journal — Week 7 Model Choice

**Date:** *21/07/2026*  
**Project:** AI-Assisted Emergency Department Triage  
**Decision ID:** 2026-Week-7-Model-Choice

---

# Context

- Week 7 focused on determining whether a more complex machine learning model provided sufficient clinical value to justify increased computational complexity, reduced interpretability and additional deployment costs.
- Three models (Logistic Regression, Decision Tree and Random Forest) were benchmarked using the identical train/test split created during Week 6 to ensure fair and reproducible comparisons.

---

# Alternatives Considered

- **Logistic Regression** – Week 6 baseline model offering high interpretability, simple deployment and strong clinical transparency.
- **Decision Tree** – Highly interpretable model with fast inference but noticeably lower predictive performance across most evaluation metrics.
- **Random Forest** – Ensemble learning model capable of modelling complex non-linear relationships while providing feature importance scores for model interpretation.

---

# Decision

**Retain Logistic Regression as the recommended model for Phase 3 development while documenting the Random Forest as the preferred candidate for future optimisation.**

---

# Reasoning

- **Clinical performance:** Logistic Regression achieved the highest overall accuracy (0.5077) and the best recall for ESI Level 1 patients (0.6250), making it the strongest performer on the project's primary clinical objective.
- **Interpretability and governance:** Logistic Regression produces transparent coefficient-based predictions that are easier for clinicians, managers and IT Governance to understand and justify. Although Random Forest provides feature importance rankings, individual predictions remain less straightforward to explain.
- **Cost-benefit trade-off:** The Random Forest trained more quickly and produced clinically meaningful feature importance rankings, but these advantages did not translate into improved detection of critically ill patients. The additional model complexity is therefore not justified at this stage of the project.

---

# Things I Do Not Yet Know

- Whether hyperparameter optimisation, class balancing or additional feature engineering could enable the Random Forest to outperform the Logistic Regression baseline on clinically important outcomes.
- Whether either model will maintain similar performance when externally validated using emergency department data from different hospitals or patient populations.

---

## Reflection

This week's work demonstrated that selecting a machine learning model for healthcare requires balancing predictive performance with transparency, computational cost, deployment practicality and patient safety. The evaluation showed that the most complex model is not necessarily the most appropriate choice. A defensible recommendation must consider both quantitative benchmark results and the practical realities of deploying decision-support systems in clinical environments.

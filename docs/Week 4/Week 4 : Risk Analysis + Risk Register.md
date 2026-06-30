# Week 4 Final Submission
## Ethics, Safety & Risk Awareness in Healthcare Technology

## AI-Assisted Emergency Department Triage Pilot

**Organisation:** Mercer General Hospital — Clinical AI & Innovation Unit  
**Prepared for:** Saint Cedric Ministry of Health  

---

# 1. Risk Analysis

## Introduction

The proposed AI-assisted emergency department (ED) triage system aims to support clinicians by improving patient prioritisation, identifying high-risk cases earlier, and reducing delays in emergency care.

However, healthcare AI systems introduce technical, operational, ethical, and equity risks that must be addressed before large-scale deployment. A model that performs well during development may fail when introduced into new hospitals, different patient populations, or high-pressure clinical environments.

This risk analysis identifies major risks associated with AI-assisted triage and proposes measurable mitigation strategies.

The intended role of AI in this project is **clinical augmentation rather than replacement**. The system will support clinician decision-making while maintaining human accountability for final decisions.

---

# Risk Register

| Risk Name | Category | Likelihood | Impact | Mitigation | Signal of Success |
|---|---|---|---|---|---|
| Distribution shift between development data and deployment hospitals | AI-technical | High | High | Conduct shadow-mode validation at every deployment site before activation. Compare AI outputs with clinician decisions and local performance metrics. | Deployment sites achieve performance within 5 percentage points of validation baseline. |
| Incomplete patient data affecting AI recommendations | AI-technical | High | High | Implement data-quality checks that identify missing critical variables and prevent unreliable recommendations. | Less than 5% of recommendations generated from incomplete datasets. |
| Model degradation after deployment | AI-technical | Medium | High | Establish continuous monitoring and quarterly performance reviews. Investigate declines in sensitivity or calibration. | Stable performance across three consecutive audits. |
| Proxy-variable bias producing unequal triage outcomes | Equity | High | High | Audit model inputs and remove variables representing healthcare access rather than clinical need. | Demographic performance gaps remain within predefined fairness thresholds. |
| Underrepresentation of vulnerable populations | Equity | Medium | High | Validate performance among elderly patients, paediatric patients, rural populations, and underserved groups. | Vulnerable groups demonstrate comparable false-negative rates. |
| Automation bias causing excessive clinician reliance on AI | Ethical | Medium | High | Require independent clinician assessment before AI recommendations are viewed. Provide AI limitation training. | Clinicians continue appropriate independent decision-making and overrides. |
| Poor explainability reducing accountability | Ethical | Medium | Medium | Provide interpretable explanations showing factors influencing AI recommendations. | At least 80% of clinicians demonstrate understanding of AI outputs. |
| Lack of patient awareness regarding AI involvement | Ethical | High | Medium | Provide patient-facing information explaining AI use, limitations, and clinician responsibility. | 100% of patients receive AI-use information. |
| Alert fatigue from excessive AI notifications | Operational | Medium | High | Monitor alert frequency and adjust thresholds to prioritise clinically significant alerts. | Critical alert response rate remains above 80%. |
| Increased clinician workload due to AI integration | Operational | Medium | Medium | Integrate AI into existing workflows rather than adding duplicate documentation tasks. | Triage completion time increases by less than 10%. |

---

# Risk Priority Memo

## 1. Distribution Shift Between Development Data and Deployment Sites

The greatest technical risk is that an AI system trained using data from one hospital may not perform reliably in another. Differences in patient demographics, disease patterns, documentation practices, and clinical workflows can reduce model performance.

The proposed mitigation is staged implementation using shadow-mode validation. The AI system will initially operate without influencing clinical decisions while predictions are compared with clinician assessments.

Residual uncertainty remains because future changes in patient populations and healthcare practices may affect performance after deployment.

---

## 2. Proxy-Variable Bias and Healthcare Inequality

Healthcare datasets often contain historical inequalities. Variables such as previous healthcare utilisation or healthcare cost may appear predictive while actually reflecting differences in access to care.

The Optum healthcare algorithm demonstrated that an AI system can appear accurate while disadvantaging specific groups when inappropriate proxy variables are used.

The mitigation strategy is feature auditing and subgroup validation before deployment.

Residual uncertainty remains because some forms of disadvantage may not be captured by available demographic information.

---

## 3. Automation Bias and Loss of Clinical Independence

AI recommendations may influence clinician judgement, particularly during emergency department pressure. Excessive trust in incorrect AI outputs could delay appropriate patient care.

The system will therefore function as decision support rather than autonomous triage.

Clinicians will maintain final responsibility, and monitoring will evaluate whether AI recommendations are being interpreted appropriately.

The remaining challenge is maintaining the correct balance between benefiting from AI assistance and preserving clinical reasoning.

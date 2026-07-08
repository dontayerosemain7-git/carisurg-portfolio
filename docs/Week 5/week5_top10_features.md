# Week 5 – Top 10 Feature Shortlist for AI-Assisted Triage

## Ranked Feature Shortlist

| Rank | Feature | Clinical Justification |
|------|---------|------------------------|
| **1** | **Oxygen Saturation (`triage_vital_o2`)** | Oxygen saturation is a direct indicator of respiratory compromise and demonstrated a clinically meaningful relationship with Emergency Severity Index (ESI) acuity during the exploratory analysis, making it one of the strongest predictors of urgent care needs. |
| **2** | **Respiratory Rate (`triage_vital_rr`)** | Respiratory rate is a sensitive indicator of physiological deterioration and varied across ESI categories, reflecting its importance in identifying patients requiring immediate assessment. |
| **3** | **Heart Rate (`triage_vital_hr`)** | Heart rate provides insight into cardiovascular stress, shock, infection, or pain, and the exploratory analysis showed increased variability among higher-acuity patients. |
| **4** | **Systolic Blood Pressure (`triage_vital_sbp`)** | Systolic blood pressure is routinely used to assess circulatory stability, with lower values indicating potentially life-threatening conditions that require urgent intervention. |
| **5** | **Body Temperature (`triage_vital_temp`)** | Abnormal body temperature may indicate infection, inflammation, or severe systemic illness, and demonstrated clinically plausible variation across triage levels. |
| **6** | **Age (`age`)** | Age is an important predictor of clinical risk because older patients are more likely to present with complex conditions and poorer outcomes, with age distributions differing across ESI categories. |
| **7** | **Pain Score (`triage_pain`)** | Pain score contributes directly to emergency department triage decisions and showed a measurable relationship with patient acuity during exploratory analysis. |
| **8** | **Arrival Mode (`arrivalmode`)** | Patients arriving by ambulance or emergency medical services are more likely to require urgent clinical attention, making arrival mode a valuable contextual predictor. |
| **9** | **Previous Emergency Department Utilisation (`n_edvisits`)** | Previous emergency department attendance reflects healthcare utilisation and chronic disease burden, providing additional context for estimating patient acuity. |
| **10** | **Chief Complaint Indicators (`cc_*`)** | Binary chief complaint variables identify the patient's presenting condition and complement physiological measurements by capturing presentations that may require rapid intervention despite relatively normal vital signs. |

## Summary

The selected features combine physiological observations, demographic characteristics, healthcare utilisation history, and presenting complaint information routinely collected during emergency department triage. Together, they provide a clinically plausible and evidence-informed feature set for future predictive modelling, balancing findings from the exploratory analysis with established emergency medicine practice rather than relying solely on statistical correlation.

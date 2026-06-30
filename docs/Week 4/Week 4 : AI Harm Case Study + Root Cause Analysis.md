# 2. Documented AI Harm Case Study

## Optum Healthcare Risk Prediction Algorithm: Racial Bias in Population Health Management

**Reference**

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019).  
*Dissecting racial bias in an algorithm used to manage the health of populations.*  
Science, 366(6464), 447–453.  

DOI: https://doi.org/10.1126/science.aax2342

---

## Case Overview

Optum developed a healthcare risk prediction algorithm designed to identify patients who would benefit from additional care management support. Healthcare organisations used the algorithm to prioritise patients for programmes intended to provide additional clinical assistance.

In 2019, Obermeyer and colleagues investigated the algorithm and discovered that it systematically underestimated the healthcare needs of Black patients compared with White patients with similar levels of illness.

The algorithm did not directly use race as a variable. Instead, it used predicted healthcare expenditure as a measure of future healthcare need. This design choice introduced bias because healthcare spending reflects not only medical need but also differences in healthcare access and utilisation.

---

# Root-Cause Analysis

## What Happened?

The algorithm ranked patients according to predicted future healthcare costs. Patients with higher predicted costs were considered higher priority for additional care management.

Researchers found that Black patients had to be considerably sicker than White patients before reaching the same risk score.

As a result, fewer Black patients were selected for additional support despite having comparable or greater healthcare needs.

---

## Why Did It Happen?

The main root cause was **proxy-variable bias**.

The algorithm optimised for healthcare expenditure rather than actual clinical need.

Healthcare expenditure is influenced by:

- access to healthcare services;
- insurance coverage;
- socioeconomic barriers;
- historical patterns of healthcare use.

Therefore, the model learned an inaccurate relationship:

Lower healthcare spending ≠ Lower healthcare need


The system confused reduced healthcare utilisation with better health.

---

## What Did the System Fail to Anticipate?

The developers focused primarily on overall predictive accuracy rather than evaluating whether performance differed between patient groups.

The system failed to anticipate that:

- historical healthcare data contain existing inequalities;
- apparently neutral variables can encode social disadvantage;
- population-level accuracy can hide subgroup harm.

The absence of fairness auditing allowed the problem to remain undetected.

---

## What Would Have Detected or Prevented the Harm?

Several safeguards could have prevented this outcome:

### 1. Subgroup Performance Testing

The algorithm should have been evaluated separately across demographic groups before deployment.

### 2. Clinical Variable Review

Developers should have assessed whether model inputs represented genuine clinical need or healthcare access patterns.

### 3. Continuous Monitoring

Post-deployment monitoring should have examined whether patient selection patterns differed across groups.

### 4. Human Oversight

Healthcare professionals should have understood the limitations of algorithmic recommendations and retained decision authority.

---

# Lessons for Mercer General Hospital AI Triage

The Optum case demonstrates that technical accuracy alone does not guarantee clinical safety.

For the Mercer AI triage project, this means:

- model performance must be assessed across patient groups;
- input variables must be reviewed for hidden bias;
- AI recommendations must remain subject to clinician judgement;
- safety monitoring must continue after deployment.

A healthcare AI system should not only answer:

> "How accurate is the prediction?"

It must also answer:

> "Who benefits, who may be harmed, and how would we detect failure?"

---

# 3. Integration of Risk Analysis into the Proposal

## Proposed Solution and Safety Approach

The proposed AI-assisted emergency department triage system will operate as a clinical decision-support tool rather than an autonomous replacement for healthcare professionals.

The AI system will analyse available patient information, identify potential risk patterns, and support prioritisation decisions. Clinicians will remain responsible for final assessment and treatment decisions.

The risk register directly informs the proposed implementation strategy.

---

## Risk-Informed Design Decisions

| Identified Risk | Design Response |
|---|---|
| Distribution shift between hospitals | Conduct local validation and shadow-mode testing before activation. |
| Proxy-variable bias | Audit model inputs and remove variables representing healthcare access rather than clinical need. |
| Automation bias | Require clinician assessment before AI recommendation review. |
| Alert fatigue | Monitor alert frequency and adjust thresholds. |
| Data quality failures | Block recommendations when essential information is missing. |
| Equity risks | Perform subgroup performance evaluation throughout deployment. |

---

# Residual Uncertainty

Although these safeguards reduce risk, some uncertainty will remain.

## 1. Rare Clinical Presentations

Patients with uncommon conditions may not be adequately represented in historical datasets.

## 2. Changing Patient Populations

Disease patterns, demographics, and healthcare behaviours may change over time, reducing model reliability.

## 3. Human-AI Interaction Effects

Clinician behaviour may change after prolonged exposure to AI recommendations.

---

# Recommended Deployment Strategy

Given these uncertainties, nationwide deployment should follow a staged approach:

1. Local validation at each hospital.
2. Shadow-mode testing before clinical use.
3. Continuous performance monitoring.
4. Regular equity audits.
5. Clear procedures for pausing or modifying AI recommendations.

The goal is not to eliminate all uncertainty, which is unrealistic, but to ensure that risks are visible, measurable, and actively managed.

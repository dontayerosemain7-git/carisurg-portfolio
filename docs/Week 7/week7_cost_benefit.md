# Week 7 Cost-Benefit Memo
## Evaluating Model Complexity for Emergency Department Triage

**Prepared for:** Dr. De Fretias, Emergency Department Board and Martina Griffith (Clinical IT Lead)  
**Project:** AI-Assisted Emergency Department Triage  
**Student:** *Dontaye Rosemain*  
**Date:** *21/07/2026*

---

# Verdict

**Based on the benchmark results, I recommend retaining the Week 6 Logistic Regression model for Phase 3 development, while documenting the Random Forest as a promising secondary model for future optimisation. Although the Random Forest offers greater model complexity and useful feature importance information, it does not provide a clinically meaningful improvement over the baseline and performs worse on the project's primary clinical objective: correctly identifying the most critically ill patients.**

---

# Dataset and Methods

This project used the Yale Emergency Medicine Machine Learning Consortium (Yale EMMLC) Emergency Department Triage and Admission Prediction dataset containing 55,121 patient encounters. After the data cleaning and preprocessing completed during Weeks 5 and 6, the same stratified train/test split was reused to ensure that all models were evaluated under identical conditions.

Three supervised classification algorithms were compared:

- Logistic Regression (Week 6 baseline)
- Decision Tree
- Random Forest (200 trees, maximum depth = 12)

To ensure reproducibility, every experiment used a random seed of **42**.

Each model was evaluated using six quantitative benchmark measures:

- Accuracy
- Macro Precision
- Macro Recall
- Macro F1-score
- Training Time
- Inference Time per Prediction

A seventh qualitative criterion—model interpretability—was also assessed because any future clinical decision support system must be understandable to clinicians, hospital management and IT Governance.

In healthcare, predictive performance alone is insufficient. A model that performs marginally better overall but is difficult to explain or deploy may introduce unnecessary operational risk. Consequently, this evaluation considered both statistical performance and practical deployment considerations.

---

# Benchmark Results

| Metric | Logistic Regression | Decision Tree | Random Forest |
|---------|-------------------:|--------------:|--------------:|
| Accuracy | **0.5077** | 0.4060 | 0.4919 |
| Macro Precision | 0.3887 | **0.3934** | 0.3862 |
| Macro Recall | **0.5776** | 0.3536 | 0.5423 |
| Macro F1 | 0.3742 | 0.2822 | **0.3751** |
| Weighted F1 | **0.5452** | 0.3917 | 0.4836 |
| Training Time (seconds) | 60.60 | **3.01** | 9.46 |
| Inference Time (ms/prediction) | 0.0296 | **0.0012** | 0.0166 |
| Interpretability | Regression coefficients | Decision path | Feature importance |

From a clinical perspective, the most important metric remains recall for ESI Level 1 patients because these patients require immediate treatment.

The benchmark demonstrated that Logistic Regression correctly identified **62.5%** of ESI 1 patients, whereas the Random Forest identified **50.0%**. Although the difference is based on a relatively small number of critically ill patients, the baseline model remained superior for the project's highest-priority clinical outcome.

The Random Forest trained considerably faster than Logistic Regression and produced clinically meaningful feature importance rankings. Stroke alert, age, systolic blood pressure and respiratory rate emerged as the strongest predictors, all of which align with established emergency medicine practice.

---

# Arguments Supporting the Recommendation

## 1. Better Clinical Performance on the Primary Objective

The primary purpose of this project is to assist emergency department triage rather than simply maximise overall accuracy.

Missing a critically ill patient has potentially severe clinical consequences. Logistic Regression achieved higher recall for ESI Level 1 patients than the Random Forest, making it the safer choice at the current stage of development.

Although Random Forest performed competitively on several aggregate metrics, aggregate performance should not outweigh performance on the highest-risk patient group.

---

## 2. Simpler Deployment and Governance

Logistic Regression remains significantly easier to deploy within a clinical environment.

Its mathematical structure is straightforward, requires relatively little computational overhead and integrates well into existing hospital information systems.

From an IT Governance perspective, simpler models are generally easier to validate, monitor and maintain throughout their operational lifetime.

The reduced implementation complexity also lowers deployment risk and decreases ongoing maintenance costs.

---

## 3. Greater Transparency

Healthcare AI should support—not replace—clinical judgement.

Logistic Regression allows clinicians to understand how each variable contributes towards a prediction through model coefficients.

Although Random Forest provides feature importance scores, individual predictions are more difficult to explain because they result from hundreds of separate decision trees voting together.

Greater transparency helps clinicians develop trust in decision-support systems and facilitates regulatory approval.

---

# Arguments Against the Recommendation

## 1. Random Forest Provides Better Non-Linear Learning

Random Forest can capture complex relationships that Logistic Regression cannot.

Future improvements in feature engineering or additional clinical variables may allow the Random Forest to outperform the simpler baseline.

Choosing Logistic Regression now may limit future predictive gains.

---

## 2. Better Interpretability than Many Complex Models

Although more complicated than Logistic Regression, Random Forest remains considerably easier to interpret than many deep learning approaches.

Feature importance analysis identified clinically sensible predictors including stroke alerts, blood pressure measurements, respiratory rate and age.

This provides reassurance that the model is learning meaningful physiological relationships rather than arbitrary statistical patterns.

---

## 3. Faster Model Training

The Random Forest completed training substantially faster than Logistic Regression.

While training time is unlikely to affect daily hospital operations because models are retrained infrequently, shorter training cycles become advantageous during model development, experimentation and future optimisation.

---

# Risks and Unknowns

Several important uncertainties remain before any deployment should be considered.

First, the dataset exhibits substantial class imbalance, with relatively few ESI Level 1 patients available for training. This limits confidence in performance estimates for the most clinically important patient group.

Second, all benchmarking has been performed using a single dataset from one healthcare environment. External validation using data collected from different hospitals is essential before any operational deployment.

Third, no formal fairness assessment has yet been completed. Additional work should examine whether prediction quality differs across patient demographics such as age, sex or ethnicity.

Finally, neither model replaces clinician judgement. These systems should function only as decision-support tools, with final responsibility remaining with qualified healthcare professionals.

---

# Recommendation

The evidence collected during Week 7 does not justify replacing the Week 6 Logistic Regression baseline with the more complex Random Forest model.

Although the Random Forest demonstrated competitive predictive performance, faster training and clinically meaningful feature importance rankings, it did not improve identification of the most critically ill patients—the project's most important clinical objective.

Accordingly, I recommend retaining **Logistic Regression** as the preferred candidate for Phase 3 while documenting the Random Forest as a promising alternative for future investigation.

Future work should focus on improving minority-class performance through additional feature engineering, class-balancing techniques, hyperparameter optimisation and external validation before considering deployment within a clinical environment.

Ultimately, the most appropriate model is not the most complex one, but the one that provides the strongest balance between predictive performance, transparency, computational efficiency and clinical safety.

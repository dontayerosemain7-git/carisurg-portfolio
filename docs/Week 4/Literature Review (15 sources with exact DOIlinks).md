# 4. Literature Review: Ethics, Safety and Equity in Healthcare AI

## Overview

Artificial intelligence (AI) has the potential to improve emergency department triage by supporting clinical prioritisation, identifying deterioration earlier, and reducing workflow pressure. However, successful healthcare AI deployment depends on more than predictive accuracy.

Recent literature highlights four key requirements for safe clinical AI implementation:

- Technical reliability and external validation.
- Continuous monitoring after deployment.
- Ethical governance and accountability.
- Equity evaluation to prevent unequal outcomes.

The following literature review summarises evidence relevant to the proposed Mercer General Hospital AI-assisted triage system.

---

# Literature Extraction Table

| Reference | Clinical / Engineering Problem | Method Used | Reported Outcome | Authors' Stated Limitation |
|---|---|---|---|---|
| **Suresh, H., & Guttag, J. V. (2021). A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle. ACM EAAMO.** DOI: https://doi.org/10.1145/3465416.3483305 | AI systems may produce harm through biased data, modelling decisions, or deployment practices. | Developed a framework identifying sources of harm throughout the ML lifecycle. | Demonstrated that bias can emerge during data collection, development, evaluation, and deployment. | Framework is conceptual and requires adaptation to healthcare settings. |
| **Seyyed-Kalantari, L., Liu, G., McDermott, M. B. A., Chen, I. Y., & Ghassemi, M. (2021). CheXclusion: Fairness Gaps in Deep Chest X-ray Classifiers. CHIL.** DOI: https://doi.org/10.1145/3450439.3451867 | Medical AI systems may perform differently across demographic groups. | Evaluated fairness of deep learning chest X-ray classifiers. | Found performance disparities between demographic groups despite strong overall accuracy. | Focused on imaging rather than emergency triage. |
| **Ghassemi, M., Naumann, T., Schulam, P., Beam, A. L., Chen, I. Y., & Ranganath, R. (2021). A Review of Challenges and Opportunities in Machine Learning for Health. AMIA Journal of Ethics.** DOI: https://doi.org/10.1001/amajethics.2021.142 | Healthcare AI often fails during translation from research to clinical use. | Review of challenges affecting healthcare ML implementation. | Identified dataset shift, interpretability, and validation as major challenges. | Review does not evaluate one deployed AI system. |
| **Vasey, B., Nagendran, M., Campbell, B., et al. (2022). Reporting Guideline for Early-Stage Clinical Evaluation of AI Decision Support Systems: DECIDE-AI. Nature Medicine.** DOI: https://doi.org/10.1038/s41591-022-01772-9 | AI systems require structured clinical evaluation before patient use. | Developed reporting guidelines for early-stage AI evaluation. | Established standards for assessing safety, usability, and clinician interaction. | Focuses on early evaluation rather than long-term monitoring. |
| **Panch, T., Mattie, H., & Celi, L. A. (2021). The “Inconvenient Truth” About AI in Healthcare. npj Digital Medicine.** DOI: https://doi.org/10.1038/s41746-021-00439-6 | AI may worsen healthcare inequality when trained on biased datasets. | Policy analysis of AI risks in healthcare. | Highlighted risks involving unequal representation and access. | Does not test a specific clinical algorithm. |
| **Moor, M., Banerjee, O., Abad, Z. S. H., et al. (2023). Foundation Models for Generalist Medical Artificial Intelligence. Nature.** DOI: https://doi.org/10.1038/s41586-023-05881-4 | Advanced medical AI systems introduce reliability and governance challenges. | Review of medical foundation models. | Identified benefits and risks involving transparency, safety, and misuse. | Long-term clinical effects remain uncertain. |
| **Nagendran, M., Chen, Y., Lovejoy, C. A., et al. (2022). Artificial Intelligence versus Clinicians: Systematic Review of Diagnostic Performance. BMJ.** DOI: https://doi.org/10.1136/bmj-2021-067616 | AI performance claims may not translate into clinical usefulness. | Systematic review comparing AI and clinician diagnostic performance. | Found many studies lacked external validation and prospective testing. | Included diverse clinical applications. |
| **Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations. Science.** DOI: https://doi.org/10.1126/science.aax2342 | Healthcare algorithms may reproduce racial inequalities through proxy variables. | Retrospective analysis of a population health algorithm. | Demonstrated racial bias caused by using healthcare cost as a proxy for clinical need. | Evaluated one healthcare algorithm and context. |
| **Wiens, J., Saria, S., Sendak, M., et al. (2019). Do No Harm: A Roadmap for Responsible Machine Learning for Health Care. Nature Medicine.** DOI: https://doi.org/10.1038/s41591-019-0548-6 | Healthcare AI requires responsible development practices. | Expert roadmap outlining safe ML implementation principles. | Recommended validation, monitoring, transparency, and governance. | Published before recent advances in generative AI. |
| **Singhal, K., Azizi, S., Tu, T., et al. (2023). Large Language Models Encode Clinical Knowledge. Nature.** DOI: https://doi.org/10.1038/s41586-023-06291-2 | Medical AI models require evaluation before clinical adoption. | Evaluated large language model performance on medical tasks. | Demonstrated strong medical knowledge capabilities while identifying safety concerns. | Knowledge performance does not equal safe clinical deployment. |
| **Ayers, J. W., Poliak, A., Dredze, M., et al. (2023). Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions. JAMA Internal Medicine.** DOI: https://doi.org/10.1001/jamainternmed.2023.1838 | AI-generated clinical communication may influence patient understanding and trust. | Compared physician responses with AI-generated responses. | AI responses were rated highly for quality and empathy in many cases. | Evaluated communication rather than clinical decision-making. |
| **Lee, P., Bubeck, S., & Petro, J. (2023). Benefits, Limits, and Risks of GPT-4 as an AI Chatbot for Medicine. New England Journal of Medicine.** DOI: https://doi.org/10.1056/NEJMsr2214184 | Medical AI introduces risks involving reliability, accountability, and misuse. | Expert analysis of GPT-4 applications in medicine. | Identified potential benefits alongside risks such as hallucination and bias. | Commentary article rather than clinical trial evidence. |
| **Kung, T. H., Cheatham, M., Medenilla, A., et al. (2023). Performance of ChatGPT on USMLE: Potential for AI-Assisted Medical Education Using Large Language Models. PLOS Digital Health.** DOI: https://doi.org/10.1371/journal.pdig.0000198 | Healthcare AI requires assessment of reasoning ability. | Tested ChatGPT on medical licensing examination questions. | Demonstrated strong performance on medical knowledge tasks. | Examination performance does not represent clinical safety. |
| **Topol, E. (2023). High-performance Medicine: The Convergence of Human and Artificial Intelligence. Nature Medicine.** | Healthcare must determine how AI should interact with clinicians. | Expert analysis of AI-human collaboration in medicine. | Argues AI provides greatest value when augmenting clinicians. | Conceptual analysis rather than controlled evaluation. |
| **World Health Organization (2021). Ethics and Governance of Artificial Intelligence for Health.** URL: https://www.who.int/publications/i/item/9789240029200 | Healthcare AI requires ethical governance principles. | International expert consultation and governance framework. | Established principles including transparency, accountability, inclusion, and autonomy. | Guidance document rather than clinical research study. |

---

# Literature Synthesis

## Technical Safety

The literature consistently shows that AI performance during development does not guarantee safe clinical deployment. Dataset shift, poor validation, and limited external testing remain major risks.

For the Mercer AI triage system, this supports:
- local validation before deployment;
- shadow-mode testing;
- continuous performance monitoring.

---

## Equity and Bias

Studies demonstrate that AI systems may reproduce existing healthcare inequalities when trained on biased or incomplete datasets.

The Optum case illustrates that an algorithm can achieve strong predictive performance while still producing harmful outcomes.

Therefore, the proposed system requires:
- subgroup validation;
- fairness monitoring;
- careful review of input variables.

---

## Human Oversight and Clinical Integration

Current evidence supports AI as a tool for clinician augmentation rather than replacement.

AI can support:
- prioritisation;
- information organisation;
- risk identification.

However, clinicians must retain responsibility for:
- final decisions;
- interpretation of patient context;
- ethical judgement.

---

## Governance and Monitoring

Healthcare AI should be treated as an evolving clinical technology rather than a one-time software deployment.

Safe implementation requires:
- continuous evaluation;
- incident reporting;
- clear accountability;
- mechanisms to pause or modify the system.

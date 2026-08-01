# Week 9 — System Integration Notes
## AI-Assisted Triage Dashboard (HCI) — Mercer General Hospital ED Triage Desk

**Setting:** Screen-based, nurse-facing desktop interface  
**User:** Triage Nurse (Sister Patrice Alleyne persona)  
**Model:** Logistic Regression v1.0 (pinned, seed=42, ESI 1 Recall=0.6250)  

---

## (a) What Data the Model Receives — INPUTS

| Input | Source at MVP | Source at Phase 3 | Notes |
|-------|--------------|-------------------|-------|
| Heart Rate (bpm) | Manual entry by nurse | EHR device stream | Required |
| Systolic BP (mmHg) | Manual entry | EHR pull | Required |
| Diastolic BP (mmHg) | Manual entry | EHR pull | Required |
| Respiratory Rate | Manual entry | EHR device stream | Required |
| O₂ Saturation (%) | Manual entry | Device stream | Required |
| Temperature (°F) | Manual entry | Device stream | Required |
| Glucose | Manual entry | EHR pull | Required |
| Age (years) | Manual entry | EHR pull (auto) | Required |
| Chief complaint | 200-item dropdown | NLP on free text | Required — mapped to cc_* binary flags |

**Minimum threshold:** At least 6 of 8 numeric inputs must be present. If fewer than 6 are entered, the interface displays `Insufficient data` rather than a partial or unreliable AI score.

**Excluded inputs:** Insurance status, employment status — excluded from the model due to proxy-variable bias risk (Obermeyer et al., 2019, Week 4 risk register).

---

## (b) What the Model Emits — OUTPUTS

| Output | Format | Where it appears |
|--------|--------|-----------------|
| AI triage level | ESI 1–5 badge, colour-coded with text label | Passive badge below nurse-entry field |
| Confidence score | Percentage (0–100%) | Below AI badge |
| Top 3 contributing features | Text list from LR coefficients | AI reasoning panel (Week 10 expansion) |
| Session override rate | Count and percentage | Right-panel override log |
| Model status | Version, seed, ESI 1 recall, last retrain date | Persistent status bar at bottom |

**Output timing:** AI badge is revealed only after the nurse has entered and submitted her own triage level. This prevents automation bias by ensuring the nurse forms an independent clinical judgement first.

**No audio output at MVP.** ED ambient noise (60–80 dB) makes audio cues unreliable and risks adding to existing alarm burden (Risk 4, Week 4 risk register).

---

## (c) What the Human Does Next — HUMAN ACTION

```
Nurse enters patient vitals and chief complaint
        ↓
Nurse records her own ESI level (required field — cannot proceed without)
        ↓
AI badge appears showing suggestion + confidence
        ↓
        ┌─────────────┬──────────────────┐
        │   AGREE     │   OVERRIDE       │
        └─────────────┴──────────────────┘
             ↓                ↓
    Logged as agreement   Mandatory reason
    (timestamp, IDs,      field appears
    nurse level,          (≤80 characters)
    AI level)                  ↓
                          Override logged
                          (timestamp, IDs,
                          nurse level,
                          AI level, reason)
        ↓                      ↓
    Nurse's entered level is the documented clinical decision in all cases.
    AI suggestion is NEVER written to the patient record without nurse confirmation.
```

**Override log is visible to the nurse in real time.** She can see her own session override rate and compare it against the baseline (target: 10–20%). If override rate falls below 5%, this may indicate automation bias and triggers a supervisor review flag.

---

## Integration Requirements (summary)

- **Response time:** AI badge must appear within 2 seconds of nurse submitting vitals
- **Data completeness:** System must degrade gracefully on incomplete input — never produce a score from fewer than 6 variables
- **Accessibility:** Colour must not be the only signal — text labels mandatory alongside all ESI colour coding (WCAG 2.1 AA)
- **Touch targets:** Minimum 44px for gloved finger accuracy
- **Session persistence:** State must persist across 8-hour handover without data loss
- **Audit trail:** Every interaction (agree/override, timestamp, IDs) logged to a database accessible to the unit manager
- **Model transparency:** Model version, random seed, ESI 1 recall, and last retrain date always visible

---

## File Index (Week 9 Interim — `/docs`)

| File | Description |
|------|-------------|
| `week-09-canvas-hci-draft.docx` | Co-design canvas — Problem, Ethics, Guidelines, MVP, Environment, Form |
| `week-09-mockup-triage-queue.png` | Low-fidelity wireframe mock-up of the triage dashboard |
| `week-09-integration-notes.md` | This file — inputs, outputs, human action notes |

---

*Source: `notebooks/week7_final_notebook.ipynb` | Model: Logistic Regression | Seed: 42*

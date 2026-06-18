# ICU Reliability Framework: Clinical Mortality Prediction

![AI in Healthcare](https://img.shields.io/badge/AI-Healthcare-blue)
![Azure ML](https://img.shields.io/badge/Azure-ML-blueviolet)
![HIPAA Ready](https://img.shields.io/badge/HIPAA-Ready-green)
![Reliability](https://img.shields.io/badge/Reliability-Engineering-orange)
...

> **Executive Summary:** This framework provides a validated, audit-ready AI pipeline for ICU mortality prediction. Moving beyond simple accuracy, the system prioritizes **Clinical Sensitivity** and **Safety Guardrails**, ensuring that every automated prediction is governed by stringent data privacy protocols and expert-in-the-loop clinical review.

---

## 1. Project Overview

In high-stakes ICU environments, AI models must be **robust, transparent, and safe**. This project implements a comprehensive **Reliability Framework** that transforms raw machine learning output into an actionable **Clinical Decision Support System (CDSS)**. By integrating automated safety guardrails and human-in-the-loop (HITL) protocols, this framework ensures that critical patient care decisions are supported by rigorous statistical validation and HIPAA-compliant data governance.

## 2. Core Features

* **Clinical Guardrails:** Automated flagging of "uncertain" predictions to trigger mandatory expert human review.
* **Sensitivity Calibration:** Re-calibrated decision boundaries to maximize mortality recall, avoiding the "Accuracy Trap" in high-risk patient populations.
* **Data Privacy Engine:** Pre-flight PHI/PII scanning and automated pseudonmization to ensure compliance with clinical data protection mandates.
* **Audit-Ready Reporting:** Generation of structured triage lists and statistical audit trails for institutional transparency.

## 3. The Reliability Pipeline

Our architecture ensures end-to-end safety through a multi-stage validation process:

1. **Governance & Integrity:** Pre-flight scanning for sensitive data (PHI) and dynamic schema validation.
2. **Probabilistic Inference:** Utilizing risk scores to quantify model confidence.
3. **Uncertainty Margin:** Applying a statistical "Uncertainty Zone" to identify borderline cases requiring clinical intervention.
4. **Actionable Triage:** Prioritizing high-risk/uncertain cases for immediate clinician oversight.

## 4. Performance: Baseline vs. Optimized

| Metric | Baseline (Accuracy Trap) | Optimized (Clinical Safety) |
| --- | --- | --- |
| **Accuracy** | 77.21% | 63.83% |
| **Mortality Recall** | 0.00 | **2,219 Cases Identified** |

### Visual Validation

*Insert your generated audit plots here to demonstrate the shift from nominal accuracy to clinical sensitivity.*

| Baseline State | Optimized State |
| --- | --- |
|  |  |

## 5. Azure ML & Clinical Compliance

This pipeline is architected for the Azure ML environment, leveraging native capabilities for secure, reproducible clinical AI:

* **Secure Infrastructure:** Execution within Azure ML Compute using Managed Identities.
* **Model Traceability:** Utilizes **MLFlow** for model versioning.
* **Auditability:** Full integration with Azure Monitor for HIPAA-ready audit trails.

## 6. Getting Started

1. **Prerequisites:** Python 3.10+, `pandas`, `scikit-learn`, `azureml-core`.
2. **Run Pipeline:**
```bash
python run_reliability_pipeline.py --asset_version 1

```


3. **Audit Assets:** Access generated reports in the `images/` directory.

> **SECURITY WARNING:** `manual_review_list.csv` contains sensitive clinical triage data. Handle strictly according to hospital security protocols.

## 7. Project Structure

```text
ICU_Reliability_Framework/
├── data/               # Clinical datasets
├── images/             # Audit reports & visualizations
├── notebooks/          # Exploratory analysis
├── src/                # Modularized production code
├── icu-mortality-predictor/  # MLFlow models
└── run_reliability_pipeline.py # Main execution script

```

## 8. License & Disclaimer

*This tool is for research and clinical support purposes only. It is intended to assist, not replace, medical judgment.*

**MIT License** | Copyright (c) 2026 Salome Scherer.

---

*Developed for ICU Mortality Prediction | Compliance: HIPAA-Ready | Framework: Reliability Engineering*


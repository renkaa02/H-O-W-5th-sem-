# Week 9 & 10 - Model Evaluation & Feature Engineering

### Topics Covered

* **Model Evaluation:** Train/test split, Cross-validation strategies, Confusion matrix analysis, Precision/Recall/F1-score trade-offs, and ROC-AUC curve evaluation.
* **Feature Engineering & Preprocessing:** Data scaling techniques, Feature encoding, Handling missing values (Imputation), and Dataset transformation pipelines.

### Files Added

* `app_week9_10.py` : Flask API backend exposing Model Evaluation and Feature Engineering metrics endpoints.
* **Colab Notebook:**
* [View Code in Google Colab](https://colab.research.google.com/drive/1kCr9MKgQm-EJgd1uZ1oBJS5wydlUAbzA?usp=sharing)

### API Routes

* `GET /api/week9-10/plan` - Returns topic syllabus and details for Week 9 & 10.
* `GET /api/week9-10/eval-demo` - Outputs model evaluation metrics, feature scaling results, and confusion matrix in JSON format.

### System Flow

```text
[ Client / Browser ]
        │
        ▼ (HTTP GET /api/week9-10/eval-demo)
[ Localtunnel Server ]
        │
        ▼ (Port 5000)
[ Flask App (Colab / app_week9_10.py) ]
        │
        ├─► [ Preprocessing Pipeline ] (Missing Data Imputation & Scaling)
        └─► [ Evaluation Metrics Engine ] (Confusion Matrix, Precision/Recall, ROC-AUC)
        │
        ▼
[ JSON Output Response ]

### OUTPUT SCREENSHOT:
<img width="959" height="140" alt="Screenshot 2026-09-02 192838" src="https://github.com/user-attachments/assets/e027ac4f-0cd6-40e0-8701-210025a1b621" />

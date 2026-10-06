# Week 13 & 14 - Ensemble Methods & Model Optimization

### Topics Covered

* **Ensemble Methods:** Bagging (Random Forest) and Boosting algorithms (XGBoost, LightGBM).
* **Model Diagnostics:** Bias-Variance Tradeoff analysis, Overfitting vs. Underfitting detection and prevention.
* **Regularization Techniques:** L1 (Lasso) and L2 (Ridge) penalties to control model complexity and improve generalization.

### Files Added

* `app_week13_14.py` : Flask API backend exposing Ensemble learning and Regularization metrics endpoints.
* **Colab Notebook:**
* [View Code in Google Colab](https://colab.research.google.com/drive/1phQ7wnyNKIK9HH-ng4_2G_0eHtaml-kb?usp=sharing)

### API Routes

* `GET /api/week13-14/plan` - Returns topic syllabus and details for Week 13 & 14.
* `GET /api/week13-14/ensemble-demo` - Outputs execution metrics for Bagging, Boosting (XGBoost, LightGBM), and Regularized models in JSON format.

### System Flow

```text
[ Client / Browser ]
        │
        ▼ (HTTP GET /api/week13-14/ensemble-demo)
[ Localtunnel Server ]
        │
        ▼ (Port 5000)
[ Flask App (Colab / app_week13_14.py) ]
        │
        ├─► [ Ensemble Engine ] (RandomForest, XGBoost, LightGBM)
        └─► [ Regularization Engine ] (L1 / L2 Penalty Evaluation)
        │
        ▼
[ JSON Output Response ]
```

###OUTPUT SCREENSHOT

<img width="958" height="163" alt="Screenshot 2026-10-06 183748" src="https://github.com/user-attachments/assets/69d69318-8c8b-4e6c-b979-951af4f17855" />


# Week 7 & 8 - Machine Learning (Regression & Classification)

### Topics Covered
* **Regression:** Linear, Polynomial (Degree 2), Ridge, and Lasso Regression using Scikit-Learn.
* **Classification:** Logistic Regression and K-Nearest Neighbors (KNN) algorithms.
* **ML Pipelines:** Feature scaling, polynomial transformation, and automated model predictions.
* **Flask Integration:** Exposing trained ML model outputs via RESTful API routes.

### Files Added
* `app_week7_8.py`: Flask application serving Week 7 & 8 machine learning model predictions.

### API Routes
* `GET /api/week7-8/plan` - Returns syllabus and ML task details in JSON format.
* `GET /api/week7-8/ml-demo` - Runs regression and classification models, returning prediction metrics in JSON.

### Output Verification
Screenshot of `/api/week7-8/ml-demo` response running via Localtunnel:

![API Response Screenshot](<img width="959" height="165" alt="Screenshot 2026-09-02 184118" src="https://github.com/user-attachments/assets/d972b655-acdb-4ab8-a7c9-bd3c59b258b3" />
)

### System Flow
```text
[ Client / Browser ] 
        │
        ▼ (HTTP GET /api/week7-8/ml-demo)
[ Localtunnel Server ]
        │
        ▼ (Port 5000)
[ Flask App (app_week7_8.py) ]
        │
        ├─► [ MachineLearningDemo Class ]
        │     ├─► Regression Models (Linear, Poly, Ridge, Lasso)
        │     └─► Classification Models (Logistic, KNN)
        │
        ▼
[ JSON Output Response ]


### Google Colab Notebook
Colab Link: [Open in Colab](https://colab.research.google.com/drive/1r36TGChC90fEhnkG3CxDe6ex_rLcHzwW?usp=sharing)

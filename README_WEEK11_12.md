# Week 11 & 12 - Dimensionality Reduction (PCA & t-SNE)

### Topics Covered

* **Dimensionality Reduction (PCA):** Principal Component Analysis intuition, Eigen-decomposition, Covariance matrix calculation, Variance maximization, and Multicollinearity elimination.
* **Dimensionality Reduction (t-SNE):** t-Distributed Stochastic Neighbor Embedding intuition, Non-linear manifold visualization, High-D vs. Low-D probability distributions, Crowding problem mitigation using Student-t distribution, and Perplexity hyperparameter tuning.

### Files Added

* `app_week11_12.py` : Flask API backend exposing Dimensionality Reduction syllabus and execution metrics endpoints.
* **Colab Notebook:**
* [View Code in Google Colab] https://colab.research.google.com/drive/1-QowrmTUCDWWyXdRaWDAuDHy2WPTRAfv?usp=sharing

### API Routes

* `GET /api/week11-12/plan` - Returns topic syllabus and details for Week 11 & 12.
* `GET /api/week11-12/dim-reduction-demo` - Outputs PCA explained variance, reconstruction metrics, and t-SNE 2D coordinate projections in JSON format.

### System Flow

```text
[ Client / Browser ]
        │
        ▼ (HTTP GET /api/week11-12/dim-reduction-demo)
[ Localtunnel Server ]
        │
        ▼ (Port 5000)
[ Flask App (Colab / app_week11_12.py) ]
        │
        ├─► [ Data Preprocessing Pipeline ] (StandardScaler High-D Dataset)
        ├─► [ Linear Projection Pipeline ]  (PCA Matrix Eigen-Decomposition)
        └─► [ Non-Linear Embedding Pipeline ] (t-SNE Probabilistic Mapping & KL Divergence)
        │
        ▼
[ JSON Output Response ]


### OUTPUT screenshot
<img width="958" height="145" alt="Screenshot 2026-09-29 235715" src="https://github.com/user-attachments/assets/2da4fa67-f3f0-4eb4-b4fa-15de24e28f56" />




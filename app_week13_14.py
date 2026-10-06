from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import xgboost as xgb
import lightgbm as lgb

app = Flask(__name__)

class EnsembleAndRegularizationDemo:
    def __init__(self):
        # Generate synthetic classification dataset
        X, y = make_classification(
            n_samples=500, n_features=15, n_informative=10, 
            n_redundant=5, random_state=42
        )
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

    def run_pipeline(self):
        # 1. Bagging (Random Forest)
        rf = RandomForestClassifier(n_estimators=50, random_state=42)
        rf.fit(self.X_train, self.y_train)
        rf_pred = rf.predict(self.X_test)

        # 2. Boosting (XGBoost)
        xgb_model = xgb.XGBClassifier(n_estimators=50, eval_metric='logloss', random_state=42)
        xgb_model.fit(self.X_train, self.y_train)
        xgb_pred = xgb_model.predict(self.X_test)

        # 3. Boosting (LightGBM)
        lgb_model = lgb.LGBMClassifier(n_estimators=50, verbose=-1, random_state=42)
        lgb_model.fit(self.X_train, self.y_train)
        lgb_pred = lgb_model.predict(self.X_test)

        # 4. Regularization (L1 & L2 Logistic Regression)
        l1_model = LogisticRegression(penalty='l1', solver='liblinear', C=0.5, random_state=42)
        l1_model.fit(self.X_train, self.y_train)
        l1_pred = l1_model.predict(self.X_test)

        l2_model = LogisticRegression(penalty='l2', C=0.5, random_state=42)
        l2_model.fit(self.X_train, self.y_train)
        l2_pred = l2_model.predict(self.X_test)

        return {
            "ensemble_models": {
                "random_forest_bagging": {
                    "accuracy": round(float(accuracy_score(self.y_test, rf_pred)), 4),
                    "f1_score": round(float(f1_score(self.y_test, rf_pred)), 4)
                },
                "xgboost_boosting": {
                    "accuracy": round(float(accuracy_score(self.y_test, xgb_pred)), 4),
                    "f1_score": round(float(f1_score(self.y_test, xgb_pred)), 4)
                },
                "lightgbm_boosting": {
                    "accuracy": round(float(accuracy_score(self.y_test, lgb_pred)), 4),
                    "f1_score": round(float(f1_score(self.y_test, lgb_pred)), 4)
                }
            },
            "regularization_and_diagnostics": {
                "l1_lasso_accuracy": round(float(accuracy_score(self.y_test, l1_pred)), 4),
                "l2_ridge_accuracy": round(float(accuracy_score(self.y_test, l2_pred)), 4),
                "bias_variance_notes": "Ensemble methods reduce variance; Regularization controls overfitting by penalizing high weights."
            }
        }

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "status": "success",
        "message": "Flask ML API Active",
        "available_endpoints": [
            "/api/week13-14/plan",
            "/api/week13-14/ensemble-demo"
        ]
    })

@app.route('/api/week13-14/plan', methods=['GET'])
def get_plan():
    return jsonify({
        "week": "13 & 14",
        "title": "Ensemble Methods & Model Optimization",
        "topics": [
            "Bagging (Random Forest)",
            "Boosting (XGBoost, LightGBM)",
            "Bias-Variance Tradeoff & Overfitting/Underfitting",
            "Regularization (L1/L2 Penalties)"
        ],
        "status": "success"
    })

@app.route('/api/week13-14/ensemble-demo', methods=['GET'])
def run_demo():
    demo = EnsembleAndRegularizationDemo()
    results = demo.run_pipeline()
    return jsonify({
        "status": "success",
        "results": results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

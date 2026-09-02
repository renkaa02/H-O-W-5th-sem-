!pip install flask scikit-learn numpy pandas -q
!npm install -g localtunnel -q

%%writefile app_week9_10.py
from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

app = Flask(__name__)

class ModelEvaluationDemo:
    def __init__(self):
        np.random.seed(42)
        X_raw = np.random.randn(100, 4)
        X_raw[5, 0] = np.nan
        X_raw[12, 2] = np.nan
        y_raw = np.random.choice([0, 1], size=100)

        imputer = SimpleImputer(strategy='mean')
        X_imputed = imputer.fit_transform(X_raw)

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_imputed)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_scaled, y_raw, test_size=0.3, random_state=42
        )

        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        y_prob = self.model.predict_proba(self.X_test)[:, 1]

        cm = confusion_matrix(self.y_test, y_pred).tolist()
        precision = float(precision_score(self.y_test, y_pred, zero_division=0))
        recall = float(recall_score(self.y_test, y_pred, zero_division=0))
        f1 = float(f1_score(self.y_test, y_pred, zero_division=0))
        roc_auc = float(roc_auc_score(self.y_test, y_prob))

        cv_scores = cross_val_score(self.model, self.X_train, self.y_train, cv=5).tolist()

        return {
            "feature_engineering": {
                "missing_values_imputed": True,
                "scaling_applied": "StandardScaler"
            },
            "model_evaluation": {
                "confusion_matrix": cm,
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1_score": round(f1, 4),
                "roc_auc_score": round(roc_auc, 4),
                "5_fold_cv_scores": [round(score, 4) for score in cv_scores],
                "mean_cv_accuracy": round(float(np.mean(cv_scores)), 4)
            }
        }

@app.route('/api/week9-10/plan', methods=['GET'])
def get_plan():
    return jsonify({
        "week": "9 & 10",
        "title": "Model Evaluation & Feature Engineering",
        "topics": [
            "Train/Test Split & Cross-Validation",
            "Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC",
            "Feature Engineering & Scaling (StandardScaler)",
            "Handling Missing Data (SimpleImputer)"
        ],
        "status": "success"
    })

@app.route('/api/week9-10/eval-demo', methods=['GET'])
def run_eval_demo():
    demo = ModelEvaluationDemo()
    results = demo.evaluate()
    return jsonify({
        "status": "success",
        "results": results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import subprocess
import time

print("=== YOUR LOCALTUNNEL PASSWORD ===")
!curl ipv4.icanhazip.com

subprocess.Popen(["python", "app_week9_10.py"])
time.sleep(3)

print("\n=== YOUR PUBLIC URL ===")
!npx localtunnel --port 5000


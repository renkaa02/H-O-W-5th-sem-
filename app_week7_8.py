!pip install flask scikit-learn -q

import threading
from flask import Flask, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)
print("Flask, NumPy, and Scikit-Learn imported successfully!")

class MachineLearningDemo:
    @staticmethod
    def regression_models():
        # Sample Data: X (Experience), y (Salary)
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([45000, 50000, 60000, 80000, 110000])

        # 1. Linear Regression
        lr = LinearRegression().fit(X, y)
        pred_lr = float(lr.predict([[6]])[0])

        # 2. Polynomial Regression (Degree 2)
        poly = PolynomialFeatures(degree=2)
        X_poly = poly.fit_transform(X)
        poly_reg = LinearRegression().fit(X_poly, y)
        pred_poly = float(poly_reg.predict(poly.transform([[6]]))[0])

        # 3. Ridge & Lasso
        ridge = Ridge(alpha=1.0).fit(X, y)
        lasso = Lasso(alpha=1.0).fit(X, y)

        return {
            "linear_regression_pred_x6": round(pred_lr, 2),
            "polynomial_regression_pred_x6": round(pred_poly, 2),
            "ridge_coef": float(ridge.coef_[0]),
            "lasso_coef": float(lasso.coef_[0])
        }

    @staticmethod
    def classification_models():
        # Sample Data: X [Hours Studied, Attendance %], y (0: Fail, 1: Pass)
        X = np.array([[1, 50], [2, 60], [3, 65], [6, 80], [7, 90], [8, 95]])
        y = np.array([0, 0, 0, 1, 1, 1])

        test_student = [[5, 75]]

        # 1. Logistic Regression
        log_reg = LogisticRegression().fit(X, y)
        pred_log = int(log_reg.predict(test_student)[0])

        # 2. K-Nearest Neighbors (KNN)
        knn = KNeighborsClassifier(n_neighbors=3).fit(X, y)
        pred_knn = int(knn.predict(test_student)[0])

        return {
            "test_input": {"hours": 5, "attendance": 75},
            "logistic_regression_pred": "Pass (1)" if pred_log == 1 else "Fail (0)",
            "knn_pred": "Pass (1)" if pred_knn == 1 else "Fail (0)"
        }

  @app.route('/api/week7-8/plan', methods=['GET'])
def get_plan():
    return jsonify({
        "status": "success",
        "week": "7 & 8",
        "title": "Machine Learning: Regression & Classification",
        "topics": [
            "Regression (Linear, Polynomial, Ridge, Lasso)",
            "Classification (Logistic Regression, KNN)"
        ]
    })

@app.route('/api/week7-8/ml-demo', methods=['GET'])
def get_ml_demo():
    reg_data = MachineLearningDemo.regression_models()
    clf_data = MachineLearningDemo.classification_models()
    
    return jsonify({
        "status": "success",
        "regression_results": reg_data,
        "classification_results": clf_data
    })

def run_app():
    app.run(port=5000)

threading.Thread(target=run_app).start()

print("\n👉 LOCALTUNNEL PASSWORD (IP):")
!curl https://loca.lt/mytunnelpassword
print("\n")

!npx localtunnel --port 5000

import os
import threading
from flask import Flask, jsonify, request
import numpy as np
import pandas as pd

app = Flask(__name__)

# --- WEEK 3 & 4 DATASET & LOGIC (OOP / Pandas / NumPy) ---
class AnalyticsManager:
    def __init__(self):
        self.data = pd.DataFrame([
            {"id": 1, "week": "W3-W4", "topic": "Python Essentials", "activity": "OOP & Comprehensions", "score": 85},
            {"id": 2, "week": "W3-W4", "topic": "NumPy Basics", "activity": "Vectorized Operations", "score": 92},
            {"id": 3, "week": "W3-W4", "topic": "Pandas DataFrames", "activity": "Data Cleaning & GroupBy", "score": 88},
            {"id": 4, "week": "W3-W4", "topic": "Data Visualization", "activity": "Seaborn & Matplotlib Plots", "score": 95}
        ])

    def get_summary(self):
        scores = self.data["score"].to_numpy()
        curved_scores = [score + 2 for score in scores]
        mean_score = np.mean(curved_scores)
        return {
            "total_topics": len(self.data),
            "average_score": round(float(mean_score), 2),
            "topics_list": [row["topic"] for _, row in self.data.iterrows()]
        }

analytics_manager = AnalyticsManager()

# --- WEEK 3 & 4 ENDPOINTS ---
@app.route('/api/week3-4/plan', methods=['GET'])
def get_week3_4_plan():
    records = analytics_manager.data.to_dict(orient='records')
    return jsonify({
        "status": "success",
        "title": "Data Science & Analytics Toolkit API",
        "data": records
    }), 200

@app.route('/api/week3-4/analytics', methods=['GET'])
def get_analytics():
    summary = analytics_manager.get_summary()
    return jsonify({"status": "success", "analytics": summary}), 200

if __name__ == "__main__":
    app.run(port=5000)

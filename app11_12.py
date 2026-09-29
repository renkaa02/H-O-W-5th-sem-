# 1. Install required packages
!pip install flask scikit-learn numpy pandas -q
!npm install -g localtunnel -q

# 2. Write app_week11_12.py
app_code = """from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

app = Flask(__name__)

class DimensionalityReductionDemo:
    def __init__(self):
        np.random.seed(42)
        # Synthetic high-dimensional dataset (100 samples, 10 features, 3 clusters)
        self.X_raw, self.y = make_blobs(
            n_samples=100, 
            n_features=10, 
            centers=3, 
            random_state=42
        )
        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(self.X_raw)

    def evaluate(self):
        # 1. PCA Reduction
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(self.X_scaled)
        explained_variance = pca.explained_variance_ratio_.tolist()

        # 2. t-SNE Reduction
        tsne = TSNE(
            n_components=2, 
            perplexity=30, 
            random_state=42, 
            init='pca', 
            learning_rate='auto'
        )
        X_tsne = tsne.fit_transform(self.X_scaled)

        return {
            "dataset_info": {
                "original_samples": 100,
                "original_features": 10,
                "scaling": "StandardScaler"
            },
            "pca_results": {
                "reduced_dimensions": 2,
                "explained_variance_ratio": [round(v, 4) for v in explained_variance],
                "total_explained_variance": round(float(np.sum(explained_variance)), 4),
                "sample_coordinates_head": [[round(c, 4) for c in point] for point in X_pca[:3].tolist()]
            },
            "tsne_results": {
                "reduced_dimensions": 2,
                "perplexity": 30,
                "kl_divergence": round(float(tsne.kl_divergence_), 4),
                "sample_coordinates_head": [[round(c, 4) for c in point] for point in X_tsne[:3].tolist()]
            }
        }

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": "Dimensionality Reduction API running!",
        "endpoints": ["/api/week11-12/plan", "/api/week11-12/dim-reduction-demo"]
    })

@app.route('/api/week11-12/plan', methods=['GET'])
def get_plan():
    return jsonify({
        "week": "11 & 12",
        "title": "Dimensionality Reduction: PCA & t-SNE",
        "topics": [
            "Linear Subspace Projection & Variance Maximization (PCA)",
            "Covariance Matrix & Eigen-Decomposition",
            "Non-Linear Manifold Learning & Probabilistic Similarity (t-SNE)",
            "Handling the Crowding Problem via Heavy-Tailed Distributions",
            "Hyperparameter Tuning: Perplexity vs. Cluster Resolution"
        ],
        "status": "success"
    })

@app.route('/api/week11-12/dim-reduction-demo', methods=['GET'])
def run_dim_reduction_demo():
    demo = DimensionalityReductionDemo()
    results = demo.evaluate()
    return jsonify({
        "status": "success",
        "results": results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
"""

with open("app_week11_12.py", "w") as f:
    f.write(app_code)

# 3. Kill old background tasks & start Flask safely
import subprocess
import socket
import time

!pkill -f app_week11_12.py

# Launch Flask app process
flask_process = subprocess.Popen(["python", "app_week11_12.py"])

# Verify Flask is accepting connections on port 5000
def wait_for_port(port, host='127.0.0.1', timeout=15):
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except (SocketError := OSError):
            if time.time() - start_time > timeout:
                return False
            time.sleep(0.5)

print("Starting Flask server...")
if wait_for_port(5000):
    print("✓ Flask server is live on port 5000!")
else:
    print("× Flask server failed to start.")

# 4. Output password IP and trigger Localtunnel
print("\n=== YOUR LOCALTUNNEL PASSWORD ===")
!curl -s ipv4.icanhazip.com

print("\n=== YOUR PUBLIC URL ===")
!npx localtunnel --port 5000

from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

# --- Linear Algebra & Calculus Helper Class ---
class MathForML:
    @staticmethod
    def linear_algebra_demo():
        # Vectors & Dot Product
        v1 = np.array([2, 3])
        v2 = np.array([4, 1])
        dot_prod = int(np.dot(v1, v2))
        
        # Matrix & Eigenvalues
        matrix = np.array([[4, 2], [1, 3]])
        eigenvalues, _ = np.linalg.eig(matrix)
        
        return {
            "vectors": {"v1": v1.tolist(), "v2": v2.tolist()},
            "dot_product": dot_prod,
            "matrix": matrix.tolist(),
            "eigenvalues": np.round(eigenvalues, 2).tolist()
        }

    @staticmethod
    def calculus_demo(x_val=4.0):
        # Function: f(x) = x^2 + 3x + 5 -> Gradient: f'(x) = 2x + 3
        df_dx = 2 * x_val + 3
        
        # Chain Rule Backprop Intuition: d/dx[3*(x^2)] = 3 * (2x) = 6x
        chain_rule_grad = 6 * x_val
        
        return {
            "function": "f(x) = x^2 + 3x + 5",
            "eval_at_x": x_val,
            "gradient_df_dx": df_dx,
            "chain_rule_backprop_intuition": f"d/dx[3*x^2] at x={x_val} is {chain_rule_grad}"
        }

# --- Flask Routes ---
@app.route('/api/week5-6/plan', methods=['GET'])
def get_plan():
    return jsonify({
        "status": "success",
        "week": "5 & 6",
        "title": "Mathematics for Machine Learning",
        "topics": [
            "Linear Algebra (Vectors, Matrices, Dot Product, Eigenvalues)",
            "Calculus (Derivatives, Gradients, Chain Rule)"
        ]
    })

@app.route('/api/week5-6/math-demo', methods=['GET'])
def get_math_demo():
    la_data = MathForML.linear_algebra_demo()
    calc_data = MathForML.calculus_demo(x_val=4.0)
    
    return jsonify({
        "status": "success",
        "linear_algebra": la_data,
        "calculus_gradient": calc_data
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)

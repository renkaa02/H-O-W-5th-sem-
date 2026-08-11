# Week 5 & 6 - Mathematics for Machine Learning #

### Topics Covered
* **Linear Algebra:** Vector operations, Matrix transformations, Dot product, and Eigenvalues computation using NumPy.
* **Calculus & Gradients:** Analytical derivatives, Gradient calculation, and Chain Rule intuition for neural network backpropagation.

### Files Added
* `app_week5_6.py`: Flask API backend exposing Linear Algebra and Calculus demo endpoints.
* **Colab Notebook:**
* [View Code in Google Colab](https://colab.research.google.com/drive/1Yo65GFpVA7IkdNLiYz39o_EeOyQk40SQ?usp=sharing)

### API Routes
* `GET /api/week5-6/plan` - Returns topic syllabus and details for Week 5 & 6.
* `GET /api/week5-6/math-demo` - Outputs computed Linear Algebra metrics and Gradient calculations in JSON format.

### System Flow
```
[ Client / Browser ] 
        │
        ▼ (HTTP GET /api/week5-6/math-demo)
[ Localtunnel Server ]
        │
        ▼ (Port 5000)
[ Flask App (Colab / app_week5_6.py) ]
        │
        ├─► [ MathForML Class ]
        │     ├─► Linear Algebra (Dot Product, Eigenvalues)
        │     └─► Calculus (Gradients, Chain Rule)
        │
        ▼
[ JSON Output Response ]

```
OUTPUT SCREENSHORT:
<img width="1919" height="335" alt="Screenshot 2026-08-11 223618" src="https://github.com/user-attachments/assets/548e659c-caf0-499a-8db0-a88e33bb85a0" />


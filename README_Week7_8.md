# Supervised Machine Learning API (Week 7 & 8)

## Project Overview
This repository contains the **Week 7 & 8 Hack-O-Week** project implementation. It demonstrates core Supervised Machine Learning concepts (Regression & Classification) integrated with a Flask REST API backend.

---

## Topics & Core Features Covered

- **Regression Models:** Linear, Polynomial (Degree 2), Ridge, and Lasso Regression using Scikit-Learn.
- **Classification Models:** Logistic Regression and K-Nearest Neighbors (KNN) algorithms.
- **Data Preprocessing:** Feature scaling, polynomial feature transformation, and dataset matrix handling via NumPy.
- **Flask REST API:** OOP-encapsulated model execution with JSON response serialization.

---

## Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/week7-8/plan` | Returns the complete Week 7 & 8 syllabus dataset in JSON |
| `GET` | `/api/week7-8/ml-demo` | Executes regression and classification pipelines and returns predictions in JSON |

---

## Live API Execution & Verification

### Localtunnel Public Endpoint Test
The API was executed live in Google Colab and exposed via Localtunnel (`/api/week7-8/ml-demo`): 

<img width="959" height="165" alt="Screenshot 2026-09-02 184118" src="https://github.com/user-attachments/assets/93c63ded-a5e6-4a82-a5f9-0df1f877adbd" />


---

## System Architecture

```text
+-----------------------+      1. HTTP GET Request           +------------------------+
|                       |  --------------------------------> |                        |
|   Client / Browser    |                                    |   Flask ML API Server  |
|      / Postman        |  <-------------------------------- |   (Scikit-Learn/NumPy) |
|                       |        2. JSON Data Response       |                        |
+-----------------------+                                    +------------------------+


## 🔗 Google Colab Notebook

`Notebook Link` ➔ [Open in Google Colab](https://colab.research.google.com/drive/1r36TGChC90fEhnkG3CxDe6ex_rLcHzwW?usp=sharing)


## Week 3 & 4 - Data Science & Analytics Implementation

### Topics Covered
* Python Essentials: OOP class structure, list and dict comprehensions.
* NumPy: Array manipulation and vectorized ops.
* Pandas: DataFrames, data cleaning, and JSON output.
* Visualization: Matplotlib and Seaborn integration setup.

### Files Added
* `app_week3_4.py`: Flask application for Week 3 and 4 API endpoints.

### API Routes
* `GET /api/week3-4/plan` - Returns syllabus and task details in JSON.
* `GET /api/week3-4/analytics` - Calculates dataset summary using NumPy and Pandas.

### Output Verification
Screenshot of `/api/week3-4/plan` response running via Localtunnel:
<img width="1919" height="322" alt="Screenshot 2026-08-11 220447" src="https://github.com/user-attachments/assets/b5341f11-1a16-4d39-88a6-0ba7401425d3" />

### System Flow
```text
[ Client / Browser ] 
        │
        ▼ (HTTP GET /api/week3-4/plan)
[ Localtunnel Server ]
        │
        ▼ (Port 5000)
[ Flask App (app_week3_4.py) ]
        │
        ├─► [ AnalyticsManager (OOP Class) ]
        └─► [ Pandas Data Frame & NumPy Ops ]
        │
        ▼
[ JSON Output Response ]
```

### Google Colab Notebook
* Colab Link: [Open in Colab](https://colab.research.google.com/drive/1ol5Y8FYDPGa_FsCPG9IHTfIKz6EGnYQW?usp=sharing)
  






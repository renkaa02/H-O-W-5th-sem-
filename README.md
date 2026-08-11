## Weekly Work Plan REST API ##

A lightweight RESTful API built using **Python** and **Flask** to manage weekly academic work plans. Exposed publicly via **Google Colab** and **Localtunnel**.

---

## 🛠️ Features
- **`GET /api/plan`**: Retrieves the list of weekly activities and topics in JSON format.
- **`POST /api/plan`**: Adds new weekly schedules to the server dynamically.
- **JSON Format**: Clean and structured JSON responses with standard HTTP status codes (`200 OK`, `201 Created`).

---

## 📁 Repository Structure
```text
H-O-W-5th-sem/
├── app.py          # Main Flask API source code
└── README.md       # Project documentation & API output screenshots
```
🌐 Live API Execution & Verification

+ Localtunnel Public Endpoint Test
The API was tested in the browser via Localtunnel ([https://neat-ears-love.loca.lt/api/plan](https://neat-ears-love.loca.lt/api/plan)).

<img width="1918" height="541" alt="Screenshot 2026-08-11 212658" src="https://github.com/user-attachments/assets/f690d83b-2ff4-44af-9e91-4f55b18eabaa" />



## 💻 How to Run in Google Colab

1. **Install Dependencies & Localtunnel:**
   ```
   !pip install flask
   !npm install -g localtunnel


Run Flask Application in Background Thread:

Python
import threading
from flask import Flask, jsonify

app = Flask(__name__)

def run_app():
    app.run(port=5000)

threading.Thread(target=run_app).start()

Expose Server via Localtunnel:

Bash
!npx localtunnel --port 5000


🔗 **Google Colab Notebook:** 
[Click Here to Run on Colab](https://colab.research.google.com/drive/1cCCBLp0bX7Qfcji8NTQJI6E13X8wo875?usp=sharing)


## 📐 System Architecture

```text
+-----------------------+     1. HTTP GET / POST Request     +------------------------+
|                       |  --------------------------------> |                        |
|   Client / Browser    |                                    |     Flask REST API     |
|      / Postman        |  <-------------------------------- |        (Server)        |
|                       |        2. JSON Data Response       |                        |
+-----------------------+                                    +------------------------+

```

   

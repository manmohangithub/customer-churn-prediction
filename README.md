# 🚀 Customer Churn Prediction System (Full-Stack ML Project)

A production-ready **Customer Churn Prediction System** built using **Machine Learning + FastAPI + React**.
This project predicts whether a customer is likely to churn based on behavioral and service usage data.

---

## 📌 Overview

Customer churn is a critical problem in telecom and subscription businesses.
This project uses a **Random Forest Classifier** to predict churn and provides a **real-time dashboard** for interaction.

---

## 🧠 Key Features

* 🔍 Predict customer churn in real-time
* 📊 Display churn probability score
* 📈 Feature importance visualization
* ⚡ FastAPI backend for high-performance inference
* 🎨 React frontend dashboard
* 🧠 Machine Learning model (Random Forest)

---

## 🏗️ Tech Stack

### Backend

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy

### Frontend

* React.js
* Axios
* Vite

### ML Model

* RandomForestClassifier
* Feature Engineering & Encoding

---

## 📂 Project Structure

```
customer-churn-prediction/

├── backend/
│   ├── main.py
│   ├── train.py
│   ├── model.pkl
│   ├── encoders.pkl
│   ├── features.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. User enters customer details in the dashboard
2. Frontend sends request to FastAPI backend
3. Backend processes input using trained ML model
4. Prediction + probability returned to UI

---

## 🧪 Sample Inputs

### 🔴 High Churn Risk

* TenureMonths: 1
* MonthlyCharges: 95
* Contract: Month-to-month
* OnlineSecurity: No
* TechSupport: No

👉 Output: **Churn = 1 (High Probability)**

---

### 🟢 Low Churn Risk

* TenureMonths: 60
* MonthlyCharges: 50
* Contract: Two year
* OnlineSecurity: Yes
* TechSupport: Yes

👉 Output: **Churn = 0 (Low Probability)**

---

## 📊 Model Performance

* Accuracy: **~80%**
* Algorithm: Random Forest
* Features Used:

  * TenureMonths
  * MonthlyCharges
  * TotalCharges
  * Contract
  * InternetService
  * PaymentMethod
  * OnlineSecurity
  * TechSupport

---

## 🚀 Setup Instructions

### 🔹 Backend

```bash
cd backend
pip install -r requirements.txt
python train.py
python -m uvicorn main:app --reload
```

---

### 🔹 Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🧠 Key Learnings

* Handling real-world dataset inconsistencies
* Feature engineering & preprocessing
* Model deployment with FastAPI
* Full-stack integration (React + ML)
* Debugging API schema mismatches



---

## 👨‍💻 Author

**Medapati Manmohan Reddy**
📍 Hyderabad, India
🔗 GitHub: https://github.com/manmohangithub
🔗 LinkedIn: https://www.linkedin.com/in/manmohanreddy1111

---

## ⭐ If you like this project, give it a star!

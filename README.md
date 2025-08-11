# 🚴 Ola Bike Ride Demand Forecasting Using Machine Learning

**Welcome to the repository of my mini-project!**
This project predicts Ola bike ride demand patterns across Bangalore, using machine learning to enhance urban mobility for riders and Ola.

---

## 📌 Project Overview

Predicting ride demand can:

* Improve ride availability
* Reduce wait times
* Optimize driver allocation

We use historical data (2022–2024) + real-time inputs like weather and calendar data to make accurate predictions.

---

## ✨ Key Features

### **Smart Predictions**

* Forecast ride demand using time, place, weather, day status, and temperature.
* Dynamic integration of real-world data sources.

### **Powerful ML Model**

* **LightGBM Regressor** for high accuracy and speed with large datasets.
* Hyperparameter tuning + evaluation via **R²**, **RMSE**, **MAE**.

### **Dynamic APIs**

* **Google Calendar API**: Detects holiday or working day.
* **OpenWeather API**: Fetches real-time temperature for given date, time, and location.

### **Interactive Web Application**

* Flask backend with HTML/CSS frontend (Ola-inspired theme).
* Users enter date, time, location — system fetches API data & predicts instantly.

### **Scalable & Ready for Deployment**

* Model saved using **Joblib** and **Pickle**.
* Modular design for integration into larger systems.

---

## 🛠 Technology Stack

**Languages & Libraries**

* Python, Pandas, NumPy, Scikit-learn, LightGBM, Matplotlib, Seaborn.

**Workflow**

* Data cleaning & preprocessing (missing values handled)
* Encoding & scaling
* Model training & evaluation

**APIs**

* Google Calendar API
* OpenWeather API

**Web**

* Flask backend
* HTML/CSS frontend

---

## 📊 Impact

**For Riders**

* Plan smarter trips during peak/off-peak hours.
* Better ride availability, reduced waiting.

**For Ola**

* Smarter driver allocation.
* Increased customer satisfaction.

---

## 👥 Team

**Contributors:**
Manjunath S, Likith Reddy, Justin Sebastian Thomas, Marilinga.

---

## 📂 Repository Contents

* **Dataset** – Preprocessed ride demand data
* **Model** – Trained LightGBM model (`.pkl`)
* **Scripts** – Data processing, model training, Flask backend
* **Web App** – Flask-based interface for predictions

---

## 📁 Directory Structure

*(Add screenshot or tree view here)*

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Code10x-letscodewithManju/OlaBikeRideDemandForecastingUsingML.git
cd OlaBikeRideDemandForecastingUsingML
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

Access in browser at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 💡 Future Enhancements

* Integrate real-time ride booking data from Ola API.
* Add traffic congestion analysis.
* Expand to multiple cities.

---

## 📜 License

MIT License

---

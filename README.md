# PM2.5 and AQI Prediction Web App

This is a simple Flask application that predicts **PM2.5 concentration** and calculates the **Air Quality Index (AQI)** based on user-input weather data.

---

## 🎯 Project Aim

To build a web app that takes basic weather conditions as input and predicts:
- **PM2.5 value** (Particulate Matter)
- **Air Quality Index (AQI)**
- **Air Quality Category** (e.g., Good, Moderate, Poor)

---

## 🔢 Inputs

The user must enter the following weather data:
- **T** – Average Temperature (°C)
- **TM** – Max Temperature (°C)
- **Tm** – Min Temperature (°C)
- **SLP** – Sea Level Pressure (hPa)
- **H** – Relative Humidity (%)
- **VV** – Visibility (km)
- **V** – Average Wind Speed (km/h)
- **VM** – Max Wind Speed (km/h)

---

## 📤 Outputs

After prediction, the app displays:
- **Predicted PM2.5 value**
- **AQI score** (0–500 scale)
- **Air Quality Category** (e.g., Good, Satisfactory, Moderate, Poor, etc.)

---

## 📂 Project Files

- `app.py` — Flask app backend
- `requirements.txt` — Required libraries
- `random_forest_regression_model.pkl` — Trained ML model
- `templates/` — HTML pages for UI

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the server:

```bash
python app.py
```

3. Open the web app in your browser:

```
http://127.0.0.1:5000/
```

---

## 📈 Tech Used

- **Python**
- **Flask**
- **HTML/CSS (Bootstrap)**
- **Scikit-learn** (Machine Learning model)

---

# 🌟 Thank You!

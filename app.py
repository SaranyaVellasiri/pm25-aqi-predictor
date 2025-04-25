from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('random_forest_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# AQI breakpoints for PM2.5
AQI_BREAKPOINTS = [
    (0.0, 30.0, 0, 50, "Good"),
    (31.0, 60.0, 51, 100, "Satisfactory"),
    (61.0, 90.0, 101, 200, "Moderate"),
    (91.0, 120.0, 201, 300, "Poor"),
    (121.0, 250.0, 301, 400, "Very Poor"),
    (251.0, 500.0, 401, 500, "Severe")
]

def calculate_aqi(pm):
    for bp_low, bp_high, i_low, i_high, category in AQI_BREAKPOINTS:
        if bp_low <= pm <= bp_high:
            aqi = ((i_high - i_low) / (bp_high - bp_low)) * (pm - bp_low) + i_low
            return round(aqi), category
    return None, "Unknown"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[key]) for key in ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM']]
        prediction = model.predict([features])[0]
        aqi_value, category = calculate_aqi(prediction)
        return render_template('result.html', pm25=round(prediction, 2), aqi=aqi_value, category=category)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run()

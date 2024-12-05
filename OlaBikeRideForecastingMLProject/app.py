from flask import Flask, render_template, request, jsonify
import os
import pickle
import requests
import csv
# from dotenv import load_dotenv
from datetime import datetime, timedelta

# # Load environment variables from .env file
# load_dotenv()

# Load the LightGBM model
MODEL_PATH = r"C:\Users\ADMIN\OneDrive\Desktop\OlaBikeRideForecastingMLProject\model\lgb_model.pkl"  # Ensure this is the correct path
with open(MODEL_PATH, 'rb') as file:
    lgb_model = pickle.load(file)

# Google Calendar API key
GOOGLE_CALENDAR_API_KEY = "InsertApiKey"

# OpenWeather API key
OPENWEATHER_API_KEY = "InsertApiKey"

# CSV file path to store predictions
CSV_FILE_PATH = r"C:\Users\ADMIN\OneDrive\Desktop\OlaBikeRideForecastingMLProject\predictions.csv"

# Flask app initialization
app = Flask(__name__)

# List of places and their corresponding encodings
PLACES = {
    "BTM Layout": 0,
    "Banashankari": 1,
    "Bannerghatta": 2,
    "Bellandur": 3,
    "Domlur": 4,
    "HSR Layout": 5,
    "Hebbal": 6,
    "Indiranagar": 7,
    "JP Nagar": 8,
    "Jayanagar": 9,
    "Jeevanbhima Nagar": 10,
    "Koramangala": 11,
    "Mahadevapura": 12,
    "Malleswaram": 13,
    "Marathahalli": 14,
    "R.T. Nagar": 15,
    "Rajajinagar": 16,
    "Rajarajeshwari Nagar": 17,
    "Sadashivanagar": 18,
    "Seshadripuram": 19,
    "Shivajinagar": 20,
    "Ulsoor": 21,
    "Vasanthnagar": 22,
    "Vijaynagar": 23,
    "Whitefield": 24,
    "Yelahanka": 25,
    "Yeshwantpur": 26
}

@app.route("/")
def home():
    """Render the homepage with input fields."""
    return render_template("index.html", places=PLACES, inputs={})

def get_day_status(year, month, day):
    """
    Determine the day status (working day or holiday) using Google Calendar API.
    Returns:
        0 for holiday, 1 for working day.
    """
    date = datetime(year, month, day)
    if date.weekday() == 6:  # Sunday
        return 0  # Holiday
    url = f"https://www.googleapis.com/calendar/v3/calendars/en.indian%23holiday%40group.v.calendar.google.com/events"
    params = {
        "key": GOOGLE_CALENDAR_API_KEY,
        "timeMin": date.isoformat() + "Z",
        "timeMax": (date + timedelta(days=1)).isoformat() + "Z"
    }
    response = requests.get(url, params=params)
    events = response.json().get('items', [])
    return 0 if events else 1  # Holiday if events exist

def get_temperature(year, month, day, city):
    """
    Fetch the temperature for the given date and city using OpenWeather API.
    """
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(weather_url).json()
    if response.get("main"):
        return response["main"]["temp"]
    return 25.0  # Default temperature if API fails

@app.route("/predict", methods=["POST", "GET"])
def predict():
    """Handle the prediction request."""
    # Extract inputs from the form
    year = int(request.form["year"])
    month = int(request.form["month"])
    day = int(request.form["date"])
    place = request.form["place"]
    hour = int(request.form["hour"])

    # Process inputs
    encoded_place = PLACES[place]
    temperature = get_temperature(year, month, day, place)
    day_status = get_day_status(year, month, day)

    # Determine temperature category
    if temperature < 18:
        temperature_category = 0  # Cold
    elif 18 <= temperature < 27:
        temperature_category = 1  # Moderate
    else:
        temperature_category = 2  # Hot

    # Prepare input for the model
    features = [[year, month, day, hour, encoded_place, temperature, day_status, temperature_category]]

    # Predict ride demand
    ride_demand = lgb_model.predict(features)[0]

    # Save the prediction to CSV
    with open(CSV_FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if os.stat(CSV_FILE_PATH).st_size == 0:
            # Write header if the file is empty
            writer.writerow(["Year", "Month", "Day", "Hour", "Place", "Temperature", "Day Status", "Temperature Category", "Ride Demand"])
        writer.writerow([year, month, day, hour, place, temperature, "Holiday" if day_status == 0 else "Working Day", ["Cold", "Moderate", "Hot"][temperature_category], int(round(ride_demand))])

    return render_template(
        "results.html",
        ride_demand=int(round(ride_demand)),
        inputs={
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "place": place,
            "temperature": temperature,
            "day_status": "Holiday" if day_status == 0 else "Working Day",
            "temperature_category": ["Cold", "Moderate", "Hot"][temperature_category]
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
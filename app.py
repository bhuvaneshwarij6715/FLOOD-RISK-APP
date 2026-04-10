from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# ✅ Safe API key handling
API_KEY = os.environ.get("OPENWEATHER_API_KEY")


# -------- RISK MODEL --------
def predict_risk(temp, humidity, rain):
    score = 0

    if rain > 80:
        score += 3
    elif rain > 40:
        score += 2
    elif rain > 10:
        score += 1

    if humidity > 85:
        score += 2
    elif humidity > 60:
        score += 1

    if temp < 20:
        score += 1

    if score >= 5:
        return "High"
    elif score >= 3:
        return "Medium"
    else:
        return "Low"


def safe_route(risk):
    if risk == "High":
        return "Route C (Avoid Low Lands ⚠️)"
    elif risk == "Medium":
        return "Route B (Caution Required 🟠)"
    else:
        return "Route A (Safe Elevated Route 🟢)"


# -------- HOME PAGE --------
@app.route("/")
def home():
    return render_template("index.html")


# -------- WEATHER API --------
@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City is required"})

    if not API_KEY:
        return jsonify({"error": "API key missing (set OPENWEATHER_API_KEY in Render)"})

    # Geo API
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo_data = requests.get(geo_url).json()

    if not geo_data:
        return jsonify({"error": "City not found"})

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # Weather API
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    data = requests.get(weather_url).json()

    temp = data.get("main", {}).get("temp", 0)
    humidity = data.get("main", {}).get("humidity", 0)
    rain = data.get("rain", {}).get("1h", 0)

    risk = predict_risk(temp, humidity, rain)
    route = safe_route(risk)

    return jsonify({
        "city": city,
        "temperature": temp,
        "humidity": humidity,
        "rainfall": rain,
        "risk": risk,
        "route": route,
        "lat": lat,
        "lon": lon
    })


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# -------- ADVANCED RISK MODEL --------
def predict_risk(temp, humidity, rain):
    score = 0

    if rain > 80: score += 3
    elif rain > 40: score += 2
    elif rain > 10: score += 1

    if humidity > 85: score += 2
    elif humidity > 60: score += 1

    if temp < 20: score += 1

    if score >= 5:
        return "High"
    elif score >= 3:
        return "Medium"
    return "Low"


def safe_route(risk):
    if risk == "High":
        return "Route C (Avoid Low Lands ⚠️)"
    elif risk == "Medium":
        return "Route B (Caution Required 🟠)"
    return "Route A (Safe Elevated Route 🟢)"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather():
    city = request.args.get("city")

    geo = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    ).json()

    if not geo:
        return jsonify({"error": "City not found"})

    lat = geo[0]["lat"]
    lon = geo[0]["lon"]

    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    ).json()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    rain = data.get("rain", {}).get("1h", 0)

    risk = predict_risk(temp, humidity, rain)

    return jsonify({
        "city": city,
        "lat": lat,
        "lon": lon,
        "temp": temp,
        "humidity": humidity,
        "rainfall": rain,
        "risk": risk,
        "route": safe_route(risk)
    })


if __name__ == "__main__":
    app.run(debug=True)
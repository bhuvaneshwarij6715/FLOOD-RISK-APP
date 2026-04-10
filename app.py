from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("OPENWEATHER_API")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_weather")
def get_weather():
    city = request.args.get("city")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()

    temp = data.get("main", {}).get("temp", 0)
    humidity = data.get("main", {}).get("humidity", 0)

    rainfall = 0
    if "rain" in data and "1h" in data["rain"]:
        rainfall = data["rain"]["1h"]

    # RISK LOGIC
    if rainfall < 2:
        risk = "Low"
    elif rainfall < 10:
        risk = "Medium"
    else:
        risk = "High"

    # SAFE ROUTE LOGIC (simple demo logic)
    safe_route = "Route A (Elevated Path) - Safe to travel"

    if risk == "High":
        safe_route = "Avoid travel - Flood-prone area detected"
    elif risk == "Medium":
        safe_route = "Use Highway Route - Caution advised"

    return jsonify({
        "temperature": temp,
        "humidity": humidity,
        "rainfall": rainfall,
        "risk": risk,
        "safe_route": safe_route
    })


if __name__ == "__main__":
    app.run(debug=True)
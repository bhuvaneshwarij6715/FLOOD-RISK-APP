from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OPENWEATHER_API = "YOUR_OPENWEATHER_API_KEY"


def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_API}&units=metric"
    res = requests.get(url).json()

    rain = 0
    temp = res["list"][0]["main"]["temp"]
    humidity = res["list"][0]["main"]["humidity"]

    # FIX: rainfall may not exist → handle safely
    if "rain" in res["list"][0]:
        rain = res["list"][0]["rain"].get("3h", 0)

    return temp, humidity, rain


def risk_level(rain):
    if rain > 20:
        return "High Risk", "red"
    elif rain > 5:
        return "Medium Risk", "orange"
    else:
        return "Low Risk", "green"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    data = request.json
    lat = data["lat"]
    lon = data["lon"]

    temp, humidity, rain = get_weather(lat, lon)
    risk, color = risk_level(rain)

    return jsonify({
        "temperature": temp,
        "humidity": humidity,
        "rainfall": rain,
        "risk": risk,
        "color": color
    })


@app.route("/city")
def city():
    name = request.args.get("name")

    geo = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid={OPENWEATHER_API}"
    ).json()

    return jsonify({
        "lat": geo[0]["lat"],
        "lon": geo[0]["lon"]
    })


if __name__ == "__main__":
    app.run(debug=True)
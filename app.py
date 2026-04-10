from flask import Flask, render_template, request, jsonify
import requests
from twilio.rest import Client

app = Flask(__name__)

import os
OPENWEATHER_API = os.environ.get("OPENWEATHER_API")

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
USER_PHONE = os.environ.get("USER_PHONE")

client = Client(TWILIO_SID, TWILIO_AUTH)


def send_sms(message):
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=USER_PHONE
        )
    except Exception as e:
        print("SMS Error:", e)


def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_API}&units=metric"
    data = requests.get(url).json()

    temp = data["list"][0]["main"]["temp"]
    humidity = data["list"][0]["main"]["humidity"]

    rain = 0
    if "rain" in data["list"][0]:
        rain = data["list"][0]["rain"].get("3h", 0)

    return temp, humidity, rain


def risk_level(rain):
    if rain > 20:
        return "HIGH", "red"
    elif rain > 5:
        return "MEDIUM", "orange"
    return "LOW", "green"


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

    # 🔴 SEND SMS ALERT FOR HIGH RISK
    if risk == "HIGH":
        send_sms(f"🚨 FLOOD ALERT!\nRainfall: {rain}mm\nLocation: {lat},{lon}")

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
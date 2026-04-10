# Flood Risk Alert App 🌧️

This app detects flood risk using:
- GPS location
- OpenWeather API
- Google Maps

## Features
- Real-time rainfall, temperature, humidity
- Flood risk prediction
- Live location map

## Setup

1. Add API keys in app.py and index.html
2. Install requirements:
   pip install -r requirements.txt

3. Run:
   python app.py

## Deployment (Render)

- Build Command:
  pip install -r requirements.txt

- Start Command:
  gunicorn app:app
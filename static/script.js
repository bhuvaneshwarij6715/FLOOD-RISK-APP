function checkRisk() {
    let city = document.getElementById("city").value;

    fetch(`/get_weather?city=${city}`)
    .then(res => res.json())
    .then(data => {

        console.log(data);

        document.getElementById("cityName").innerText =
            "📍 City: " + city;

        document.getElementById("temp").innerText =
            "🌡️ Temperature: " + data.temperature + " °C";

        document.getElementById("humidity").innerText =
            "💧 Humidity: " + data.humidity + " %";

        document.getElementById("rainfall").innerText =
            "🌧️ Rainfall: " + data.rainfall + " mm";

        document.getElementById("risk").innerText =
            "⚠️ Risk Level: " + data.risk;

        document.getElementById("route").innerText =
            "🛣️ Safe Route: " + data.safe_route;
    })
    .catch(err => console.log(err));
}
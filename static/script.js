function checkRisk() {
    let city = document.getElementById("city").value;

    fetch(`/get_weather?city=${city}`)
    .then(res => res.json())
    .then(data => {

        console.log(data); // DEBUG (IMPORTANT)

        document.getElementById("temp").innerText =
            "Temperature: " + data.temperature + " °C";

        document.getElementById("humidity").innerText =
            "Humidity: " + data.humidity + " %";

        document.getElementById("rainfall").innerText =
            "Rainfall: " + data.rainfall + " mm";

        document.getElementById("risk").innerText =
            "Risk: " + data.risk;
    })
    .catch(err => console.log(err));
}
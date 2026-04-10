function checkRisk() {
    let city = document.getElementById("city").value;

    fetch(`/weather?city=${city}`)
        .then(res => res.json())
        .then(data => {

            if (data.error) {
                alert(data.error);
                return;
            }

            document.getElementById("temp").innerText = data.temperature + " °C";
            document.getElementById("hum").innerText = data.humidity + " %";
            document.getElementById("rain").innerText = data.rainfall + " mm";
            document.getElementById("risk").innerText = data.risk;
            document.getElementById("route").innerText = data.route;
        })
        .catch(err => console.log(err));
}
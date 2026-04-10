let map;
let marker;

function getCity() {
    let city = document.getElementById("city").value;

    fetch(`/city?name=${city}`)
    .then(res => res.json())
    .then(data => {
        loadWeather(data.lat, data.lon);
    });
}

function loadWeather(lat, lon) {

    fetch("/weather", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ lat, lon })
    })
    .then(res => res.json())
    .then(data => {

        document.getElementById("rainfall").innerText = data.rainfall;
        document.getElementById("risk").innerText = data.risk;

        showMap(lat, lon);
    });
}

function showMap(lat, lon) {

    let location = { lat: lat, lng: lon };

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: location
    });

    marker = new google.maps.Marker({
        position: location,
        map: map
    });
}
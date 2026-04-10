let map;

function check() {
  let city = document.getElementById("city").value;

  fetch(`/weather?city=${city}`)
    .then(res => res.json())
    .then(data => {

      if (data.error) {
        alert("City not found");
        return;
      }

      document.getElementById("cityName").innerText = city;
      document.getElementById("temp").innerText = data.temp + " °C";
      document.getElementById("humidity").innerText = data.humidity + " %";
      document.getElementById("rain").innerText = data.rainfall + " mm";
      document.getElementById("risk").innerText = data.risk;
      document.getElementById("route").innerText = data.route;

      loadMap(data.lat, data.lon);
    });
}

function loadMap(lat, lon) {
  let location = { lat: lat, lng: lon };

  if (!map) {
    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: location
    });
  }

  new google.maps.Marker({
    position: location,
    map: map
  });

  map.setCenter(location);
}
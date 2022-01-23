mapboxgl.accessToken =
  "MApBOXAPIKEY";
const map = new mapboxgl.Map({
  container: "map", // container ID
  style: "mapbox://styles/mapbox/streets-v11", // style URL
  center: [36.3219, 1.2921], // starting position [lng, lat]
  zoom: 9, // starting zoom
});

map.on("load", function () {
  fetch("http://localhost:8000/api/address/")
    .then((res) => res.json())
    .then((data) =>
      data.forEach((element) => {
        new mapboxgl.Marker({ color: "#b40219" })
          .setLngLat([element.long, element.lat])
          .addTo(map);
      })
    );
});

mapboxgl.accessToken =
  "pk.eyJ1IjoiYmVuamFtaW5vYmEiLCJhIjoiY2thcTN0NnA0MGc1bTJ1bXM1eWNhNXlzNyJ9.4dZbi6CnmRWapW2kMWE4eA";
const map = new mapboxgl.Map({
  container: "map", // container ID
  style: "mapbox://styles/mapbox/streets-v11", // style URL
  center: [36.3219, 1.2921], // starting position [lng, lat]
  zoom: 9, // starting zoom
});

map.on("load", function () {
  fetch("https://covid-tracker-assessement.herokuapp.com/api/address/")
    .then((res) => res.json())
    .then((data) =>
      data.forEach((element) => {
        new mapboxgl.Marker({ color: "#b40219" })
          .setLngLat([element.long, element.lat])
          .addTo(map);
      })
    );
});

var map = L.map('swipemap').setView([51.462405, -0.066630], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

setTimeout(function() {
  map.invalidateSize();
}, 100);

fetch('data/AreaWithLightDensity.geojson')
  .then(res => res.json())
  .then(data => L.geoJson(data).addTo(map));




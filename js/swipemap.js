var map = L.map('swipemap').setView([51.462405, -0.066630], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

setTimeout(function() {
  map.invalidateSize();
}, 100);

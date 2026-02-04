var map = L.map('swipemap').setView([51.462405, -0.066630], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

setTimeout(function() {
  map.invalidateSize();
}, 100);

fetch('data/AreaWithLightDensity.geojson')
  .then(response => response.json())
  .then(data => {
    // 1. Extract values from the property
    let values = data.features.map(f => f.properties.Density);

    // 2. Calculate 5 natural breaks (Jenks)
    let breaks = turf.jenks(values, 5);

    // 3. Color function based on natural breaks
    function getColor(value) {
      for (let i = 0; i < breaks.length - 1; i++) {
        if (value >= breaks[i] && value <= breaks[i+1]) {
          // pick a color ramp (you can choose your own)
          return ['#FFEDA0','#FED976','#FEB24C','#FD8D3C','#FC4E2A'][i];
        }
      }
      return '#FFEDA0';
    }

    // 4. Add GeoJSON layer
    L.geoJSON(data, {
      style: function(feature) {
        return {
          fillColor: getColor(feature.properties.Density),
          weight: 2,
          color: 'white',
          fillOpacity: 0.7
        };
      },
      onEachFeature: function(feature, layer) {
        layer.bindPopup(`${feature.properties.Density}`);
      }
    }).addTo(map);
  });
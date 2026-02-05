var map = L.map('swipemap').setView([51.462405, -0.066630], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

setTimeout(function() {
  map.invalidateSize();
}, 100);

// Color function for choropleth
function getColor(d) {
    return d > 90652  ? '#BD0026' :
           d > 46250  ? '#E31A1C' :
           d > 25294  ? '#FC4E2A' :
           d > 13085  ? '#FD8D3C' :
           d > 305    ? '#FEB24C' :
                        '#FFEDA0'; 
}

// Style function for each feature
function style(feature) {
    return {
        fillColor: getColor(feature.properties.Density), // Use your GeoJSON property
        weight: 0.5,
        opacity: 1,
        color: 'white',
        fillOpacity: 0.7
    };
}

// Fetch GeoJSON and add to map with style
fetch('data/AreaWithLightDensity.geojson')
  .then(res => res.json())
  .then(data => {
      L.geoJson(data, {style: style}).addTo(map);
  });


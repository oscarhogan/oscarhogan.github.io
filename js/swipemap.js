// Map 1 - Density

var map = L.map('densitymap').setView([51.462405, -0.066630], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

setTimeout(function() {
  map.invalidateSize();
}, 100);

// Color function for choropleth
function getColorDensity(d) {
    return d > 90652  ? '#BD0026' :
           d > 46250  ? '#E31A1C' :
           d > 25294  ? '#FC4E2A' :
           d > 13085  ? '#FD8D3C' :
                        '#FFEDA0'; 
}

// Style function for each feature
function styleDensity(feature) {
    return {
        fillColor: getColorDensity(feature.properties.Density), // Use your GeoJSON property
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
      L.geoJson(data, {style: styleDensity}).addTo(map);
  });


// Map 2 - Light Density

var map2 = L.map('lightdensitymap').setView([51.462405, -0.066630], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map2);

setTimeout(function() {
  map2.invalidateSize();
}, 100);

// Color function for choropleth
function getColorLightDensity(d) {
    return d > 6487  ? '#BD0026' :
           d > 3698  ? '#E31A1C' :
           d > 1630  ? '#FC4E2A' :
           d > 961  ? '#FD8D3C' :
           d > 495    ? '#FEB24C' :
                        '#FFEDA0'; 
}

function styleLightDensity(feature) {
    return {
        fillColor: getColorLightDensity(feature.properties.lightdensi), // Use your GeoJSON property
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
      L.geoJson(data, {style: styleLightDensity}).addTo(map2);
  });
import geopandas as gpd
import json

# ---------------------------
# Load data
# ---------------------------
gdf = gpd.read_file("data/AreaWithLightDensity.geojson").to_crs("EPSG:4326")
outline = gpd.read_file("data/AreaOutline.geojson")
borolabel = gpd.read_file("data/AreaLabels.geojson")

# Convert GeoDataFrames to GeoJSON strings
density_geojson = gdf.to_json()
light_geojson = gdf.to_json()  # same geometry, different property for coloring
outline_geojson = outline.to_json()

# ---------------------------
# Create HTML with Leaflet and SideBySide
# ---------------------------
html_template = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Population vs Light Density</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Leaflet CSS/JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<!-- Leaflet SideBySide -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet-side-by-side/2.2.0/leaflet-side-by-side.min.css"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-side-by-side/2.2.0/leaflet-side-by-side.min.js"></script>

<style>
#map {{ width: 100%; height: 100vh; }}
</style>
</head>
<body>
<div id="map"></div>
<script>
// Initialize map
var map = L.map('map').setView([51.462396, -0.066644], 13);

// Base layer
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a>',
    subdomains: 'abcd',
    maxZoom: 19
}}).addTo(map);

// Color scales
function getDensityColor(d) {{
    return d > {gdf['Density'].max()} ? '#08519c' :
           d > {gdf['Density'].quantile(0.8)} ? '#3182bd' :
           d > {gdf['Density'].quantile(0.6)} ? '#6baed6' :
           d > {gdf['Density'].quantile(0.4)} ? '#bdd7e7' :
           '#eff3ff';
}}

function getLightColor(d) {{
    return d > {gdf['lightdensi'].max()} ? '#08519c' :
           d > {gdf['lightdensi'].quantile(0.8)} ? '#3182bd' :
           d > {gdf['lightdensi'].quantile(0.6)} ? '#6baed6' :
           d > {gdf['lightdensi'].quantile(0.4)} ? '#bdd7e7' :
           '#eff3ff';
}}

// Density layer
var densityLayer = L.geoJson({density_geojson}, {{
    style: function(feature) {{
        return {{
            fillColor: getDensityColor(feature.properties.Density),
            fillOpacity: 0.7,
            weight: 0
        }};
    }}
}});

// Light layer
var lightLayer = L.geoJson({light_geojson}, {{
    style: function(feature) {{
        return {{
            fillColor: getLightColor(feature.properties.lightdensi),
            fillOpacity: 0.7,
            weight: 0
        }};
    }}
}});

// Add outlines
L.geoJson({outline_geojson}, {{
    style: function(feature) {{
        return {{color:'skyblue', weight:2, fill:false}};
    }}
}}).addTo(map);

// Add borough labels
var labels = {json.dumps([{ 'name': r['name'], 'coords':[r.geometry.centroid.y, r.geometry.centroid.x]} for idx,r in borolabel.iterrows()])};
labels.forEach(function(lbl){{
    L.marker(lbl.coords, {{
        icon: L.divIcon({{
            className: 'label',
            html: '<div style="font-size:16px;font-weight:800;color:darkblue;text-shadow:0 0 3px white">' + lbl.name + '</div>'
        }})
    }}).addTo(map);
}});

// Add side-by-side slider
L.control.sideBySide(densityLayer, lightLayer).addTo(map);
</script>
</body>
</html>
"""

# ---------------------------
# Save HTML
# ---------------------------
with open("AllBoroLightsMap_Slider.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("AllBoroLightsMap_Slider.html created! Open it in a browser to see the slider.")



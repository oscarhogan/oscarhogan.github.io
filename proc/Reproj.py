#Reproj network Geojson

import geopandas as gpd

network = gpd.read_file('data/network.geojson')
print(network.crs)
network = network.to_crs(epsg=4326)
print(network.crs)
network.to_file('data/network.geojson', driver='GeoJSON')
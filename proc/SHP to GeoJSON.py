import geopandas as gpd

#Converting shapefiles to GeoJSON

gdf = gpd.read_file("data/AreaWithLightDensity.shp").to_crs("EPSG:4326")
gdf["geometry"] = gdf.geometry.simplify(tolerance=0.0001, preserve_topology=True)
gdf.to_file("data/AreaWithLightDensity.geojson", driver="GeoJSON")

outline = gpd.read_file("data/AreaOutline.shp").to_crs("EPSG:4326")
outline["geometry"] = outline.geometry.simplify(tolerance=0.0001, preserve_topology=True)
outline.to_file("data/AreaOutline.geojson", driver="GeoJSON")

labels = gpd.read_file("data/AreaLabels.shp").to_crs("EPSG:4326")
labels.to_file("data/AreaLabels.geojson", driver="GeoJSON")
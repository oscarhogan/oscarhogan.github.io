import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import geopandas as gpd

area = gpd.read_file("data/PopDensity.shp")
lights = gpd.read_file("data/AllBoroLights.shp")

area = area.to_crs("EPSG:27700")
lights = lights.to_crs("EPSG:27700")

print(area["geometry"].head(5))
print(lights["geometry"].head(5))

joined = gpd.sjoin(lights, area, how="left", predicate="intersects")

light_counts = joined["index_right"].value_counts()

print(light_counts.head(5))

area["lightstotal"] = light_counts.fillna(0)

area["areakm2"] = area.geometry.area / 1_000_000 

area["lightdensity"] = area["lightstotal"] / area["areakm2"]

area["lightdensity"] = area["lightdensity"].fillna(0)

area = area.to_crs("EPSG:4326")

area = area.to_file("data/AreaWithLightDensity.shp")


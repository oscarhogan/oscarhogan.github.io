from numpy import rint
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import geopandas as gpd


gdf = gpd.read_file("data/areabounds.shp")
popden = pd.read_csv("data/PopDenNomis.csv")
Southwarklightloc = pd.read_csv("data/LightLoc.csv")
Lewishamlightloc = gpd.read_file("data/Lewisham.shp")
Lambethlightloc = gpd.read_file("data/Street_Lighting.shp")

gdf = gdf.to_crs("EPSG:4326")

popden = pd.read_csv("data/PopDenNomis.csv")
merged = gdf.merge(popden, left_on="OA21CD", right_on="2021 output area")

lightlocgdf = gpd.GeoDataFrame(Southwarklightloc, geometry=gpd.points_from_xy(Southwarklightloc.easting, Southwarklightloc.northing))
Southwark = lightlocgdf.set_crs("EPSG:27700")
Southwark = Southwark.to_crs("EPSG:4326")

Lewisham = Lewishamlightloc.set_crs("EPSG:4326")
Lambeth = Lambethlightloc.to_crs("EPSG:4326")

print(Lewisham.geometry.head(5))
print(Lambeth.geometry.head(5))
print(Southwark.geometry.head(5))

#Lewisham is fucked will fix tomoz
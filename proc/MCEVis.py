import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import geopandas as gpd


gdf = gpd.read_file("data/areabounds.shp")
gdf = gdf.to_crs("EPSG:4326")
popden = pd.read_csv("data/PopDenNomis.csv")
lightloc = pd.read_csv("data/LightLoc.csv")

merged = gdf.merge(popden, left_on="OA21CD", right_on="2021 output area")

print(merged.crs)

print(lightloc.head())

print(lightloc.head)

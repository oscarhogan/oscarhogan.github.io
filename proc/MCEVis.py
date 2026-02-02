import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import geopandas as gpd

Southwark = pd.read_csv("data/LightLoc.csv")
Lewisham = gpd.read_file("data/Lewisham.shp")
Lambeth = gpd.read_file("data/Street_Lighting.shp")

lightlocgdf = gpd.GeoDataFrame(Southwark, geometry=gpd.points_from_xy(Southwark.easting, Southwark.northing))
Southwark = lightlocgdf.set_crs("EPSG:27700")
Southwark = Southwark.to_crs("EPSG:4326")

Lewisham = Lewisham.set_crs("EPSG:27700",allow_override=True)
Lewisham = Lewisham.to_crs("EPSG:4326")

Lambeth = Lambeth.to_crs("EPSG:4326")

AllBoro = gpd.GeoDataFrame(pd.concat([Southwark, Lewisham, Lambeth], ignore_index=True))

AllBoro = AllBoro.to_crs("EPSG:4326")

AllBoro.to_file("data/AllBoroLights.shp")

#Output shape file containing street lights from all three boroughs
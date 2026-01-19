import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("Documents/OscarWeb/data/areabounds.shp")
popden = pd.read_csv("Documents/OscarWeb/data/PopDenNomis.csv")


merged = gdf.merge(popden, left_on="OA21CD", right_on="2021 output area")

print(merged.columns)

merged2 = 
#merged.plot(column="Density", cmap="OrRd", legend=True)
#plt.show()
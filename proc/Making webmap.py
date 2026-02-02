import folium
import geopandas as gpd
import mapclassify

#Core data
gdf = gpd.read_file("data/AreaWithLightDensity.geojson")
gdf = gdf.to_crs("EPSG:4326")

#Additional aesthetic context
outline = gpd.read_file("data/AreaOutline.geojson")
borolabel = gpd.read_file("data/AreaLabels.geojson")

# Defining bins using Jenks Natural Breaks - Population Density

jenks_density = mapclassify.NaturalBreaks(gdf["Density"], k=5)
jenks_bins_density = [gdf["Density"].min()] + jenks_density.bins.tolist()

#Defining bins using Jenks Natural Breaks - Light Density

jenks_light = mapclassify.NaturalBreaks(gdf["lightdensi"], k=5)
jenks_bins_light = [gdf["lightdensi"].min()] + jenks_light.bins.tolist()

#Creatuing map using folium

m = folium.Map(location=[51.45, -0.1], zoom_start=11, tiles='CartoDB positron')

# Population Density Layer
folium.Choropleth(
    geo_data=gdf,
    data=gdf,
    columns=["OA21CD", "Density"],
    key_on="feature.properties.OA21CD",
    fill_color="YlGnBu",
    fill_opacity=0.5,
    line_opacity=0,
    legend_name="Population Density (Jenks)",
    bins=jenks_bins_density,
    reset=True
).add_to(m)

# Light Density Layer
folium.Choropleth(
    geo_data=gdf,
    data=gdf,
    columns=["OA21CD", "lightdensi"],
    key_on="feature.properties.OA21CD",
    fill_color="YlGnBu",
    fill_opacity=0.5,
    line_opacity=0,
    legend_name="Light Density (Jenks)",
    bins=jenks_bins_light,
    reset=True
).add_to(m)

folium.GeoJson(
    outline,
    name="Area Outline",
    style_function=lambda x: {
        'color': 'skyblue',
        'weight': 2,
        'fill': False
    }
).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

m.save("AllBoroLightsMap.html")
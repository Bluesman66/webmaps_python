import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[42.8799019, -113.2210007], zoom_start=5)
fg = folium.FeatureGroup(name="My Group")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=6,
            popup=str(el) + "m",
            fill_color=color_producer(el),
            color="grey",
            fill_opacity=0.7)
        )

with open("world.json", "r", encoding="utf-8-sig") as world_file:
    fg.add_child(folium.GeoJson(data=(world_file).read()))

map.add_child(fg)

map.save("map2.html")
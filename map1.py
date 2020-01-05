import folium

map = folium.Map(location=[55.199100, 61.327461], zoom_start=12)
fg = folium.FeatureGroup(name="My Group")

for coordinates in [[55.189100, 61.227461], [55.199100, 61.327461]]:
    fg.add_child(
        folium.Marker(
            location=coordinates,
            popup="Hi, there!",
            icon=folium.Icon(color="red")
        )
    )

map.add_child(fg)

map.save("map1.html")

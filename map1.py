import folium

map = folium.Map(location=[55.199100, 61.327461], zoom_start=16)
fg = folium.FeatureGroup(name="My Group")
fg.add_child(
    folium.Marker(
        location=[55.199100, 61.327461],
        popup="Hi, there!", 
        icon=folium.Icon(color="red")
    )
)
map.add_child(fg)

map.save("map1.html")
import folium

def show_map(lat, lon, hospitals):

    m = folium.Map(location=[lat, lon], zoom_start=13)

    folium.Marker(
        [lat, lon],
        tooltip="Your Location",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    for hospital in hospitals:

        folium.Marker(
            [hospital["lat"], hospital["lon"]],
            tooltip=hospital["name"],
            icon=folium.Icon(color="red", icon="plus")
        ).add_to(m)

    return m
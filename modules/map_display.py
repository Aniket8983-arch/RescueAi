import folium

def show_map(lat, lon, hospitals):

    m = folium.Map(location=[lat, lon], zoom_start=13)

    # user location
    folium.Marker(
        [lat, lon],
        popup="Your Location",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    for hospital in hospitals:

        popup = hospital["name"]

        folium.Marker(
            [hospital["lat"], hospital["lon"]],
            popup=popup,
            tooltip=popup,
            icon=folium.Icon(color="red", icon="plus")
        ).add_to(m)

    return m
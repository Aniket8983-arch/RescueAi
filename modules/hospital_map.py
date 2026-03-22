import requests

def get_nearby_hospitals(lat, lon):

    overpass_url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:5000,{lat},{lon});
      way["amenity"="hospital"](around:5000,{lat},{lon});
      relation["amenity"="hospital"](around:5000,{lat},{lon});
    );
    out center;
    """

    try:
        response = requests.get(overpass_url, params={"data": query})

        if response.status_code != 200:
            return []

        data = response.json()

        hospitals = []

        for element in data.get("elements", []):

            lat = element.get("lat") or element.get("center", {}).get("lat")
            lon = element.get("lon") or element.get("center", {}).get("lon")

            if not lat or not lon:
                continue

            name = element.get("tags", {}).get("name", "Hospital")
            address = element.get("tags", {}).get("addr:full", "Address not available")
            phone = element.get("tags", {}).get("phone", None)

            hospitals.append({
                "name": name,
                "lat": lat,
                "lon": lon,
                "address": address,
                "phone": phone
            })

        return hospitals

    except:
        return []
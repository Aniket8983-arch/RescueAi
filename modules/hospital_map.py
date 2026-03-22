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
    out center tags;
    """

    try:

        response = requests.get(
            overpass_url,
            params={"data": query},
            timeout=15
        )

        if response.status_code != 200:
            return []

        data = response.json()

    except Exception:
        return []

    hospitals = []

    for element in data.get("elements", []):

        if "lat" in element:
            lat = element["lat"]
            lon = element["lon"]
        else:
            lat = element["center"]["lat"]
            lon = element["center"]["lon"]

        tags = element.get("tags", {})

        hospitals.append({
            "name": tags.get("name", "Hospital"),
            "lat": lat,
            "lon": lon,
            "address": tags.get("addr:full", "Address not available"),
            "phone": tags.get("phone")
        })

    return hospitals
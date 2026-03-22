import requests

def get_coordinates(city):

    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"

    try:
        response = requests.get(url, headers={"User-Agent": "rescue-ai"})
        data = response.json()

        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])

        return None, None

    except:
        return None, None
from geopy.geocoders import Nominatim

def get_coordinates(city):

    geolocator = Nominatim(user_agent="first_aid_app")

    location = geolocator.geocode(city)

    if location:
        return location.latitude, location.longitude
    else:
        return None, None
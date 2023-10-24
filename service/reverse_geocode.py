import requests

from exceptions import GmapsClientError


def get_address_by_latlng(gmaps_apikey, latitude, longitude):
    url = google_maps_url(gmaps_apikey, latitude, longitude)

    resp =  requests.get(url, timeout=10000)

    if resp.status_code >= 400:
        raise GmapsClientError()
    
    return resp.json()


def google_maps_url(maps_google_api_key, latitude=-23.446, longitude=-46.755):
    return f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&location_type=ROOFTOP&result_type=street_address&key={maps_google_api_key}"

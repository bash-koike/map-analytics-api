import os

import requests


PLACES_API_KEY = os.environ['PLACES_API_KEY']


def place_search(input, inputtype='textquery'):
    # Args:
    #   input: The text input specifying which place to search for (for example, a name, address, or phone number).
    #   inputtype: inputtype — The type of input. This can be one of either textquery or phonenumber.
    #              Phone numbers must be in international format (prefixed by a plus sign ("+"), followed by the country code, then the phone number itself).
    #
    # References:
    #   https://developers.google.com/places/web-service/search

    URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    res = requests.get(
        URL,
        params={
            'key': PLACES_API_KEY,
            'input': input,
            'inputtype': inputtype,
            'language': 'ja',
            'region': 'jp'
        })
    res_dict = res.json()

    return res_dict


def place_details(place_id):
    # Args:
    #   place_id: A textual identifier that uniquely identifies a place, returned from a Place Search. For more information about place IDs.
    #
    # References:
    #   https://developers.google.com/places/web-service/details

    URL = 'https://maps.googleapis.com/maps/api/place/details/json'
    res = requests.get(
        URL,
        params={
            'key': PLACES_API_KEY,
            'placeid': place_id,
            'language': 'ja',
            'region': 'jp'
        })
    res_dict = res.json()

    return res_dict


def nearby_search(location, radius, keyword):
    # Args:
    #   lat: latitude
    #   lng: longitude
    #   radius: radius from location. Unit is meter.
    #
    # References:
    #   https://developers.google.com/places/web-service/search

    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    res = requests.get(
        URL,
        params={
            'key': PLACES_API_KEY,
            'location': f"{location['lat']},{location['lng']}",
            'radius': radius,
            'keyword': keyword,
            'language': 'ja',
            'region': 'jp'
        })
    res_dict = res.json()

    return res_dict

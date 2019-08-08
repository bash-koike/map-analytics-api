from pprint import pprint

from libs import places_api


def test_place_details():
    # Get place ids from places API
    res = places_api.place_search('新宿御苑')

    # Get place details from place details API
    res = places_api.place_details(res['candidates'][0]['place_id'])

    return res


def test_nearby_search():

    # Get place ids from places API
    res = places_api.place_search('東京駅')

    # Get place details from place details API
    res = places_api.place_details(res['candidates'][0]['place_id'])

    # Get nearby places from nearby search API
    location = res['result']['geometry']['location']
    res = places_api.nearby_search(location, radius=5000, keyword='カフェ')

    dict_list = []
    for r in res['results']:
        import json
        print(json.dumps(r, ensure_ascii=False))
        import sys; sys.exit(0)
        dict_list.append({
            'lat': location['lat'],
            'lng': location['lng'],
            'name': r['name'],
            'place_id': r['place_id'],
            'rating': r['rating']
        })
    pprint(dict_list)

    return dict_list


if __name__ == "__main__":
    # test_place_details()
    test_nearby_search()

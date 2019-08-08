import csv
import datetime
import json
import os
import tempfile

from handlers import handlers
from libs import places_api, s3


@handlers.func_handler
def lambda_handler(event, context):

    # Get query parameters
    my_place = event['queryStringParameters']['my_place']
    keyword = event['queryStringParameters']['keyword']
    radius = event['queryStringParameters'].get('radius')
    if radius is None:
        radius = 5000

    # Get place ids from places API
    res = places_api.place_search(my_place)

    # Get place details from place details API
    res = places_api.place_details(res['candidates'][0]['place_id'])

    # Get nearby places from nearby search API
    location = res['result']['geometry']['location']
    res = places_api.nearby_search(location, radius=radius, keyword=keyword)

    dict_list = []
    for r in res['results']:
        dict_list.append({
            'lat': location['lat'],
            'lng': location['lng'],
            'address': r['vicinity'],
            'name': r['name'],
            'place_id': r['place_id'],
            'rating': r['rating']
        })

    # Write CSV file and upload it to S3.
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Use datetime instead of uuid
        now_iso8601 = datetime.datetime.now().isoformat()
        csv_filename = f'{my_place}_{keyword}_{now_iso8601}.csv'
        csv_path = os.path.join(tmp_dir, csv_filename)

        with open(csv_path, 'w', encoding="utf_8_sig") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['lat', 'lng', 'address', 'name', 'place_id', 'rating'])
            writer.writeheader()
            writer.writerows(dict_list)

        s3_key = f'places/{csv_filename}'
        s3.upload_file(csv_path, s3_key)

    # Make response
    body = {
        'status': 'OK',
        'code': 200,
        's3_location': f's3://map-analytics-api/{s3_key}'
    }
    body = json.dumps(body, ensure_ascii=False)
    res = {
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': body
    }

    return res

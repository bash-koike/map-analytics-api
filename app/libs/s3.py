import boto3


s3 = boto3.resource('s3')
bucket = s3.Bucket('map-analytics-api')


def upload_file(filename, key):
    res = bucket.upload_file(filename, key)
    return res

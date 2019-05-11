# -*- coding: utf-8 -*-
'''
getparse.py
1.  collect data from opendata api. 
2.  parse out lat, long, no, nox, no2, and records time
3.  save data to be opened in html / leaflet
Author: nigel@knowtext.co.uk
Created: 15 April 2019, 12:00

'''

import requests
import json
import boto3

def get_data(event, context):
    response = requests.get("https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=nox_wide&q=date_time%3E%3d%23now(hours=-3)&sort=date_time&apikey=6c2afeadeeaea3dcbbd1c2f48551bc37e043a0ac4ee5bf59855e05d0")
    data = response.json()
    mapdata = []
    for i in range(0,9):
        dat = [data['records'][i]['fields']['geo_point_2d'][0], 
               data['records'][i]['fields']['geo_point_2d'][1], 
               data['records'][i]['fields']['no'],
               data['records'][i]['fields']['nox'],
               data['records'][i]['fields']['no2']]
        mapdata.append(dat)
    AWS_BUCKET_NAME = 'airqual19'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    s3.Object('airqual19', 'noxdata.js').delete()
    path = 'noxdata.js'
    data = 'var noPoints = ' + str(mapdata) 
    bucket.put_object(
        ACL='public-read',
        ContentType='text/plain',
        Key=path,
        Body=data,
    )

    body = {
        "uploaded": "true",
        "bucket": AWS_BUCKET_NAME,
        "path": path,
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }

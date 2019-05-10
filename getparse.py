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
    response = requests.get("https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=nox_wide&q=date_time%3E%3d%23now(hours=-2)&apikey=6c2afeadeeaea3dcbbd1c2f48551bc37e043a0ac4ee5bf59855e05d0")
    data = response.json()
    mapdata = {}
    for i in range(0,9):
        dat = {}
        dat['recno'] = i
        try:
            dat['recordid'] = data['records'][i]['recordid']
            dat['time'] = data['records'][i]['fields']['date_time']
            dat['latitude'] = data['records'][i]['fields']['geo_point_2d'][0]
            dat['longitude'] = data['records'][i]['fields']['geo_point_2d'][1]
            dat['no'] = data['records'][i]['fields']['no']
            dat['nox'] = data['records'][i]['fields']['nox']
            dat['no2'] = data['records'][i]['fields']['no2']
        except:
            dat['recordid'] = 'na'
            dat['time'] = 'na'
            dat['latitude'] = 'na'
            dat['longitude'] = 'na'
            dat['no'] = 'na'
            dat['nox'] = 'na'
            dat['no2'] = 'na'
        mapdata[i] = dat
    AWS_BUCKET_NAME = 'airqual19'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    s3.Object('airqual19', 'noxdata.json').delete()
    path = 'noxdata.json'
    data = json.dumps(mapdata)
    bucket.put_object(
        ACL='public-read',
        ContentType='application/json',
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

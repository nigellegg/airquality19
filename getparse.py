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


from lambdabase import LambdaBase

class AirQualDataClass(LambdaBase):
    def __init__(self, event): # implementation-specific args and/or kwargs
        self.data = ''

    def handle(self, event, context):
        self.get_data()
        self.get_fields()
        self.save_to_bucket()

    def get_data():
    	response = requests.get("https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=nox_wide&q=date_time = #now(hours=-2)&apikey=6c2afeadeeaea3dcbbd1c2f48551bc37e043a0ac4ee5bf59855e05d0")
        data = response.json()
        self.data = data 
        return True

    def get_fields():
    	data = self.data
    	mapdata = {}
    	for i in range(0,9):
           	dat = {}
    	    dat['recno'] = i
    	    dat['recordid'] = data['records'][i]['recordid']
    	    dat['time'] = data['records'][i]['fields']['date_time']
    	    dat['location'] = data['records'][i]['fields']['geo_point_2d']
    	    dat['no'] = date['records'][i]['fields']['no']
    	    dat['nox'] = data['records'][i]['fields']['nox']
    	    dat['no2'] = data['records'][i]['fields']['no2']
            mapdata[i] = dat
        out = open('nox.json', 'w')
        data = json.load(mapdata)
        json.dumps(data, out)
        self.data = data
        return True

    def save_to_bucket(event, context):
        AWS_BUCKET_NAME = 'airqual19'
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(AWS_BUCKET_NAME)
        path = 'noxdata.txt'
        data = self.data
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

handler = AirQualDataClass.get_handler(self, event) # input values for args and/or kwargs
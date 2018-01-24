#!/usr/bin/env python
from  collections import OrderedDict
from pymongo import MongoClient
from sys import exit
from os import getcwd, environ
import xmltodict
import json
import requests


def create_json_output(xml_file, json_file):
    with open(xml_file) as fd:
        doc = xmltodict.parse(fd.read())
    with open(json_file, 'w') as f:
        f.write(json.dumps(doc['robot']))
    print 'Json:   ', json_file

    # Post json data to gateway api
    mongo_api_host = environ.get('API_GATEWAY_SERVICE_ENDPOINT')
    mongo_api_port = environ.get('API_GATEWAY_SERVICE_PORT')
    mongo_db_name = environ.get('MONGO_DB_NAME')
    gateway_api_url = "http://" + str(mongo_api_host) + ":" + str(mongo_api_port) + "/automation/results/testing"
    payload = json.dumps(doc['robot'])
    payload = json.loads(payload)
    r = requests.post(gateway_api_url, json=payload)
    print 'Json:    ' + 'posted json output to ', gateway_api_url
    print r.text



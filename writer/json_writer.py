#!/usr/bin/python3
from  collections import OrderedDict
from pymongo import MongoClient
from sys import exit
from os import getcwd, environ
import xmltodict
import json


def create_json_output(xml_file, json_file):
    with open(xml_file) as fd:
        doc = xmltodict.parse(fd.read())
    with open(json_file, 'w') as f:
        f.write(json.dumps(doc['robot']))
    print 'Json:   ', json_file

def write_json_todb(json_file):
    try:
        db_instances = environ.get('MONGO_DBS').split(',')
    except:
        print '\n'
        print "Not such env variable named MONGO_DBS, create before running tests"
        print "Example: MONGO_DBS='127.0.0.1:27017,127.0.0.2:27017'"
    with open(json_file) as jfile:
        json_data = json.loads(jfile.read())
        for i in db_instances:
            try:
                ip,port = i.split(':')
                client = MongoClient(ip, int(port))
                db = client.json_db
                result = db.json_db.insert_one(json_data)
                client.close()
                print('Json:    ' + 'Written successfully to mongoDB')
            except:
                print('Can not connect/write to DB')


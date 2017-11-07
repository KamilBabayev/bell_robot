#!/usr/bin/python3
from robot.conf import RobotSettings
from  collections import OrderedDict
from pymongo import MongoClient
from sys import exit
from os import getcwd
import xmltodict
import json


settings = RobotSettings()

def create_json_output(xml_file, json_file):
    with open(xml_file) as fd:
        doc = xmltodict.parse(fd.read())
    with open(json_file, 'w') as f:
        f.write(json.dumps(doc['robot']))
    p = getcwd() + "/logs/" + "output.json"
    print('Json:   ', p)

def write_json_todb(json_file):
    with open(json_file) as jfile:
        try:
            client = MongoClient('127.0.0.1', 27017)
            db = client.db0005
        except:
            print('can not connect to database')
        result = db.db0005.insert_one(json.loads(jfile.read()))
        print('Json:    ' + 'Written successfully to mongoDB')

#if __name__ == "__main__":
#    create_json_output(xml_file)
#    write_json_todb(json_file)

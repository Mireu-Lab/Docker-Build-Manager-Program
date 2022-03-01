# -*- coding: utf-8 -*-
import json, os

def status(name):
    filelocation = 'Data/Docker_Container/json/containers_{}.json'.format(name)
    jsondata = open(filelocation, "r", encoding="utf-8")

    return json.load(jsondata)

def dockerid(name):
    filelocation = 'Data/Docker_Container/json/containers_{}.json'.format(name)
    jsondata = open(filelocation, "r", encoding="utf-8")

    return json.load(jsondata)['id']

def status_bool(name): 
    filelocation = 'Data/Docker_Container/json/containers_{}.json'.format(name)

    if os.path.isfile(filelocation):
        return True
    else:
        return False

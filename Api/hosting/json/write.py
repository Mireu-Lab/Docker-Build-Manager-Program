# -*- coding: utf-8 -*-
import datetime, json, os
from time import sleep
from ..manage import *

# 이메일 테이블 에 데이터 추가
def add_data(name, dockerid, port, token, status, os):
    filelocation = 'Data/Docker_Container/json/containers_{0}.json'.format(name)
    jsondata = {
        'name':name,
        'id':dockerid,
        'port':port,
        'status':status,
        'os':os,
        'time':str(datetime.datetime.now())
    }
    jsonwrite = open(filelocation, "w",encoding="utf-8")
    json.dump(jsondata, jsonwrite, indent="\t")

    return 'Container add done'

# 이메일 테이블에 데이터 업데이트
def update(status, name):
    filelocation = 'Data/Docker_Container/json/containers_{0}.json'.format(name)

    jsondata = open(filelocation, "r", encoding="utf-8")
    jsonlist = json.load(jsondata)
    
    jsonlist["status"] = status
    
    jsonwrite = open(filelocation, "w", encoding="utf-8")
    json.dump(jsonlist, jsonwrite, indent="\t")

    return "Update Done"

# 이메일 테이블에 데이터 삭제
def json_delete(name):
    filelocation = 'Data/Docker_Container/json/containers_{0}.json'.format(name)
    os.remove(filelocation)

    return 'Container delete data done'
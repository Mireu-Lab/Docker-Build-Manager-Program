# -*- coding: utf-8 -*-
from .hosting.json import *

from fastapi import FastAPI
import uvicorn

from pytz import timezone
import datetime

import json

with open('Data/set.json','r') as docker_image_url:
    url = json.load(docker_image_url)

app=FastAPI()
run_time = datetime.datetime.now(timezone('Asia/Seoul'))


@app.get("/", tag=["test"])
async def version():
    return {
        "Run Time" : run_time, 
        "DB Program" : "SQL", 
        "Docker Image Url" : {
            "ubuntu" : url["docker image"]["ubuntu"],
            "fedora" : url["docker image"]["fedora"]
        }
    }

#사용자 도커 SQL 테이블 생성
@app.post("/container/build", tags=["container"])
async def build(name:str, os:bool):
    pass

@app.post("/container/status", tags=["container"])
async def status(name:str):
    pass

@app.post("/container/stop", tags=["container"])
async def stop(name:str):
    pass

@app.post("/container/start", tags=["container"])
async def start(name:str):
    pass

@app.post("/container/restart", tags=["container"])
async def restart(name:str):
    pass

@app.post("/container/delete", tags=["container"])
async def delete(name:str):
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=65000)
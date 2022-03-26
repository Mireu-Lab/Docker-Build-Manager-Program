# -*- coding: utf-8 -*-
from hosting import hosting

from fastapi import FastAPI
import uvicorn

from pytz import timezone
import datetime

import json

with open('Data/set.json','r') as docker_image_url:
    url = json.load(docker_image_url)

app=FastAPI()
run_time = datetime.datetime.now(timezone('Asia/Seoul'))

@app.get("/", tags=["test"])
async def version():
    return {
        "run_time" : run_time, 
        "db_program" : "SQL", 
        "Docker Image Url" : {
            "Ubuntu" : url["docker image"]["ubuntu"],
            "Fedora" : url["docker image"]["fedora"]
        }
    }

#사용자 도커 SQL 테이블 생성
@app.post("/container/build", tags=["container"])
async def build(name:str, os:bool):
    return hosting.build(name, os)

@app.post("/container/status", tags=["container"])
async def status(name:str):
    return hosting.info(name)

@app.post("/container/stop", tags=["container"])
async def stop(name:str):
    return hosting.stop(name)

@app.post("/container/start", tags=["container"])
async def start(name:str):
    return hosting.start(name)

@app.post("/container/restart", tags=["container"])
async def restart(name:str):
    return hosting.restart(name)

@app.post("/container/delete", tags=["container"])
async def delete(name:str):
    return hosting.delete(name)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=url["API_Port"])
from .build import ubuntu, fedora
from .sql.write import *
from .sql.read import *
from .manage import *

from pytz import timezone
import datetime

#사용자 도커 컨테이너 빌드
def build(name, os=bool):
    data = status_bool(name)
    
    if data == False:
        if os == True:
            date = ubuntu.build(datetime.datetime.now(timezone('Asia/Seoul')),name)
            return add_data(name, date["dockerid"], date["port"], date["password"], "start", "ubuntu")

        elif os == False:
            date = fedora.build(datetime.datetime.now(timezone('Asia/Seoul')),name)
            return add_data(name, date["dockerid"], date["port"], date["password"], "start", "fedora")

        else:
            return "Unsupported service"

    elif data == True:
        return "Have a container_data with that name"

#사용자 도커 컨테이너 시작
def start(name):
    data = status_bool(name)
    
    if data == True:
        restart(dockerid(name))
        return update("start", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 정지
def stop(name):
    data = status_bool(name)
    
    if data == True:
        stop(dockerid(name))
        return update("stop", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 재시작
def restart(name):
    data = status_bool(name)
    
    if data == True:
        restart(dockerid(name))
        return update("start", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 강제 종료
def kill(name):
    data = status_bool(name)
    
    if data == True:
        kill(dockerid(name))
        return update("stop", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 삭제
def remove(name):
    data = status_bool(name)
    
    if data == True:
        remove(dockerid(name))
        return remove(name)
    elif data == False:
        return 'container_data has already been deleted'

#사용자 도커 컨테이너 웹 리스트 전송
def info(name):
    data = status_bool(name)
    
    if data == True:
        return status(name)
    elif data == False:
        return 'No container_data'

def password(name):
    data = status_bool(name)
    
    if data == True:
        return update(dockerid(name))
    elif data == False:
        return 'No container_data'
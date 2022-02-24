from .build.ubuntu import build as ubuntu_build
from .build.fedora import build as fedora_build
from .json.write import *
from .json.read import *
from .manage import *

from pytz import timezone
import datetime

#사용자 도커 컨테이너 빌드
def build(name, os=bool):
    data = status_bool(name)
    times = datetime.datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')

    if data == False:
        if os == True:
            date = ubuntu_build(times, name)
            return add_data(name, date["dockerid"], date["port"], date["password"], "start", "ubuntu")

        elif os == False:
            date = fedora_build(times, name)
            return add_data(name, date["dockerid"], date["port"], date["password"], "start", "fedora")

        else:
            return "Unsupported service"

    elif data == True:
        return "Have a container_data with that name"

#사용자 도커 컨테이너 시작
def start(name):
    data = status_bool(name)
    
    if data == True:
        container_start(dockerid(name))
        return update("start", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 재시작
def restart(name):
    data = status_bool(name)
    
    if data == True:
        container_restart(dockerid(name))
        return update("start", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 정지
def stop(name):
    data = status_bool(name)
    
    if data == True:
        container_stop(dockerid(name))
        return update("stop", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 강제 종료
def kill(name):
    data = status_bool(name)
    
    if data == True:
        container_kill(dockerid(name))
        return update("stop", name)
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 삭제
def delete(name):
    data = status_bool(name)
    
    if data == True:
        container_delete(dockerid(name))
        return json_delete(name)

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
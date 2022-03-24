from .build.ubuntu import build as ubuntu_build
from .build.fedora import build as fedora_build
from .build.nginx import upload as nginx_upload
from .build.nginx import remove as nginx_remove
from .sql.read import *
from .sql.write import *
from .manage import *

from time import sleep

from pytz import timezone
import datetime

#사용자 도커 컨테이너 빌드
def build(name, os=bool):
    data = status_bool(name)
    times = datetime.datetime.now(timezone('Asia/Seoul')).strftime('%Y%m%d')

    print(data)

    if data == False:
        if os == True:
            date = ubuntu_build(times, name)
            nginx_upload(date["dockerid"], date["port"])
            add_data(name, date["dockerid"], date["port"], date["password"], "start", "ubuntu")
            return "Container add done"

        elif os == False:
            date = fedora_build(times, name)
            nginx_upload(date["dockerid"], date["port"])
            add_data(name, date["dockerid"], date["port"], date["password"], "start", "fedora")
            return "Container add done"

        else:
            return "Unsupported service"

    elif data == True:
        return "Have a container_data with that name"

#사용자 도커 컨테이너 시작
def start(name):
    data = status_bool(name)
    
    if data == True:
        container_start(dockerid(name))
        update("start", name)
        return "Update Done"

    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 재시작
def restart(name):
    data = status_bool(name)
    
    if data == True:
        container_restart(dockerid(name))
        update("start", name)
        return "Update Done"

    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 정지
def stop(name):
    data = status_bool(name)
    
    if data == True:
        container_stop(dockerid(name))
        update("stop", name)
        return "Update Done"
    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 강제 종료
def kill(name):
    data = status_bool(name)
    
    if data == True:
        container_kill(dockerid(name))
        update("stop", name)
        return "Update Done"

    elif data == False:
        return 'No container_data'

#사용자 도커 컨테이너 삭제
def delete(name):
    data = status_bool(name)
    
    if data == True:
        container_delete(dockerid(name))
        nginx_remove(dockerid(name))
        remove(name)
        return "Container delete data done"

    elif data == False:
        return 'container_data has already been deleted'

#사용자 도커 컨테이너 웹 리스트 전송
def info(name):
    data = status_bool(name)
    
    if data == True:
        data1 = status(name)
        if data1['status'] == 'stop':
            return {'info' : data1, 'token' : None}
        elif data1['status'] == 'start':
            sleep(1)
            return {'info' : data1, 'token' : password_update(dockerid(name))}

    elif data == False:
        return 'No container_data'

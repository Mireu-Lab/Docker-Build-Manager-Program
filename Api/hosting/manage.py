# -*- coding: utf-8 -*-
import docker

client = docker.from_env()

# 컨테이너 정지
def container_stop(dockerid):
    client.containers.get(dockerid).stop()

# 컨테이너 강제 종료
def container_kill(dockerid):
    client.containers.get(dockerid).kill()

# 컨테이너 삭제
def container_delete(dockerid):
    container = client.containers.get(dockerid)
    container.stop()
    container.remove()

# 컨테이너 재시작
def container_restart(dockerid):
    dockerget = client.containers.get(dockerid)
    dockerget.stop()
    dockerget.start()

# 컨테이너 시작
def container_start(dockerid):
    client.containers.get(dockerid).start()

def password_update(dockerid):
    dockerdata = client.containers.get(dockerid)
    data1 = str(dockerdata.exec_run(cmd='jupyter server list'))
    return data1[88:136]
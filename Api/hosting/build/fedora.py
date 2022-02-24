# -*- coding: utf-8 -*-
import docker
import json
import random
from time import sleep

with open('Data/set.json','r') as docker_image_url:
    url = json.load(docker_image_url)

client = docker.from_env()

def port():
    port = random.randrange(150,59999)
    return int(port)

def build(time,name):
    ports = int(port())
    name = "{0}_{1}".format(name, time)
    dockerbuild = client.containers.run(
        ports={'8888/tcp': ports},
        hostname="HOSTING",
        image=url['docker image']['fedora'],
        name=name,
        detach=True
    )

    dockerbuild.start()
    sleep(1)
    data1 = str(dockerbuild.exec_run(cmd='jupyter server list'))
    data = {'dockerid' : dockerbuild.short_id, 'port' : ports, "password" : data1[89:137]}
    return data
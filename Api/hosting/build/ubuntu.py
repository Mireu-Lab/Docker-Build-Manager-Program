# -*- coding: utf-8 -*-
import docker
import json
import random
from time import sleep
from .nginx import remove

with open('Data/set.json','r') as docker_image_url:
    url = json.load(docker_image_url)

client = docker.from_env()

def main_ports():
    port = random.randrange(url["container"]["build"]["min"],url["container"]["build"]["max"])
    return int(port)

def proxy_ports():
    port = random.randrange(url["container"]["proxy"]["min"],url["container"]["proxy"]["max"])
    return int(port)

def build(time,name):
    main_port = int(main_ports())
    proxy_port = int(proxy_ports())
    name = "{0}{1}".format(name, time)

    try:
        dockerbuild = client.containers.run(
            ports={'8888/tcp': main_port, '80/tcp' : proxy_port},
            hostname="HOSTING",
            image=url['docker image']['ubuntu'],
            name=name,
            detach=True
        )
        dockerbuild.start()
        sleep(1)
        data1 = str(dockerbuild.exec_run(cmd='jupyter server list'))
        data = {'dockerid' : dockerbuild.short_id, 'docker_port' : main_port, "web_port" : proxy_port, "password" : data1[89:137]}
        return data

    except docker.errors.APIError as e:
        a = str(e)
        if int(a[0:3]) == 409:
            return 409
        elif int(a[0:3]) == 500:
            dockerbuild.remove()
            remove(dockerbuild.short_id)
            build()
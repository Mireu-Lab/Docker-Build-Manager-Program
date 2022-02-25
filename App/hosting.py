import requests
import json

headers = {
    'accept': 'application/json',
}

seturl = "http://192.168.0.2:65000/"

def info():
    response = requests.get(seturl, headers=headers)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def build(name, os):
    if os == "ubuntu":
        os = True
    elif os == "fedora":
        os = False
    
    params = (
        ('name', name),
        ('os', os),
    )
    response = requests.post(seturl+'container/build', headers=headers, params=params)
    if response.status_code == 200:
        return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def status(name):
    params = (('name', name),)

    response = requests.post(seturl+'container/status', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def start(name):
    params = (('name', name),)

    response = requests.post(seturl+'container/start', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def stop(name):
    params = (('name', name),)

    response = requests.post(seturl+'container/stop', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def restart(name):
    params = (('name', name),)

    response = requests.post(seturl+'container/restart', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def delete(name):
    params = (('name', name),)

    response = requests.post(seturl+'container/delete', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}
import requests
import json

headers = {
    'accept': 'application/json',
}

seturl = "http://192.168.0.2:65000/"

def info():
    try:
        response = requests.get(seturl, headers=headers)
        if response.status_code == 200:
            return {"Code" : response.status_code, "Data" : json.loads(response.text)}
        else:
            return {"Code" : response.status_code, "Data" : "응~ 서버 터졌어~"}
    except:
        return {"Code" : 500, "Data" : "응~ 서버 터졌어~"}

def build(name, os, email=None):
    if os == "ubuntu":
        os = True
    elif os == "fedora":
        os = False
    
    params = (
        ('name', name),
        ('os', os),
        ('email', email),
    )
    response = requests.post(seturl+'container/build', headers=headers, params=params)
    if response.status_code == 200:
        return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def status(name, email=None):
    params = (
        ('name', name),
        ('email', email),
    )

    response = requests.post(seturl+'container/status', headers=headers, params=params)
    print(response)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def start(name, email=None):
    params = (
        ('name', name),
        ('email', email),
    )
    response = requests.post(seturl+'container/start', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def stop(name, email=None):
    params = (
        ('name', name),
        ('email', email),
    )

    response = requests.post(seturl+'container/stop', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def restart(name, email=None):
    params = (
        ('name', name),
        ('email', email),
    )
    response = requests.post(seturl+'container/restart', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}

def delete(name, email=None):
    params = (
        ('name', name),
        ('email', email),
    )
    response = requests.post(seturl+'container/delete', headers=headers, params=params)
    return {"Code" : response.status_code, "Data" : json.loads(response.text)}
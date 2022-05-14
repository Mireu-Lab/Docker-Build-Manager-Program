import os
import json
from time import sleep

with open('Data/set.json','r') as docker_image_url:
    url = json.load(docker_image_url)

def upload(dockerid, main_port, proxy_port, ssh_port):
    conf = f"""
    map $http_upgrade $connection_upgrade {{
        default upgrade;
        ''      close;
    }}

    server {{
        listen 80;
        server_name {dockerid}.{url["Domain"]};

        client_max_body_size 5G;
        
        location / {{
            proxy_pass http://127.0.0.1:{proxy_port}/;
            
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

            # WebSocket 설정
            proxy_http_version     1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
            proxy_read_timeout    86400;

        }}
    }}

    server {{
        listen 80;
        server_name {dockerid}.host.{url["Domain"]};

        client_max_body_size 5G;

        location / {{
            proxy_pass http://127.0.0.1:{main_port}/;

            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

            # WebSocket 설정
            proxy_http_version     1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
            proxy_read_timeout    86400;

        }}

    }}
    """

    if url["Proxy_Pass"] == True:
        data = open(f"Data/{dockerid}.mireu.xyz.conf", "w", encoding="utf-8")
        data.write(conf)
        os.system(f"sudo mv Data/{dockerid}.mireu.xyz.conf ../../../../etc/nginx/sites-available/{dockerid}.mireu.xyz.conf")
        sleep(1)
        os.system("sudo service nginx restart")
    else:
        pass

def remove(dockerid):
    os.system(f"sudo rm ../../../../etc/nginx/sites-available/{dockerid}.mireu.xyz.conf")
    sleep(1)
    os.system("sudo service nginx restart")

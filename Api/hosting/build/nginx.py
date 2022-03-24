import os

def upload(dockerid, port):
    conf = f"""map $http_upgrade $connection_upgrade {{
        default upgrade;
        ''      close;
    }}

    server {{
        listen 80;
        server_name {dockerid}.hosting.mireu.xyz;

        location / {{
            proxy_pass http://192.168.0.2:{port};
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
            proxy_set_header X-Scheme $scheme;
            proxy_buffering off;
        }}

        location ~ /.well-known {{
            allow all;
        }}
    }}
    """

    data = open(f"Data/{dockerid}.hosting.mireu.xyz.conf", "w", encoding="utf-8")
    data.write(conf)
    os.system(f"sudo mv Data/{dockerid}.hosting.mireu.xyz.conf ../../../../etc/nginx/sites-available/{dockerid}.hosting.mireu.xyz")
    print(os.system("sudo nginx -t"))
    os.system("sudo service nginx restart")

def remove(dockerid):
    os.system(f"sudo rm ../../../../etc/nginx/sites-available/{dockerid}.hosting.mireu.xyz")
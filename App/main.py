from flask import Flask, request, render_template
from hosting import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main_web():
    if request.method == "GET":
        data = info()
        return render_template('main.html', run_time=data['Data']['run_time'], db=data['Data']['db_program'])

@app.route("/add", methods=["GET","POST"])
def container_add_web():
    if request.method == "GET":
        return render_template('index.html', url="add")
    elif request.method == "POST":
        name = request.form["name"]
        os = request.form["os"]
        data1 = build(name, os)    
        if data1['Data'] == "Container add done":        
            data = status(name)
            return render_template(
                'list.html', 
                name=data['Data']['name'], 
                id=data['Data']['id'], 
                port=data['Data']['port'], 
                os=data['Data']['os'],
                password=data['Data']['token'],
                status=data['Data']['status'], 
                time=data['Data']['time']
            )
        elif data1['Data'] == "Have a container_data with that name":
            return render_template('index.html', url="add", return_data="해당 이름을 가진 컨테이너가 있습니다.")


@app.route("/start", methods=["GET","POST"])
def container_start_web():
    if request.method == "GET":
        return render_template('index.html', url="start")
    elif request.method == "POST":
        name = request.form["name"]
        data = status(name)
        if data['Data'] != 'No container_data':
            if data['Data']["status"] == "start":
                return render_template(
                        'list.html', 
                        name=data['Data']['name'], 
                        id=data['Data']['id'], 
                        port=data['Data']['port'], 
                        os=data['Data']['os'],
                        password=data['Data']['token'],
                        status=data['Data']['status'], 
                        time=data['Data']['time']
                    )
            else:
                data = start(name)
                if data['Data'] == "Update Done":
                    data = status(name)
                    return render_template(
                        'list.html', 
                        name=data['Data']['name'], 
                        id=data['Data']['id'], 
                        port=data['Data']['port'], 
                        os=data['Data']['os'],
                        password=data['Data']['token'],
                        status=data['Data']['status'], 
                        time=data['Data']['time']
                    )
                elif data['Data'] == "No container_data":
                    return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")
        else:
            return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")

@app.route("/stop", methods=["GET","POST"])
def container_stop_web():
    if request.method == "GET":
        return render_template('index.html', url="stop")
    elif request.method == "POST":
        name = request.form["name"]
        data = status(name)
        if data['Data'] != 'No container_data':
            if data['Data']["status"] == "stop":
                return render_template(
                        'list.html', 
                        name=data['Data']['name'], 
                        id=data['Data']['id'], 
                        port=data['Data']['port'], 
                        os=data['Data']['os'], 
                        password=data['Data']['token'],
                        status=data['Data']['status'], 
                        time=data['Data']['time']
                    )
            else:
                data = stop(name)
                if data['Data'] == "Update Done":
                    data = status(name)
                    return render_template(
                        'list.html', 
                        name=data['Data']['name'], 
                        id=data['Data']['id'], 
                        port=data['Data']['port'], 
                        os=data['Data']['os'], 
                        password=data['Data']['token'],
                        status=data['Data']['status'], 
                        time=data['Data']['time']
                    )
                elif data['Data'] == "No container_data":
                    return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")
        else:
            return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")
@app.route("/restart", methods=["GET","POST"])
def container_restart_web():
    if request.method == "GET":
        return render_template('index.html', url="restart")
    elif request.method == "POST":
        name = request.form["name"]
        data = restart(name)
        
        if data['Data'] == "Update Done":
            data = status(name)
        
            return render_template(
                'list.html', 
                    name=data['Data']['name'], 
                    id=data['Data']['id'], 
                    port=data['Data']['port'], 
                    os=data['Data']['os'], 
                    password=data['Data']['token'],
                    status=data['Data']['status'], 
                    time=data['Data']['time']
                )
        elif data['Data'] == "No container_data":
            return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")

@app.route("/remove", methods=["GET","POST"])
def container_remove_web():
    if request.method == "GET":
        return render_template('index.html', url="remove")
    elif request.method == "POST":
        name = request.form["name"]
        data = delete(name)    
        if data['Data'] == "Container delete data done":
            return render_template('index.html', url="remove", return_data="컨테이너가 삭제되었습니다.")
        elif data['Data'] == "container_data has already been deleted":
            return render_template('index.html', url="remove", return_data="해당 이름을 가진 컨테이너가 없습니다.")

@app.route("/info", methods=["GET","POST"])
def container_info_web():
    if request.method == "GET":
        return render_template('index.html', url="info")
    elif request.method == "POST":
        name = request.form["name"]
        data = status(name)
        if data['Data'] != 'No container_data':
            return render_template(
                'list.html', 
                    name=data['Data']['name'], 
                    id=data['Data']['id'], 
                    port=data['Data']['port'], 
                    os=data['Data']['os'],
                    password=data['Data']['token'],
                    status=data['Data']['status'], 
                    time=data['Data']['time']
                )
        elif data['Data'] == 'No container_data':
            return render_template('index.html', url="info", return_data="잘못된 이름")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="81", debug=True)
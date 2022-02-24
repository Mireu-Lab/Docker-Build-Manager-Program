from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
async def main_web():
    if request.method == "GET":
        return render_template('main.html', version = dply.__version__)

@app.route("/add", methods=["GET","POST"])
async def container_add_web():
    if request.method == "GET":
        return render_template('index.html', url="add")
    elif request.method == "POST":
        name = request.form["name"]
        data = dply.container.build(name)    
        if str(data) == "Container add done":        
            data = dply.container.info(name)
            password = dply.container.password(name)
            return render_template(
                'list.html', 
                name=data['name'], 
                id=data['id'], 
                port=data['port'], 
                password=password,
                status=data['status'], 
                time=data['time']
            )
        elif str(data) == "Have a container_data with that name":
            return render_template('index.html', url="add", return_data="해당 이름을 가진 컨테이너가 있습니다.")


@app.route("/start", methods=["GET","POST"])
async def container_start_web():
    if request.method == "GET":
        return render_template('index.html', url="start")
    elif request.method == "POST":
        name = request.form["name"]
        info = dply.container.info(name)
        if info["status"] == "start":
            password = dply.container.password(name)
            return render_template(
                    'list.html', 
                    name=info['name'], 
                    id=info['id'], 
                    port=info['port'], 
                    password=password,
                    status=info['status'], 
                    time=info['time']
                )
        else:
            data = dply.container.start(name)
            if str(data) == "Update Done":
                datainfo = dply.container.info(name)
                password = dply.container.password(name)
                return render_template(
                    'list.html', 
                    name=datainfo['name'], 
                    id=datainfo['id'], 
                    port=datainfo['port'], 
                    password=password,
                    status=datainfo['status'], 
                    time=datainfo['time']
                )
            elif str(data) == "No container_data":
                return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")

@app.route("/stop", methods=["GET","POST"])
async def container_stop_web():
    if request.method == "GET":
        return render_template('index.html', url="stop")
    elif request.method == "POST":
        name = request.form["name"]
        info = dply.container.info(name)
        print(info["status"])
        if info["status"] == "stop":
            password = None
            return render_template(
                    'list.html', 
                    name=info['name'], 
                    id=info['id'], 
                    port=info['port'], 
                    password=password,
                    status=info['status'], 
                    time=info['time']
                )
        else:
            data = dply.container.stop(name)
            if str(data) == "Update Done":
                datainfo = dply.container.info(name)
                password = dply.container.password(name)
                return render_template(
                    'list.html', 
                    name=datainfo['name'], 
                    id=datainfo['id'], 
                    port=datainfo['port'], 
                    password=password,
                    status=datainfo['status'], 
                    time=datainfo['time']
                )
            elif str(data) == "No container_data":
                return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")
        
@app.route("/kill", methods=["GET","POST"])
async def container_kill_web():
    if request.method == "GET":
        return render_template('index.html', url="stop")
    elif request.method == "POST":
        name = request.form["name"]
        info = dply.container.info(name)
        if info["status"] == "start":
            password = dply.container.password(name)
            return render_template(
                    'list.html', 
                    name=info['name'], 
                    id=info['id'], 
                    port=info['port'], 
                    password=password,
                    status=info['status'], 
                    time=info['time']
                )
        else:
            data = dply.container.kill(name)
            if str(data) == "Update Done":
                datainfo = dply.container.info(name)
                password = dply.container.password(name)
                return render_template(
                    'list.html', 
                    name=datainfo['name'], 
                    id=datainfo['id'], 
                    port=datainfo['port'], 
                    password=password,
                    status=datainfo['status'], 
                    time=datainfo['time']
                )
            elif str(data) == "No container_data":
                return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")


@app.route("/restart", methods=["GET","POST"])
async def container_restart_web():
    if request.method == "GET":
        return render_template('index.html', url="restart")
    elif request.method == "POST":
        name = request.form["name"]
        data = dply.container.restart(name)
        
        if str(data) == "Update Done":
            datainfo = dply.container.info(name)
            password = dply.container.password(name)
        
            return render_template(
                'list.html', 
                    name=datainfo['name'], 
                    id=datainfo['id'], 
                    port=datainfo['port'], 
                    password=password,
                    status=datainfo['status'], 
                    time=datainfo['time']
                )
        elif str(data) == "No container_data":
            return render_template('index.html', url="start", return_data="해당 이름을 가진 컨테이너가 없습니다.")

@app.route("/remove", methods=["GET","POST"])
async def container_remove_web():
    if request.method == "GET":
        return render_template('index.html', url="remove")
    elif request.method == "POST":
        name = request.form["name"]
        data = dply.container.remove(name)    
        if str(data) == "Container delete data done":
            return render_template('index.html', url="remove", return_data="컨테이너가 삭제되었습니다.")
        elif str(data) == "container_data has already been deleted":
            return render_template('index.html', url="remove", return_data="해당 이름을 가진 컨테이너가 없습니다.")

@app.route("/info", methods=["GET","POST"])
async def container_info_web():
    if request.method == "GET":
        return render_template('index.html', url="info")
    elif request.method == "POST":
        name = request.form["name"]
        data = dply.container.info(name)
        if type(data) == dict:
            if data['status'] == 'start':
                password = dply.container.password(name)
            else:
                password = None

            return render_template(
                'list.html', 
                name=data['name'], 
                id=data['id'], 
                port=data['port'], 
                password=password,
                status=data['status'], 
                time=data['time']
            )
        elif type(data) == str:
            return render_template('index.html', url="info", return_data="잘못된 이름")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="81", debug=True)

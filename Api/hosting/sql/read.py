import sqlite3

dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
docker_db = dockerdb.cursor()

# 데이터 상태 확인
def status(name):
    sql = """SELECT * FROM Docker_Container WHERE Name={};""".format(name)

    docker_db.execute(sql)

    try:
        result = docker_db.fetchall()
        docker_db.close()
        return result

    except:
        return False


# 도커 ID 데이터 추출
def dockerid(name):
    sql = """SELECT docker_ID FROM Docker_Container WHERE Name={};""".format(name)

    docker_db.execute(sql)
 
    try:
        result = docker_db.fetchall()
        docker_db.close()
        return result

    except:
        return False

# 전체 데이터 추출
def info(name):
    sql = """SELECT docker_ID, name, os FROM Docker_Container WHERE Name={};""".format(name)

    docker_db.execute(sql)
 
    try:
        result = docker_db.fetchall()
        docker_db.close()
        return result

    except:
        return False

def status_bool(name): 
    sql = """SELECT name FROM Docker_Container WHERE Name={};""".format(name)

    try:
        result = docker_db.fetchall()
        docker_db.close()
        return result

    except:
        return False
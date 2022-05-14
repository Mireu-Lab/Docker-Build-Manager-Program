import sqlite3
import json

# 데이터 상태 확인
def status(name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = f"SELECT name, docker_ID, os, status, time FROM Docker_Containers WHERE name='{name}';"
    
    docker_db.execute(sql)
    result = docker_db.fetchall()

    docker_db.close()
    dockerdb.close()

    return {"name":result[0][0], "id":result[0][1], "os":result[0][2], "status":result[0][3], "time":result[0][4]}

# 도커 ID 데이터 추출
def dockerid(name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = f"SELECT docker_ID FROM Docker_Containers WHERE name='{name}';"
    
    docker_db.execute(sql)

    try:
        result = docker_db.fetchall()
        docker_db.close()
        dockerdb.close()

        return result[0][0]

    except:
        return False

# 전체 데이터 추출
def all_info(name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = f"SELECT docker_ID, name, os FROM Docker_Containers WHERE name='{name}';"

    docker_db.execute(sql)

    try:
        result = docker_db.fetchall()
        docker_db.close()
        dockerdb.close()
        return result

    except:
        return False

#컨테이너 확인
def status_bool(name): 
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = f"SELECT COUNT(*) cnt FROM Docker_Containers WHERE name='{name}';"
    
    docker_db.execute(sql)
    re = docker_db.fetchall()
    docker_db.close()
    dockerdb.close()
    if re[0][0] == 1:
        return True
    else:
        return False
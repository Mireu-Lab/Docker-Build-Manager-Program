# -*- coding: utf-8 -*-
import datetime
import sqlite3

# 데이터 추가
def add_data(name, dockerid, port, token, status, os):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()

    sql = """INSERT INTO Docker_Container (name, docker_ID, docker_Port, token, status, os, time) VALUES (?, ?, ?, ?, ?, ?, ?);"""

    docker_db.execute(sql, (name, dockerid, port, token, status, os, datetime.datetime.now()))
    dockerdb.commit()
    docker_db.close()
    dockerdb.close()
    return True

# 데이터 업데이트
def update(status, name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = """UPDATE Docker_Container SET status=?, TIME=? WHERE name=?;"""

    docker_db.execute(sql, (status, datetime.datetime.now(), name))
    dockerdb.commit()
    docker_db.close()
    dockerdb.close()
    return True
    
# 데이터 삭제
def remove(name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = f"""DELETE FROM Docker_Container WHERE name='{name}';"""

    docker_db.execute(sql)
    dockerdb.commit()
    docker_db.close()
    dockerdb.close()
    return True
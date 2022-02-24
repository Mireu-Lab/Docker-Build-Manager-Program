# -*- coding: utf-8 -*-
import datetime
import sqlite3

dockerdb = sqlite3.connect("Data/sql/Hosting_Data.sqlite3")
docker_db = dockerdb.cursor()

# 데이터 추가
def add_data(name, dockerid, port, token, status, os):
    sql = """INSERT INTO Docker_Container (name, docker_ID, docker_Port, token, status, os, time) VALUES (%s, %s, %s, %s, %s, %s, %s);"""

    docker_db.execute(sql, (name, dockerid, port, token, status, os, datetime.datetime.now()))
    dockerdb.commit()
    docker_db.close()
    return True

# 데이터 업데이트
def update(status, name):
    sql = """UPDATE Docker_Container SET Status=%s, TIME=%s WHERE Name=%s;"""

    docker_db.execute(sql, (status, datetime.datetime.now(), name))
    dockerdb.commit()
    docker_db.close()
    return True
    
# 데이터 삭제
def remove(name):
    sql = """DELETE FROM Docker_Container WHERE Name=%s;"""

    docker_db.execute(sql, (name))
    dockerdb.commit()
    docker_db.close()
    return True
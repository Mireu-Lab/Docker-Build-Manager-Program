# -*- coding: utf-8 -*-
import datetime
import sqlite3

# 데이터 추가
def add_data(name, dockerid, status, os, email):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()

    sql = """INSERT INTO Docker_Containers (user_email, name, docker_ID, status, os, time) VALUES (?, ?, ?, ?, ?, ?);"""

    docker_db.execute(sql, (email, name, dockerid, status, os, datetime.datetime.now()))
    dockerdb.commit()
    docker_db.close()
    dockerdb.close()
    return True

# 데이터 업데이트
def update(status, name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = """UPDATE Docker_Containers SET status=?, TIME=? WHERE name=?;"""

    docker_db.execute(sql, (status, datetime.datetime.now(), name))
    dockerdb.commit()
    docker_db.close()
    dockerdb.close()
    return True
    
# 데이터 삭제
def remove(name):
    dockerdb = sqlite3.connect("Data/Hosting_Data.sqlite3")
    docker_db = dockerdb.cursor()
    
    sql = f"""DELETE FROM Docker_Containers WHERE name='{name}';"""

    docker_db.execute(sql)
    dockerdb.commit()
    docker_db.close()
    dockerdb.close()
    return True
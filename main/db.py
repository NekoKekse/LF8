#!/usr/bin/env python3
'''Database Part'''
import sqlite3

def build(databseFile):
    '''Build database and table'''
    con = sqlite3.connect(databseFile)
    cur = con.cursor()

    sqlCreateTable = '''CREATE TABLE IF NOT EXISTS hw (
        date date,
        time time,
        tem_cpu int,
        used_cpu_percent int,
        used_disk_percent int,
        free_disk_gb txt,
        user text,
        connection bool);'''

    cur.execute(sqlCreateTable)

    con.commit()
    con.close()

def add(databseFile, date, time, tem_cpu, used_cpu_percent, used_disk_percent, free_disk_gb, user, connection):
    con = sqlite3.connect(databseFile)
    cur = con.cursor()

    sqlInsert = "INSERT INTO hw (date, time, tem_cpu, used_cpu_percent, used_disk_percent, free_disk_gb, user, connection) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);"

    sqlInsertData = (date, time, tem_cpu, used_cpu_percent, used_disk_percent, free_disk_gb, user, connection)

    cur.execute(sqlInsert, sqlInsertData)

    con.commit()
    con.close()

def remove(databaseFile, date):
    '''Remove object from table'''
    con = sqlite3.connect(databaseFile)
    cur = con.cursor()

    sqlRemove = "DELETE FROM hw WHERE date = ?"

    sqlRemoveData = (date,)
    
    cur.execute(sqlRemove, sqlRemoveData)

    con.commit()
    con.close()

def select(databseFile, date):
    '''Read object from table (selected by date)'''
    con = sqlite3.connect(databseFile)
    cur = con.cursor()

    sqlSelect = "SELECT * FROM hw WHERE date = ?"

    sqlSelectData = (date,)

    cur.execute(sqlSelect, sqlSelectData)

    hwdata = cur.fetchall()

    for data in hwdata:
        print(data)

    con.close()

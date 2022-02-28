import sqlite3

class DB:
    def build(databseFile):
        con = sqlite3.connect(databseFile)
        cur = con.cursor()

        sqlCreateTable = '''CREATE TABLE IF NOT EXISTS hw (
            Datum date,
            Zeit time,
            tem_cpu int,
            used_cpu_percent int,
            used_disk_percent int,
            free_disk_gb double(10, 2),
            user text,
            connection bool);'''

        cur.execute(sqlCreateTable)

        con.commit()
        con.close()

    def add(databseFile, date, time, acpu, aram, anetz, tcpu, max_disk_space, used_disk_space):
        con = sqlite3.connect(databseFile)
        cur = con.cursor()

        sqlInsert = "INSERT INTO hw (Datum, Zeit, CPU_Auslastung, RAM_Auslastung, NetzwerkAuslastung, CPU_Temperatur, RAM_Temperatur, FestplattenSpeicher_Maximal, FestplattenSpeicher_Frei) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"

        sqlInsertData = (date, time, acpu, aram, anetz, tcpu, max_disk_space, used_disk_space)

        cur.execute(sqlInsert, sqlInsertData)

        con.commit()
        con.close()

    def remove(databaseFile, date):
        con = sqlite3.connect(databaseFile)
        cur = con.cursor()

        sqlRemove = "DELETE FROM hw WHERE Datum = ?"

        sqlRemoveData = (date,)
        
        cur.execute(sqlRemove, sqlRemoveData)

        con.commit()
        con.close()

    def select(databseFile, date):
        con = sqlite3.connect(databseFile)
        cur = con.cursor()

        sqlSelect = "SELECT * FROM hw WHERE Datum = ?"

        sqlSelectData = (date,)

        cur.execute(sqlSelect, sqlSelectData)

        hwdata = cur.fetchall()

        for data in hwdata:
            print(data)

        con.close()

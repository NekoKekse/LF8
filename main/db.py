import sqlite3

dbFile = "database.db"

con = sqlite3.connect(dbFile)
cur = con.cursor()

class DB:
    def build():
        sqlCreateTable = '''CREATE TABLE IF NOT EXISTS hw (
            Datum date,
            Zeit time,
            CPU_Auslastung int,
            GPU_Auslastung int,
            RAM_Auslastung int,
            NetzwerkAuslastung int,
            CPU_Temperatur double(10, 2),
            GPU_Temperatur double(10, 2),
            RAM_Temperatur double(10, 2),
            FestplattenSpeicher_Maximal double(10, 2),
            FestplattenSpeicher_Frei double(10, 2));'''

        cur.execute(sqlCreateTable)

        con.commit()

    def add(date, time, acpu, agpu, aram, anetz, tcpu, tgpu, tram, max_disk_space, used_disk_space):
        sqlInsert = "INSERT INTO hw (Datum, Zeit, CPU_Auslastung, GPU_Auslastung, RAM_Auslastung, NetzwerkAuslastung, CPU_Temperatur, GPU_Temperatur, RAM_Temperatur, FestplattenSpeicher_Maximal, FestplattenSpeicher_Frei) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

        sqlInsertData = (date, time, acpu, agpu, aram, anetz, tcpu, tgpu, tram, max_disk_space, used_disk_space)

        cur.execute(sqlInsert, sqlInsertData)

        con.commit()

    def select(date):
        cur.execute("SELECT * FROM hw WHERE Datum = ?", (date,))

        hwdata = cur.fetchall()

        for data in hwdata:
            print(data)

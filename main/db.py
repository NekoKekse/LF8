import sqlite3

class DB:
    def build(databseFile):
        con = sqlite3.connect(databseFile)
        cur = con.cursor()

        sqlCreateTable = '''CREATE TABLE IF NOT EXISTS hw (
            Datum date,
            Zeit time,
            CPU_Auslastung int,
            RAM_Auslastung int,
            NetzwerkAuslastung int,
            CPU_Temperatur double(10, 2),
            FestplattenSpeicher_Maximal double(10, 2),
            FestplattenSpeicher_Frei double(10, 2));'''

        cur.execute(sqlCreateTable)

        con.commit()
        con.close()

    def add(databseFile, date, time, acpu, aram, anetz, tcpu, max_disk_space, used_disk_space):
        con = sqlite3.connect(databseFile)
        cur = con.cursor()

        sqlInsert = "INSERT INTO hw (Datum, Zeit, CPU_Auslastung, RAM_Auslastung, NetzwerkAuslastung, CPU_Temperatur, FestplattenSpeicher_Maximal, FestplattenSpeicher_Frei) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);"

        sqlInsertData = (date, time, acpu, aram, anetz, tcpu, max_disk_space, used_disk_space)

        cur.execute(sqlInsert, sqlInsertData)

        con.commit()
        con.close()

    def select(databseFile, date):
        con = sqlite3.connect(databseFile)
        cur = con.cursor()

        cur.execute("SELECT * FROM hw WHERE Datum = ?", (date,))

        hwdata = cur.fetchall()

        for data in hwdata:
            print(data)

        con.close()

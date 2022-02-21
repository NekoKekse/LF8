import sqlite3

dbfile = "database.db"


# Daten in die Datenbank einfügen
con = sqlite3.connect(dbfile)
cur = con.cursor()
class DB:
    def build():
        cur.execute('''CREATE TABLE IF NOT EXISTS HW (test text)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS SW (test text)''')
        
    def add(table):
        fTable = table.higher()

        cur.execute("INSERT INTO " + fTable + "")

con.commit()
con.close()
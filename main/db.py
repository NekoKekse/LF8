import sqlite3

dbfile = "database.db"

con = sqlite3.connect(dbfile)
cur = con.cursor()
class DB:
    def build():
        cur.execute('''CREATE TABLE IF NOT EXISTS HW (test text)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS SW (test text)''')
        
    def add(table_name, data):
        fTable_name = table_name.higher()
        fData = data.replace('"', '')
        cur.execute("INSERT INTO " + fTable_name + " VALUES " + "(" + str(fData) + ")" )

con.commit()
con.close()
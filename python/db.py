import sqlite3

dbfile = "database.db"

con = sqlite3.connect(dbfile)
cur = con.cursor()

# Datenbank Table erstellen

cur.execute('''CREATE TABLE IF NOT EXISTS HW (test text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS SW (test text)''')

# Daten in die Datenbank einfügen

def add (table, value):
    cur.execute("INSERT INTO str(table) (test) VALUE (?)")

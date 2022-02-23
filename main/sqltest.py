import sqlite3
from db import DB

from datetime import datetime

DB.build()

x = datetime.now()
date = x.strftime("%Y-%m-%d")
time = x.strftime("%H:%M:%S")


print(date)
print(time)

DB.add(str(date), str(time), 1, 2, 3, 4, 5, 6, 7, 8, 9)

con = sqlite3.connect('database.db')
cur = con.cursor()

sqlSelect = "SELECT * FROM hw;"

cur.execute(sqlSelect)

for row in cur:
    print(row[0])
    print(str(row[1])) 

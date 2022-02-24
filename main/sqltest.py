from time import time
from db import DB

filename = 'test.db'

class dbtest():

    def add(date, time):
        DB.build(filename)
        DB.add(filename, str(date), str(time), 1, 2, 3, 4, 5, 6)
    
    def select(date):
        return DB.select(filename, self.date)
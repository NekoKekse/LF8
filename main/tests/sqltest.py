#!/usr/bin/env python3
from time import time
import db

filename = 'test.db'

class dbtest():

    def add(date, time):
        db.build(filename)
        db.add(filename, str(date), str(time), 1, 2, 3, 4, 5, 6)
    
    def select(date):
        return db.select(filename, self.date)
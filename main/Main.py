import sys
from sqltest import dbtest
from datetime import datetime

class mainfunktions():
    def date(self):
        x = datetime.now()
        return x.strftime("%Y-%m-%d")

    def time(self):
        x = datetime.now()
        return x.strftime("%H:%M:%S")

if __name__ == '__main__':
    if len(sys.argv)==1:
        print('normal')
    else:
        print(sys.argv[1])
        if sys.argv[1] == '-L':
            print('Log')
        elif sys.argv[1]=='-D':
            dbtest.add(mainfunktions.date, mainfunktions.time)
            print(dbtest.select(mainfunktions.date))
        else:
            print('''Use: 
-D      Debug Mode
-L      Erstelle Log''')
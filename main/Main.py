from lib2to3.pgen2.token import EQUAL
import sys

if __name__ == '__main__':
    if len(sys.argv)==1:
        print('normal')
    else:
        print(sys.argv[1])
        if sys.argv[1] == '-L':
            print('Log')
        elif sys.argv[1]=='-D' and len(sys.argv)==1:
            print('debug')
        else:
            print('''Use: 
-D      Debug Mode
-L      Erstelle Log''')
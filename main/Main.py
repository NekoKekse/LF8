import sys

if __name__ == '__main__':
    if len(sys.argv)==1:
        print('normal')
    else:
        print(sys.argv[1])
        if sys.argv[1]=='':
            print('normal')
        elif sys.argv[1]=='-L' or '-l':
            print('Log')
        elif sys.argv[1]=='-D' or '-d' and len(sys.argv)==1:
            print('debug')
        else:
            print('Use: -D/-d (Debug Mode)')
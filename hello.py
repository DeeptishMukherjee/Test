import sys


def hello(x):
    print(int(x[1]) + 2)
    print(int(x[1]))
    print('yay1')

if __name__=='__main__':
    hello(sys.argv)

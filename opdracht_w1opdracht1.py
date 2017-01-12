__author__ = 'jer'
import sys


def mymax(a):
    assert( len(a) != 0 ),"len(a) == 0"
    max = 0
    for i in a:
        assert (  type(i) == type(8) or type(i) == type(8.6) ), i
        if i>max:
            max = i
    return max

a = []
b = [10,70,30,"elf",40,50,60]
c = [10,70,30,40,50,60]

try:
    print(mymax(a))
except:
     print(sys.exc_info())

try:
    print(mymax(b))
except:
     print(sys.exc_info())

try:
    print(mymax(c))
except:
     print(sys.exc_info())




# false is error
# true is continue
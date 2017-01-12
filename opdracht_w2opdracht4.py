__author__ = 'jer'

def machtv3(a,n):
    assert n > 0
    m = 1
    while n > 0:
        if n%2 == 0:
            n = n // 2
            a = a * a
        else:
            n = n - 1
            m = m * a
    return m

def myBin(n):
    assert n >= 0
    s = str(n%2)

    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:


        return  myBin(n >> 1) + s


for i in range(0 , machtv3(2,4)):
    print(myBin(i))


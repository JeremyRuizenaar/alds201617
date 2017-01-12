__author__ = 'jer'

def machtv3(a,n):
    assert n > 0
    m = 1
    count = 0

    while n > 0:
        if n%2 == 0:
            n = n // 2
            a = a * a
            count += 1
        else:
            n = n - 1
            m = m * a
            count += 1

    return count, m




print(machtv3(2,10000))

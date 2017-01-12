__author__ = 'jer'
import time
fDict = dict()

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)



def d( n, k):
    return((fac(n)//fac(k))//fac(n-k))

def Z(n, k):
    C = [0 for i in range(k + 1)]
    C[0] = 1

    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j - 1]
            j -= 1
    return C[k]




print("dynamic calculated 1\n")
start = time.clock()
print(Z(100, 50))
end = time.clock()
print(end - start)



print("--------------------"*2)



print("calculated with full fac()\n")
start = time.clock()
print(d(100, 50))
end = time.clock()
print(end - start)


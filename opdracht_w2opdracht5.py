__author__ = 'jer'
import random

count = 0

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]


def qsort(a,low=0,high=-1):
    global count
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
        for j in range(low+1,high+1):
            count+=1

            if a[j] < a[low]:
                m += 1
                swap(a,m,j)


        swap(a,low,m)
        qsort(a,low,m-1)
        qsort(a,m+1,high)



a = [0]*100000
for i in range(100000):
     a[i] = random.randint(0,50000000)
print("a gegenereerd")
print(a[0:10])

qsort(a)
print(a[0:10])
print(count)
count = 0


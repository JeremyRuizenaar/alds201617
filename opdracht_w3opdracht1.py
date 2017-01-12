__author__ = 'jer'
def check(a,i):
    n = len(a)
    return not (i in a or
                i+n in [a[j]+j for j in range(n)] or
                i-n in [a[j]-j for j in range(n)])

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print(a[i], end= " ")
            else:
                print("*", end= " ")
        print()
    print()

def rsearch(N):
    global a
    global b
    for i in range(N):

        if check(a,i):
            a.append(i)

            if len(a) == N:
                b.append(list(a))

            rsearch(N)
            del a[-1] # verwijder laatste element

    return "done"


a = []
b = []
count = 0
rsearch(8)

for u in b:
    print(u)
    #printQueens(u)
    count+=1
print(str(count) + " combinaties mogelijk")









#===========================================================
#
# from itertools import permutations
#
# n=8
# cols = range(n)
# print(cols)
# for vec in permutations(cols):
#     print(vec)
#     if n == len(set(vec[i]+i for i in cols)) \
#          == len(set(vec[i]-i for i in cols)):
#          print (vec )
#


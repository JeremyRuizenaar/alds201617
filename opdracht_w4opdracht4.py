__author__ = 'jer'

def Z(n):
    assert n < 10000
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000,2000,5000,10000]
    w, h = n+1, len(m)
    matrix = [[0 for x in range(w)] for y in range(h)]

    for x in range(h):
        matrix[x][0] = 1

    for j in range(w):
        matrix[0][j] = 1

    for i in range(len(m)):
        for j in range(n+1):
            if j >= m[i]:
                matrix[i][j] = matrix[i-1][j] + matrix [i][j-m[i]]

            if j < m[i]:
                matrix[i][j] = matrix[i-1][j]


    return matrix[len(m)-1][n]



def f(n):

    w, h = n, 10
    matrix = [[0 for x in range(w)] for y in range(h)]

    for x in range(h):
        matrix[x][0] = 1

    for j in range(w):
        matrix[0][j] = 1
    print(matrix)



    assert type(n) == int
    assert n <= 1000
    solutions = [0] + ([0] * n)

    moneys = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

    for money in moneys:
        for i in range(money, n + 1):

            if i == money:
                solutions[i] = 1


            else:
                hold = i - money
                solutions[i] = solutions[hold] + 1




    print(solutions)
    return solutions[n]

print(Z(7))
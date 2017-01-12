__author__ = 'jer'

def getNumbers(s):
    list= []
    firstNumber = 1
    sum = 1
    for ch in s:
        if ch >= '0' and ch <= '9':
            if firstNumber == 1:
                sum *= int (ch)
                firstNumber = 0

            elif firstNumber < 1:
                sum *= 10
                sum += int (ch)

        elif ch < '0' or ch > '9':
            if firstNumber < 1:
                #print(sum)
                list.append(sum)
            firstNumber = 1
            sum = 1

    list.append(sum)
    return list

string = "d11d34bj54k34jb976b54n6b5ikkkk49kk435v0v0v0v0222f03330v444011f011f4g424"
print(getNumbers(string))
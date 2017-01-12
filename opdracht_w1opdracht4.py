__author__ = 'jer'
import random
sum = 0
classesList = []
for x in range(0,100):
         lijst = [random.randrange(1, 366, 1) for x in range(0,23)]
         classesList.append(lijst)

for klas in classesList:
    for student in klas:
        if klas.count(student) > 1:
            print(klas)
            sum+=1
        break

print( sum)

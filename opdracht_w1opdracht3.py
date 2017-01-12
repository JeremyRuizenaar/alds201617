__author__ = 'jer'
import math


def eratosthenesZeef(list):
    for i in list:
        if i > math.sqrt(list[-1]):
            return list
        for x in list[i:]:
            if x%i == 0:
                list.remove(x)







list = [i for i in range (2, 1001)]
print(eratosthenesZeef(list))

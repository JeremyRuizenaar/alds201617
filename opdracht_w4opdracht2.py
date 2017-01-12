__author__ = 'jer'

import random

hashDict = dict()

while(True):
    r = random.random()
    if r not in hashDict.values():
        rh = hash(r) % ( 2 ** 32)
        if rh in hashDict.keys():
            print("hash(" + repr(r) + ") = " +  repr(rh) + " value with same hash : "+ repr(hashDict[rh]))
            break

        hashDict[rh] = r



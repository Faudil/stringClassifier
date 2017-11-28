#!/usr/bin/python3

import sys

def maxLen(array):
    return max([len(e) for e in array])

class Pivot():
    def __init__(self, char, pos=0):
        self._char = char
        self._pos = pos
    def getChar(self):
        return self._char
    def getPos(self):
        return self._pos
    def __str__(self):
        return self.getChar() + " at " + str(self.getPos())
    def test(self, toTest):
        return (len(toTest) > self.getPos() and toTest[self.getPos()] == self.getChar())
    def split(self, array):
        res = [[], []]
        for elem in array:
            if self.test(elem):
                res[0].append(elem)
            else:
                res[1].append(elem)
        return res
    def repartition(self, array):
        nbP = 0
        nbN = 0
        for elem in array:
            if self.test(elem):
                nbP += 1
            else:
                nbN += 1
        return (nbP, nbN)

    def efficiency(self, array):
        f, s = self.repartition(array)
        tt = f + s
        return (tt - (abs(f - s))) / tt

def findSepCrit2(array, firstPos=0):
    # Here I determine a pivot Object
    finalPivot = None
    bestE = 0
    maxL = maxLen(array)
    pos = firstPos
    for i in range (0, maxL):
        tried = []
        for elem in array:
            if len(elem) > pos and elem[pos] not in tried:
                tried.append(elem[pos])
                char = elem[pos]
                pivot = Pivot(char, pos)
                e = pivot.efficiency(array)
#                print(pivot, e)
                if e > bestE:
                    bestE = e
                    finalPivot = pivot
                    if bestE == 1:
                        return finalPivot
        pos += 1
    return finalPivot

def classify(array, maxElemInGrp):
    if len(array) <= maxElemInGrp:
        return
    p = findSepCrit2(array)
    if p != None:
        print(p)
        for sub in p.split(array):
            if len(sub) > maxElemInGrp:
                classify(sub, maxElemInGrp)
            else:
                print(sub)
    else:
        print("No pivot founded in dataset for array :", array)

maxElemInGrp = int(sys.argv[1])
array = sys.argv[2:]
classify(array, maxElemInGrp)

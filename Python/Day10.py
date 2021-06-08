from itertools import groupby
from functools import reduce

inputString = [int(i) for i in open("Day10Input.txt", "r").read().splitlines()]
inputString.sort()
inputString.insert(0, 0)
inputString.append(inputString[len(inputString)-1] + 3)

def countPoss(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return countPoss(n-3)+countPoss(n-2)+countPoss(n-1)

def getDelta():
    delta = [inputString[n]-inputString[n-1] for n in range(1, len(inputString))]
    print(delta.count(1) * delta.count(3))
    return delta

def findCombinations(delta):
    possibilities = [countPoss(len(list(g))) for i, g in groupby(delta) if i == 1]
    print(reduce(lambda x, y: x*y, possibilities))

findCombinations(getDelta())

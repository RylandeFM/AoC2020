inputString = open("Python/Day13Input.txt", "r").read().splitlines()

def partOne():
    timeTable = {int(x) - (int(inputString[0]) % int(x)): int(x) for x in inputString[1].split(",") if x != "x"}
    print(min(timeTable.keys()) * timeTable[min(timeTable.keys())])

def partTwo():
    idList = [(i, int(x)) for i, x in enumerate(inputString[1].split(",")) if x != 'x']
    interval, currTime = idList[0][1], 0
    for delta, period in idList[1:]:
        while (currTime + delta) % period != 0:
            currTime += interval
        interval *= period
    print(currTime)

partOne()
partTwo()

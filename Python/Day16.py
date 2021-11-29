from functools import reduce

inputString = open("Python/Day16Input.txt", "r").read().splitlines()

def getCorrectTickets():
    possibleNumbers, incorrect, correctTickets = set(), [], []
    for line in inputString[:20]:
        for numberRange in line.split(": ")[1].split(" or "):
            possibleNumbers.update(range(int(numberRange.split("-")[0]), int(numberRange.split("-")[1])+1))
    for ticket in inputString[25:]:
        impossibles = [int(x) for x in ticket.split(",") if int(x) not in possibleNumbers]
        if len(impossibles) > 0:
            incorrect.extend(impossibles)
        else:
            correctTickets.append(ticket)
    print(sum(incorrect))
    return correctTickets

def getPossibleRanges():
    possibleNumbers = []
    for line in inputString[:20]:
        currNum = set()
        for numberRange in line.split(": ")[1].split(" or "):
            currNum.update(range(int(numberRange.split("-")[0]), int(numberRange.split("-")[1]) + 1))
        possibleNumbers.append(currNum)
    return possibleNumbers

def getValidRanges(myTicket, validTickets, possibleRanges):
    validRanges = []
    for j in range(0, 20):
        positionSet = {int(x.split(",")[j]) for x in validTickets}
        positionSet.add(int(myTicket.split(",")[j]))
        validSet = set()
        for i in range(0, 20):
            if len(positionSet.difference(possibleRanges[i])) == 0:
                validSet.add(i)
        validRanges.append(validSet)
    return validRanges

def removeFromValidRange(validRanges, validPos):
    updatedList = []
    for possSet in validRanges:
        if validPos in possSet:
            possSet.remove(validPos)
        updatedList.append(possSet)
    return updatedList

def identifyValidPositions(validTickets):
    myTicket = inputString[22]
    possibleRanges = getPossibleRanges()
    validRanges = getValidRanges(myTicket, validTickets, possibleRanges)
    identifiedPositions = [0] * 20
    while sum({len(x) for x in validRanges}) > 0:
        for i, possSet in enumerate(validRanges):
            if len(possSet) == 1:
                validPos = possSet.pop()
                identifiedPositions[validPos] = i
                validRanges = removeFromValidRange(validRanges, validPos)
    print(reduce(lambda x, y: x * y, [int(myTicket.split(",")[identifiedPositions[x]]) for x in range(0, 6)]))

identifyValidPositions(getCorrectTickets())

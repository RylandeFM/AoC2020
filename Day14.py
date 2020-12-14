import itertools as it

inputString = open("Day14Input.txt", "r").read().splitlines()

def applyMask(mask, number, notRelevant):
    relevantMask = [(i, x) for i, x in enumerate(mask[::-1]) if x != notRelevant]
    paddedBin = list(bin(number)[2:].zfill(len(mask))[::-1])
    for swapPos in relevantMask:
        paddedBin[swapPos[0]] = swapPos[1]
    return "".join(paddedBin[::-1])

def getUpdatePositions(mask, memLoc):
    addressList, maskedLoc = [], list(applyMask(mask, memLoc, '0'))
    positions = [i for i, x in enumerate(maskedLoc) if x == 'X']
    for binNumber in it.product(['0', '1'], repeat=maskedLoc.count("X")):
        newNumber = maskedLoc[:]
        for j in range(maskedLoc.count("X")):
            newNumber[positions[j]] = binNumber[j]
        addressList.append("".join(newNumber))
    return addressList

def processInstructions(maskAddress):
    memory, mask = {}, ""
    for line in inputString:
        instr, value = line.split(" = ")
        if instr == "mask":
            mask = value
        else:
            if maskAddress:
                updatePositions = getUpdatePositions(mask, int(instr[4:-1]))
                for pos in updatePositions:
                    memory[pos] = int(value)
            else:
                memory[instr[4:-1]] = int(applyMask(mask, int(value), 'X'), 2)
    print(sum(memory.values()))

processInstructions(False)
processInstructions(True)

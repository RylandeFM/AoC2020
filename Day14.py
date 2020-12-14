import re
from copy import deepcopy

inputString = open("Day14Input.txt", "r").read().splitlines()

def applyMask(mask, number, character):
    relevantMask = [(i, x) for i, x in enumerate(mask[::-1]) if x != character]
    paddedBin = list(bin(number)[2:].zfill(len(mask))[::-1])
    for swap in relevantMask:
        paddedBin[swap[0]] = swap[1]
    return "".join(paddedBin[::-1])

def getUpdatePositions(mask, number):
    addressList, updatedNumber = [], list(applyMask(mask, number, '0'))
    positions = [i for i, x in enumerate(updatedNumber) if x == 'X']
    for i in range(2 ** updatedNumber.count("X")):
        binRepresentation = list(bin(i)[2:].zfill(updatedNumber.count("X")))
        newNumber = deepcopy(updatedNumber)
        for j in range(len(binRepresentation)):
            newNumber[positions[j]] = binRepresentation[j]
        addressList.append(int("".join(newNumber), 2))
    return addressList

def processInstructions(maskAddress):
    memory, mask, updatePositions = {}, "", []
    for line in inputString:
        instr, value = line.split(" = ")
        if instr == "mask":
            mask = value
        else:
            if maskAddress:
                updatePositions = getUpdatePositions(mask, int(re.search(r"\[(.*)]", instr).group(1)))
                for pos in updatePositions:
                    memory[pos] = int(value)
            else:
                memory[int(re.search(r"\[(.*)]", instr).group(1))] = int(applyMask(mask, int(value), 'X'), 2)
    print(sum(memory.values()))

processInstructions(False)
processInstructions(True)

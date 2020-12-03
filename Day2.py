inputString = open("Day2Input.txt", "r").read().splitlines()

def partOne():
    validCount = 0
    for fullEntry in inputString:
        [condition, password] = fullEntry.split(": ")
        [conditionNumbers, conditionLetter] = condition.split(" ")
        [conditionLbound, conditionUbound] = conditionNumbers.split("-")
        if password.count(conditionLetter) >= int(conditionLbound) and password.count(conditionLetter) <= int(conditionUbound): validCount += 1
    print(validCount)

def partTwo():
    validCount = 0
    for fullEntry in inputString:
        [condition, password] = fullEntry.split(": ")
        [conditionNumbers, conditionLetter] = condition.split(" ")
        [conditionpos1, conditionpos2] = conditionNumbers.split("-")
        valCount = 0
        if password[int(conditionpos1) - 1] == conditionLetter: valCount += 1
        if password[int(conditionpos2) - 1] == conditionLetter: valCount += 1
        if valCount == 1: validCount += 1
    print(validCount)

partOne()
partTwo()
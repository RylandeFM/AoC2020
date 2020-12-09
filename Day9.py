inputString = [int(i) for i in open("Day9Input.txt", "r").read().splitlines()]

def partOne(size):
    currentNumbers, matchFound = [], False
    for i in range(size):
        currentNumbers.append(inputString[i])
    for entry in inputString[size:]:
        matchFound = False
        for poss in currentNumbers:
            if entry - poss in currentNumbers and not entry - poss == poss:
                matchFound = True
                break
        if not matchFound:
            return entry
        currentNumbers.pop(0)
        currentNumbers.append(entry)

def partTwo(number):
    start, end, totalSum = 0, 1, 0
    while totalSum != number:
        totalSum = sum(inputString[start:end])
        if totalSum < number:
            end += 1
        elif totalSum > number:
            start += 1
            end = start + 1
        else:
            print(min(inputString[start:end])+max(inputString[start:end]))

weakness = partOne(25)
print(weakness)
partTwo(weakness)

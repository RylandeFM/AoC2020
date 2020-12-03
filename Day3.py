inputString = open("Day3Input.txt", "r").read().splitlines()

def countTrees(step, slope):
    length, xPos, totalCount = len(inputString[0]), 0, 0
    for row in inputString[::step]:
        if row[xPos % length] == "#": totalCount += 1
        xPos += slope
    return totalCount

print(countTrees(1, 3))
print(countTrees(1, 1) * countTrees(1, 3) * countTrees(1, 5) * countTrees(1, 7) * countTrees(2, 1))
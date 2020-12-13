inputString = open("Day12Input.txt", "r").read().splitlines()

directions = ["N", "E", "S", "W"]
translations = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}

def partOne():
    x, y, currDirIdx = 0, 0, 1
    for line in inputString:
        if line[:1] == "L":
            currDirIdx = (currDirIdx - int(int(line[1:]) / 90)) % 4
        elif line[:1] == "R":
            currDirIdx = (currDirIdx + int(int(line[1:]) / 90)) % 4
        elif line[:1] == "F":
            x += translations[directions[currDirIdx]][0] * int(line[1:])
            y += translations[directions[currDirIdx]][1] * int(line[1:])
        else:
            x += translations[line[:1]][0] * int(line[1:])
            y += translations[line[:1]][1] * int(line[1:])
    print(abs(x)+abs(y))

def partTwo():
    x, y, wayX, wayY, currDirIdx = 0, 0, 10, 1, 1
    for line in inputString:
        if line[:1] == "L":
            for i in range(0, int(int(line[1:]) / 90)):
                newX, newY = -wayY, wayX
                wayX, wayY = newX, newY
        elif line[:1] == "R":
            for i in range(0, int(int(line[1:]) / 90)):
                newX, newY = wayY, -wayX
                wayX, wayY = newX, newY
        elif line[:1] == "F":
            x += wayX * int(line[1:])
            y += wayY * int(line[1:])
        else:
            wayX += translations[line[:1]][0] * int(line[1:])
            wayY += translations[line[:1]][1] * int(line[1:])
    print(abs(x) + abs(y))

partOne()
partTwo()

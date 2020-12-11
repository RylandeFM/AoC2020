import copy

inputString = open("Day11Input.txt", "r").read().splitlines()

def addBorderToData(data):
    newList = [['.'] * (len(data[0]) + 2)]
    for line in data:
        newList.append(['.']+list(line)+['.'])
    newList.append(['.'] * (len(data[0]) + 2))
    return newList

def countSeats(x, y, data, countVisible):
    if not countVisible:
        count = sum(line[x-1:x+2].count('#') for line in data[y-1:y+2])
        if data[y][x] == '#': count -= 1
    else:
        count, currX, currY = 0, x, y
        # L
        currX -= 1
        while data[currY][currX] == '.' and currX > 0:
            currX -= 1
        if data[currY][currX] == "#": count += 1
        # R
        currX = x + 1
        while data[currY][currX] == '.' and currX < len(data[0]) - 1:
            currX += 1
        if data[currY][currX] == "#": count += 1
        # U
        currX, currY = x, y - 1
        while data[currY][currX] == '.' and currY > 0:
            currY -= 1
        if data[currY][currX] == "#": count += 1
        # D
        currX, currY = x, y + 1
        while data[currY][currX] == '.' and currY < len(data) - 1:
            currY += 1
        if data[currY][currX] == "#": count += 1
        # LU
        currX, currY = x - 1, y - 1
        while data[currY][currX] == '.' and currX > 0 and currY > 0:
            currX -= 1
            currY -= 1
        if data[currY][currX] == "#": count += 1
        # LD
        currX, currY = x - 1, y + 1
        while data[currY][currX] == '.' and currX > 0 and currY < len(data) - 1:
            currX -= 1
            currY += 1
        if data[currY][currX] == "#": count += 1
        # RD
        currX, currY = x + 1, y + 1
        while data[currY][currX] == '.' and currX < len(data[0]) - 1 and currY < len(data) - 1:
            currX += 1
            currY += 1
        if data[currY][currX] == "#": count += 1
        # RU
        currX, currY = x + 1, y - 1
        while data[currY][currX] == '.' and currX < len(data[0]) - 1 and currY > 0:
            currX += 1
            currY -= 1
        if data[currY][currX] == "#": count += 1
    return count

def updateState(data, threshold, countVisible):
    stable = True
    newData = copy.deepcopy(data)
    for x in range(1, len(data[0])):
        for y in range(1, len(data)):
            if data[y][x] == 'L':
                if countSeats(x, y, data, countVisible) == 0:
                    newData[y][x] = '#'
                    stable = False
            elif data[y][x] == '#':
                if countSeats(x, y, data, countVisible) >= threshold:
                    newData[y][x] = 'L'
                    stable = False
    return newData, stable


def progressLife(countVisible):
    data = addBorderToData(inputString)
    stable = False
    while not stable:
        if countVisible:
            data, stable = updateState(data, 5, countVisible)
        else:
            data, stable = updateState(data, 4, countVisible)
    print(sum(line.count('#') for line in data))

progressLife(False)
progressLife(True)

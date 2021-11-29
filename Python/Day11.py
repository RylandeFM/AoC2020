inputString = open("Python/Day11Input.txt", "r").read().splitlines()

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
        count, operations = 0, [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for op in operations:
            currX, currY = x + op[0], y + op[1]
            while data[currY][currX] == '.' and 0 < currX < len(data[0]) - 1 and 0 < currY < len(data) - 1:
                currX, currY = currX + op[0], currY + op[1]
            if data[currY][currX] == "#": count += 1
    return count

def updateState(data, threshold, countVisible):
    newData, stable = data[:], True
    for x in range(1, len(data[0])):
        for y in range(1, len(data)):
            if data[y][x] == 'L':
                if countSeats(x, y, data, countVisible) == 0:
                    newData[y][x], stable = '#', False
            elif data[y][x] == '#':
                if countSeats(x, y, data, countVisible) >= threshold:
                    newData[y][x], stable = 'L', False
    return newData, stable

def progressLife(countVisible):
    data, stable = addBorderToData(inputString), False
    while not stable:
        if countVisible:
            data, stable = updateState(data, 5, countVisible)
        else:
            data, stable = updateState(data, 4, countVisible)
    print(sum(line.count('#') for line in data))

progressLife(False)
progressLife(True)

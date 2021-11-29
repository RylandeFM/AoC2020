inputString = open("Python/Day24Input.txt", "r").read().splitlines()
transformations = {"e": (1, 0), "w": (-1, 0), "nw": (-1, 1), "ne": (0, 1), "sw": (0, -1), "se": (1, -1), "i": (0, 0)}

def parseLine(line):
    operations = []
    while len(line) > 0:
        currOp = line.pop(0)
        if currOp in ["s", "n"]:
            operations.append(currOp + line.pop(0))
        else:
            operations.append(currOp)
    return operations

def flipTiles():
    flippedTiles = set()
    for line in inputString:
        operations = parseLine(list(line))
        currentCoord = (0, 0)
        for op in operations:
            currentCoord = tuple(map(sum, zip(currentCoord, transformations[op])))
        flippedTiles.remove(currentCoord) if currentCoord in flippedTiles else flippedTiles.add(currentCoord)
    print(len(flippedTiles))
    return flippedTiles

def getNeighbours(tile, inclusive):
    if inclusive:
        return {tuple(map(sum, zip(tile, transformation))) for transformation in transformations.values()}
    else:
        return {tuple(map(sum, zip(tile, transformation))) for key, transformation in transformations.items() if key != "i"}

def progressDays(blackTiles, days):
    for _ in range(days):
        potentialChanges, newBlackTiles = set(), set()
        for tile in blackTiles:
            potentialChanges.update(getNeighbours(tile, True))
        for potential in potentialChanges:
            neighbours = getNeighbours(potential, False)
            if potential in blackTiles:
                if 0 < len(neighbours & blackTiles) < 3: newBlackTiles.add(potential)
            else:
                if len(neighbours & blackTiles) == 2: newBlackTiles.add(potential)
        blackTiles = newBlackTiles
    print(len(newBlackTiles))

progressDays(flipTiles(), 100)

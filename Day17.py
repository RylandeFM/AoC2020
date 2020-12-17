import itertools

inputString = open("Day17Input.txt", "r").read().splitlines()

def parseInput(hyper):
    data = {}
    for i, line in enumerate(inputString):
        for j, character in enumerate(line):
            if hyper:
                if character == '#': data[(j, i, 0, 0)] = "#"
            else:
                if character == '#': data[(j, i, 0)] = "#"
    return data

def getListOfPotentialActives(activeCubes, hyper):
    minX, maxX = min(activeCubes, key=lambda t: t[0])[0], max(activeCubes, key=lambda t: t[0])[0]
    minY, maxY = min(activeCubes, key=lambda t: t[1])[1], max(activeCubes, key=lambda t: t[1])[1]
    minZ, maxZ = min(activeCubes, key=lambda t: t[2])[2], max(activeCubes, key=lambda t: t[2])[2]
    if hyper:
        minW, maxW = min(activeCubes, key=lambda t: t[3])[3], max(activeCubes, key=lambda t: t[3])[3]
        return list(itertools.product(range(minX - 1, maxX + 2), range(minY - 1, maxY + 2), range(minZ - 1, maxZ + 2), range(minW - 1, maxW + 2)))
    else:
        return list(itertools.product(range(minX - 1, maxX + 2), range(minY - 1, maxY + 2), range(minZ - 1, maxZ + 2)))

def countNeighbours(activeCubes, coordinates, translations):
    count = 0
    for translation in translations:
        if tuple(left + right for left, right in zip(coordinates, translation)) in activeCubes: count += 1
        if count > 3: return count
    return count

def bootProcess(hyper):
    activeCubes = parseInput(hyper)
    if hyper:
        neighbourTranslations = list(itertools.product(range(-1, 2), range(-1, 2), range(-1, 2), range(-1, 2)))
        neighbourTranslations.remove((0, 0, 0, 0))
    else:
        neighbourTranslations = list(itertools.product(range(-1, 2), range(-1, 2), range(-1, 2)))
        neighbourTranslations.remove((0, 0, 0))
    for _ in range(0, 6):
        potentialCubes = getListOfPotentialActives(activeCubes, hyper)
        newActive = {}
        for cube in potentialCubes:
            if cube in activeCubes:
                if countNeighbours(activeCubes, cube, neighbourTranslations) in [2, 3]: newActive[cube] = "#"
            else:
                if countNeighbours(activeCubes, cube, neighbourTranslations) == 3: newActive[cube] = "#"
        activeCubes = newActive
    print(len(activeCubes))

bootProcess(False)
bootProcess(True)

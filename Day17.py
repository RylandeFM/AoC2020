import itertools

inputString = open("Day17Input.txt", "r").read().splitlines()

def parseInput(dimensions):
    data = {}
    for y, line in enumerate(inputString):
        for x, character in enumerate(line):
            if character == '#': data[(x, y)+(0,)*(dimensions-2)] = "#"
    return data

def getListOfPotentialActives(activeCubes, dimensions):
    ranges = []
    for i in range(0, dimensions):
        low, high = min(activeCubes, key=lambda t: t[i])[i], max(activeCubes, key=lambda t: t[i])[i]
        ranges.append(list(range(low - 1, high + 2)))
    return list(itertools.product(*ranges))

def countNeighbours(activeCubes, coordinates, translations):
    count = 0
    for translation in translations:
        if tuple(left + right for left, right in zip(coordinates, translation)) in activeCubes: count += 1
        if count > 3: return count
    return count

def getTranslations(dimensions):
    neighbourTranslations = list(itertools.product(range(-1, 2), repeat=dimensions))
    neighbourTranslations.remove((0,)*dimensions)
    return neighbourTranslations

def bootProcess(dimensions):
    activeCubes = parseInput(dimensions)
    neighbourTranslations = getTranslations(dimensions)
    for _ in range(0, 6):
        potentialCubes = getListOfPotentialActives(activeCubes, dimensions)
        newActive = {}
        for cube in potentialCubes:
            if cube in activeCubes:
                if countNeighbours(activeCubes, cube, neighbourTranslations) in [2, 3]: newActive[cube] = "#"
            else:
                if countNeighbours(activeCubes, cube, neighbourTranslations) == 3: newActive[cube] = "#"
        activeCubes = newActive
    print(len(activeCubes))

bootProcess(3)
bootProcess(4)

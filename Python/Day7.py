inputString = open("Day7Input.txt", "r").read().splitlines()
bags, foundBags, containCount = {}, set(), 0

def readInput():
    for line in inputString:
        bags[line.split(" contain ")[0]] = line.split(" contain ")[1]

def findBags(searchString):
    containers = {keys for keys, values in bags.items() if searchString in values}
    if len(containers) > 0:
        foundBags.update(containers)
        for container in containers:
            findBags(container[:-5])

def countContains(searchString, multiplier):
    global containCount
    if bags[searchString] != "no other bags.":
        for subBag in bags[searchString].split(", "):
            containCount += multiplier * int(subBag.split(" ")[0])
            countContains(subBag.split(" bag")[0][2:].strip() + " bags", multiplier * int(subBag.split(" ")[0]))

readInput()
findBags("shiny gold")
print(len(foundBags))
countContains("shiny gold bags", 1)
print(containCount)

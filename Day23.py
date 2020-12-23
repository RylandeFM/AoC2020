inputString = "137826495"

def playRounds(inputCups, iterations):
    numberOfCups = len(inputCups)
    nextCup = [0] * numberOfCups
    for i, v in enumerate(inputCups):
        nextCup[v] = inputCups[(i + 1) % numberOfCups]

    currentCup = inputCups[0]
    for _ in range(iterations):
        pickup1 = nextCup[currentCup]
        pickup2 = nextCup[pickup1]
        pickup3 = nextCup[pickup2]
        cupAfterPickup = nextCup[pickup3]
        destination = (currentCup - 1) % numberOfCups
        while destination == pickup1 or destination == pickup2 or destination == pickup3:
            destination = (destination - 1) % numberOfCups
        nextCup[pickup3] = nextCup[destination]
        nextCup[destination] = pickup1
        nextCup[currentCup] = cupAfterPickup
        currentCup = cupAfterPickup
    return nextCup

def partOne(nextCup):
    answer = ""
    cup = nextCup[0]
    while cup != 0:
        answer += str(cup + 1)
        cup = nextCup[cup]
    print(answer)

def partTwo(nextCup):
    firstCup = nextCup[0]
    secondCup = nextCup[firstCup]
    print((firstCup + 1) * (secondCup + 1))

cups = tuple(int(c) - 1 for c in inputString)  # -1 so we can just use the index
partOne(playRounds(cups, 100))
cups = cups + tuple(range(9, 1000000))
partTwo(playRounds(cups, 10000000))

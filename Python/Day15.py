inputString = open("Python/Day15Input.txt", "r").read().splitlines()
inputString = [int(i) for i in inputString[0].split(",")]

def playMemory(target):
    memory = {x: i for i, x in enumerate(inputString[:-1])}
    lastNumber = inputString[-1]
    for turn in range(len(inputString)-1, target-1):
        currNumber = turn - memory[lastNumber] if lastNumber in memory.keys() else 0
        memory[lastNumber] = turn
        lastNumber = currNumber
    print(lastNumber)

playMemory(2020)
playMemory(30000000)

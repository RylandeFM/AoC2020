inputString = [int(x) for x in open("Day1Input.txt", "r").read().splitlines()]
inputString.sort()

def partOne(total):
    for x in inputString:
        if total - x in inputString:
            print(x * (total - x))
            return

def partTwo(total):
    for x in inputString:
        for y in inputString[1:]:
            if x + y > total:
                break
            if total - x - y in inputString[2:]:
                print(x * y * (total - x - y))
                return

partOne(2020)
partTwo(2020)

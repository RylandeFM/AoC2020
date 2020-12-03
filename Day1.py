inputString = [int(x) for x in open("Day1Input.txt", "r").read().splitlines()]
inputString.sort()

def partOne(sum):
    for x in inputString:
        if sum - x in inputString:
            print(x * (sum-x))
            return

def partTwo(sum):
    for x in inputString:
        for y in inputString[1:]:
            if x + y > sum:
                break
            if sum - x - y in inputString[2:]:
                print(x * y * (sum - x - y))
                return

partOne(2020)
partTwo(2020)
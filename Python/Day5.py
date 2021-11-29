inputString = open("Python/Day5Input.txt", "r").read().splitlines()
seatList = []

def readSeats():
    for scan in inputString:
        seatList.append(int(scan.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0"), 2))
    seatList.sort(reverse=True)

def findSeat():
    for seat in seatList:
        if seat - 2 in seatList and seat - 1 not in seatList: return seat - 1

readSeats()
print(seatList[0])
print(findSeat())

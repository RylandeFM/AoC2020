inputString = open("Python/Day8Input.txt", "r").read().splitlines()
accumulator, swappedPos = 0, set()

def runProgram(skip):
    global accumulator
    pos, hasSwapped, executedPos = 0, False, set()
    while pos not in executedPos:
        instr, value = inputString[pos].split(" ")
        executedPos.add(pos)
        if skip and instr != "acc" and not hasSwapped and pos not in swappedPos:
            hasSwapped = True
            swappedPos.add(pos)
            instr = "nop" if instr == "jmp" else "jmp"
        if instr == "acc": accumulator += int(value)
        pos += int(value) if instr == "jmp" else 1
        if pos >= len(inputString): return True
    return False

runProgram(False)
print(accumulator)
accumulator = 0
while not runProgram(True):
    accumulator = 0
print(accumulator)

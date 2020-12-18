from functools import reduce

inputString = open("Day18Input.txt", "r").read().splitlines()

def solveReducedEquation(equation, priority):
    if priority:
        if '*' in equation:
            return reduce(lambda x, y: eval(str(x)) * eval(str(y)), equation.split("*"))
        else:
            return eval(equation)
    else:
        currentOperation = ''
        total = int(equation.split(" ")[0])
        for c in equation.split(" ")[1:]:
            if c.isnumeric():
                total = eval(str(total) + currentOperation + c)
            else:
                currentOperation = c
        return total

def solveEquation(line, priority):
    while "(" in line:
        subEquation = line[line.find("("):line.find(")")+1]
        if "(" not in subEquation[1:-1]:
            line = line.replace(subEquation, str(solveEquation(subEquation[1:-1], priority)))
        else:
            subEquation = subEquation[subEquation[1:].find("(")+2:subEquation.find(")")]
            line = line.replace("("+subEquation+")", str(solveEquation(subEquation, priority)))
    return solveReducedEquation(line, priority)

def solveLines(priority):
    total = 0
    for line in inputString:
        total += solveEquation(line, priority)
    print(total)

solveLines(False)
solveLines(True)

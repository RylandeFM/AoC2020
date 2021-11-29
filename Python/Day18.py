from functools import reduce

inputString = open("Python/Day18Input.txt", "r").read().splitlines()

def solveReducedEquation(equation, priority):
    if priority:
        if '*' in equation:
            return reduce(lambda x, y: eval(str(x)) * eval(str(y)), equation.split("*"))
        else:
            return eval(equation)
    else:
        equation = equation.split(" ")
        if len(equation) == 3:
            return eval(" ".join(equation))
        else:
            return eval(str(solveReducedEquation(" ".join(equation[:-2]), priority)) + " ".join(equation[-2:]))

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
    print(sum(map(lambda line: solveEquation(line, priority), inputString)))

solveLines(False)
solveLines(True)

inputString = open("Day6Input.txt", "r").read().splitlines()

def readAnswers():
    totalCount, totalP2Count, lineCount, answers = 0, 0, 0, {}
    for line in inputString:
        if line == "":
            totalCount += len(answers)
            totalP2Count += list(answers.values()).count(lineCount)
            answers, lineCount = {}, 0
        else:
            for answer in line:
                if answer in answers.keys():
                    answers[answer] = answers[answer] + 1
                else:
                    answers[answer] = 1
            lineCount += 1
    totalCount += len(answers)
    totalP2Count += list(answers.values()).count(lineCount)
    print(totalCount)
    print(totalP2Count)

def readAnswersSet():
    totalP1Count, totalP2Count, setP1, setP2, newEntry = 0, 0, set(), set(), True
    for line in inputString:
        if line == "":
            totalP1Count += len(setP1)
            totalP2Count += len(setP2)
            newEntry = True
        else:
            if newEntry:
                setP1 = set(line)
                setP2 = set(line)
                newEntry = False
            else:
                setP1.update(set(line))
                setP2.intersection_update(set(line))
    totalP1Count += len(setP1)
    totalP2Count += len(setP2)
    print(totalP1Count)
    print(totalP2Count)


readAnswers()
readAnswersSet()

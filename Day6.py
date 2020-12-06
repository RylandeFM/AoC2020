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

readAnswers()
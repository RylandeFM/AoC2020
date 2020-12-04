import re

inputString = open("Day4Input.txt", "r").read().splitlines()
requiredFields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}

def readPassports():
    passport, validKeysCount, validatedCount = {}, 0, 0
    for line in inputString:
        if line == "":
            if len(requiredFields.intersection(passport.keys())) == len(requiredFields):
                if validatePassport(passport): validatedCount += 1
                validKeysCount += 1
            passport = {}
        else:
            inputs = line.split(" ")
            for kvPair in inputs:
                [key, value] = kvPair.split(":")
                passport[key] = value
    if len(requiredFields.intersection(passport.keys())) == len(requiredFields):
        if validatePassport(passport): validatedCount += 1
        validKeysCount += 1
    print(validKeysCount)
    print(validatedCount)

def validatePassport(passport):
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002: return False
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020: return False
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030: return False
    if re.search("#[0-9a-f]{6}", passport["hcl"]) == None or len(passport["hcl"]) != 7: return False
    if passport["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]: return False
    if re.search("[0-9]{9}", passport["pid"]) == None or len(passport["pid"]) != 9: return False
    if passport["hgt"][-2:] == "cm":
        if int(passport["hgt"].split("cm")[0]) < 150 or int(passport["hgt"].split("cm")[0]) > 193: return False
    elif passport["hgt"][-2:] == "in":
        if int(passport["hgt"].split("in")[0]) < 59 or int(passport["hgt"].split("in")[0]) > 76: return False
    else:
        return False
    return True

readPassports()
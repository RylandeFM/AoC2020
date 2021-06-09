using System;
using System.IO;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Linq;

namespace CSharp
{
    class Day4
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day4Input.txt");
            RunPart1(inputData);
            RunPart2(inputData);
        }

        static void RunPart1(string[] inputData)
        {
            Dictionary<string, string> passport = new();
            int validPassports = 0;
            foreach (string line in inputData)
            {
                if (line == "")
                {
                    validPassports += checkPassport(passport) ? 1 : 0;
                    passport = new();
                }
                else
                {
                    foreach (string item in line.Split(" "))
                    {
                        passport.Add(item.Split(":")[0], item.Split(":")[1]);
                    }
                }
            }
            validPassports += checkPassport(passport) ? 1 : 0;
            Console.WriteLine(validPassports);
        }

        static bool checkPassport(Dictionary<string, string> passport)
        {
            string[] requiredKeys = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
            int presentFields = 0;
            foreach (string reqKey in requiredKeys)
            {
                presentFields += passport.ContainsKey(reqKey) ? 1 : 0;
            }
            return presentFields == requiredKeys.Length;
        }

        static void RunPart2(string[] inputData)
        {
            Dictionary<string, string> passport = new();
            int validPassports = 0;
            foreach (string line in inputData)
            {
                if (line == "")
                {
                    if (checkPassport(passport))
                    {
                        validPassports += validatePassport(passport) ? 1 : 0;
                    }
                    passport = new();
                }
                else
                {
                    foreach (string item in line.Split(" "))
                    {
                        passport.Add(item.Split(":")[0], item.Split(":")[1]);
                    }
                }
            }
            if (checkPassport(passport)) { validPassports += validatePassport(passport) ? 1 : 0; }
            Console.WriteLine(validPassports);
        }

        static bool validatePassport(Dictionary<string, string> passport)
        {
            Regex fourNumbers = new("^\\d{4}$");
            Regex nineNumbers = new("^\\d{9}$");
            Regex hexColor = new("^#[0-9a-f]{6}$");
            Regex heightFormat = new("^\\d{2}in|\\d{3}cm$");
            string[] validColours = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" };

            if (!fourNumbers.IsMatch(passport["byr"]))
            {
                return false;
            }
            else if (int.Parse(passport["byr"]) is < 1920 or > 2002)
            {
                return false;
            }

            if (!fourNumbers.IsMatch(passport["iyr"]))
            {
                return false;
            }
            else if (int.Parse(passport["iyr"]) is < 2010 or > 2020)
            {
                return false;
            }

            if (!fourNumbers.IsMatch(passport["eyr"]))
            {
                return false;
            }
            else if (int.Parse(passport["eyr"]) is < 2020 or > 2030)
            {
                return false;
            }

            if (!heightFormat.IsMatch(passport["hgt"]))
            {
                return false;
            }
            else if (passport["hgt"].Substring(passport["hgt"].Length - 2, 2) == "in")
            {
                if (int.Parse(passport["hgt"][0..^2]) is < 59 or > 76) { return false; }
            }
            else if (passport["hgt"].Substring(passport["hgt"].Length - 3, 3) == "cm")
            {
                if (int.Parse(passport["hgt"][0..^3]) is < 150 or > 193) { return false; }
            }

            if (!hexColor.IsMatch(passport["hcl"])) { return false; }

            if (!validColours.Contains<string>(passport["ecl"])) { return false; }

            if (!nineNumbers.IsMatch(passport["pid"])) { return false; }

            return true;
        }
    }
}

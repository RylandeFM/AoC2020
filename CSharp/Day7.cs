using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace CSharp
{
    class Day7
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day7Input.txt");
            Dictionary<string, string> inputDict = readInputData(inputData);
            RunPart1(inputDict);
            RunPart2(inputDict);
        }

        static Dictionary<string, string> readInputData(string[] inputData)
        {
            Dictionary<string, string> outputDict = new();
            foreach (string line in inputData)
            {
                outputDict[line.Split(" contain ")[0].Trim()] = line.Split(" contain ")[1].Trim();
            }
            return outputDict;
        }

        static void RunPart1(Dictionary<string, string> inputDict)
        {
            HashSet<string> bags = new();
            lookupBag("shiny gold", bags, inputDict);
            Console.WriteLine(bags.Count);
        }

        static void lookupBag(string searchString, HashSet<string> bags, Dictionary<string, string> inputDict)
        {
            IEnumerable<string> result = inputDict.Where(p => p.Value.Contains(searchString)).Select(p => p.Key);
            foreach (string newBag in result)
            {
                bags.Add(newBag[0..^5]);
                lookupBag(newBag[0..^5].Trim(), bags, inputDict);
            }
        }

        static void RunPart2(Dictionary<string, string> inputDict)
        {
            Console.WriteLine(countContains("shiny gold bags", 1, inputDict));
        }

        static long countContains(string keyString, long multiplier, Dictionary<string, string> inputDict)
        {
            long containCount = 0;
            if (inputDict[keyString] != "no other bags.")
            {
                foreach (string subBag in inputDict[keyString].Split(", "))
                {
                    containCount += long.Parse(subBag.Split(" ")[0]) * multiplier;
                    containCount += countContains(subBag[2..].Split("bag")[0].Trim() + " bags", long.Parse(subBag.Split(" ")[0]) * multiplier, inputDict);
                }
            }
            return containCount;
        }
    }
}

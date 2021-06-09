using System;
using System.IO;
using System.Collections.Generic;

namespace CSharp
{
    class Day6
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day6Input.txt");
            RunPart1(inputData);
            RunPart2(inputData);
        }

        static void RunPart1(string[] inputData)
        {
            HashSet<char> answers = new();
            int totalCount = 0;
            foreach (string line in inputData)
            {
                if (line == "")
                {
                    totalCount += answers.Count;
                    answers = new();
                }
                else
                {
                    foreach (char letter in line)
                    {
                        answers.Add(letter);
                    }
                }
            }
            totalCount += answers.Count;
            Console.WriteLine(totalCount);
        }

        static void RunPart2(string[] inputData)
        {
            HashSet<char> answers, groupAnswers = new();
            int totalCount = 0;
            bool newGroup = true;
            foreach (string line in inputData)
            {
                if (line == "")
                {
                    totalCount += groupAnswers.Count;
                    groupAnswers = new();
                    newGroup = true;
                }
                else
                {
                    answers = new();
                    foreach (char letter in line)
                    {
                        if (newGroup)
                        {
                            groupAnswers.Add(letter);
                        }
                        else 
                        {
                            answers.Add(letter);
                        }
                    }
                    if (!newGroup) { groupAnswers.IntersectWith(answers); }
                    newGroup = false;
                }

            }
            totalCount += groupAnswers.Count;
            Console.WriteLine(totalCount);
        }
    }
}

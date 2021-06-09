using System;
using System.IO;
using System.Collections.Generic;

namespace CSharp
{
    class Day5
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day5Input.txt");
            RunPart1(inputData);
        }

        static void RunPart1(string[] inputData)
        {
            List<int> seatNumbers = new();
            foreach (string line in inputData)
            {
                seatNumbers.Add(Convert.ToInt32(line.Replace("F", "0").Replace("B", "1").Replace("L", "0").Replace("R", "1"), 2));
            }
            seatNumbers.Sort();
            seatNumbers.Reverse();
            Console.WriteLine(seatNumbers[0]);
            RunPart2(seatNumbers);
        }

        static void RunPart2(List<int> seatNumbers)
        {
            for (int i = 1; i < seatNumbers.Count - 1; i++)
            {
                if (seatNumbers[i] - seatNumbers[i + 1] > 1)
                {
                    Console.WriteLine(seatNumbers[i] - 1);
                    return;
                }
            }
        }
    }
}

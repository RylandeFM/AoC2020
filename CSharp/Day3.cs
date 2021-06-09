using System;
using System.IO;

namespace CSharp
{
    class Day3
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day3Input.txt");
            RunPart1(inputData);
            RunPart2(inputData);
        }

        static void RunPart1(string[] inputData)
        {
            int currentX = 0, noOfTrees = 0;
            for (int i = 1; i < inputData.Length; i += 1)
            {
                currentX += 3;
                noOfTrees += inputData[i][currentX % inputData[0].Length] == '#' ? 1 : 0;
            }
            Console.WriteLine(noOfTrees);
        }

        static void RunPart2(string[] inputData)
        {
            Console.WriteLine(checkSlopes(inputData, 1, 1) * checkSlopes(inputData, 3, 1) * checkSlopes(inputData, 5, 1) * checkSlopes(inputData, 7, 1) * checkSlopes(inputData, 1, 2));
        }

        static long checkSlopes(string[] inputData, int stepX, int stepY)
        {
            int currentX = 0;
            long noOfTrees = 0;
            for (int i = stepY; i < inputData.Length; i += stepY)
            {
                currentX += stepX;
                noOfTrees += inputData[i][currentX % inputData[0].Length] == '#' ? 1 : 0;
            }
            return noOfTrees;
        }
    }
}

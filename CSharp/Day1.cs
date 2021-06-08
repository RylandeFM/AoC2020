using System;
using System.IO;

namespace CSharp
{
    class Day1
    {
        public static void RunPart1()
        {
            string[] inputData = File.ReadAllLines("../../../Day1Input.txt");
            foreach (string line in inputData)
            {
                Console.WriteLine(line);
            }
        }
    }
}

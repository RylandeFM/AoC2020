using System;
using System.IO;

namespace CSharp
{
    class Day2
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day2Input.txt");
            RunPart1(inputData);
            RunPart2(inputData);
        }

        static void RunPart1(string[] inputData)
        {
            int valid = 0;

            foreach (string line in inputData)
            {
                int lBound, uBound, charCount = 0;
                char character;
                string password;
                lBound = int.Parse(line.Split("-")[0]);
                uBound = int.Parse(line.Split("-")[1].Split(" ")[0]);
                character = char.Parse(line.Split(" ")[1].Split(":")[0]);
                password = line.Split(":")[1];

                foreach (char c in password)
                {
                    if (c == character)
                    {
                        charCount++;
                    }
                }

                if (lBound <= charCount && charCount <= uBound)
                {
                    valid++;
                }
            }

            Console.WriteLine(valid);
        }

        static void RunPart2(string[] inputData)
        {
            int valid = 0;

            foreach (string line in inputData)
            {
                int position1, position2;
                char character;
                string password;
                position1 = int.Parse(line.Split("-")[0]);
                position2 = int.Parse(line.Split("-")[1].Split(" ")[0]);
                character = char.Parse(line.Split(" ")[1].Split(":")[0]);
                password = line.Split(":")[1].Trim();

                if ((password[position1 - 1] == character && password[position2 - 1] != character) || (password[position1 - 1] != character && password[position2 - 1] == character))
                {
                    valid++;
                }
            }

            Console.WriteLine(valid);
        }
    }
}

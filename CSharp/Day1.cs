using System;
using System.IO;

namespace CSharp
{
    class Day1
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day1Input.txt");
            int[] inputNumbers = new int[inputData.Length];
            for (int i = 0; i < inputData.Length; i++)
            {
                inputNumbers[i] = int.Parse(inputData[i]);
            }

            Array.Sort(inputNumbers);

            RunPart1(inputNumbers);
            RunPart2(inputNumbers);
        }

        static void RunPart1(int[] inputNumbers)
        {
            int targetNumber = 2020;

            for (int i = 0; i < inputNumbers.Length; i++)
            {
                for (int j = inputNumbers.Length - 1; j > 0; j--)
                {
                    if (inputNumbers[i] + inputNumbers[j] == targetNumber)
                    {
                        Console.WriteLine(inputNumbers[i] * inputNumbers[j]);
                        return;
                    }

                    if (inputNumbers[i] + inputNumbers[j] < targetNumber)
                    {
                        break;
                    }
                }
            }
        }

        static void RunPart2(int[] inputNumbers)
        {
            int targetNumber = 2020;

            for (int i = 0; i < inputNumbers.Length; i++)
            {
                for (int j = i + 1; j < inputNumbers.Length; j++)
                {
                    if (inputNumbers[i] + inputNumbers[j] > targetNumber)
                    {
                        break;
                    }

                    for (int k = inputNumbers.Length - 1; k > 0; k--)
                    {
                        if (inputNumbers[i] + inputNumbers[j] + inputNumbers[k] == targetNumber)
                        {
                            Console.WriteLine(inputNumbers[i] * inputNumbers[j] * inputNumbers[k]);
                            return;
                        }
                        if (inputNumbers[i] + inputNumbers[j] + inputNumbers[k] < targetNumber)
                        {
                            break;
                        }
                    }
                }
            }
        }
    }
}

using System;
using System.IO;
using System.Collections.Generic;

namespace CSharp
{
    class Day8
    {
        public static void getSolutions()
        {
            string[] inputData = File.ReadAllLines("../../../Day8Input.txt");
            RunPart1(inputData);
            RunPart2(inputData);
        }

        static void RunPart1(string[] inputData)
        {
            HandHeldConsole console = new();
            HashSet<long> visitedIndexes = new();

            while (!visitedIndexes.Contains(console.getProcessIndex()))
            {
                visitedIndexes.Add(console.getProcessIndex());
                console.runCommand(inputData[console.getProcessIndex()]);
            }
            Console.WriteLine(console.getAccumulator());
        }

        static void RunPart2(string[] inputData)
        {
            HashSet<long> swappedPositions = new();
            HandHeldConsole console = new() ;
            bool foundSwap = false;

            while (!foundSwap) {
                console = new();
                HashSet<long> visitedIndexes = new();
                bool hasSwapped = false;

                while (!visitedIndexes.Contains(console.getProcessIndex()) && console.getProcessIndex() < inputData.Length)
                {
                    visitedIndexes.Add(console.getProcessIndex());
                    if (inputData[console.getProcessIndex()].Split(" ")[0] != "acc" && !hasSwapped && !swappedPositions.Contains(console.getProcessIndex()))
                    {
                        string instruction = inputData[console.getProcessIndex()];
                        instruction = instruction.Split(" ")[0] == "nop" ? instruction.Replace("nop", "jmp"): instruction.Replace("jmp", "nop");
                        hasSwapped = true;
                        swappedPositions.Add(console.getProcessIndex());
                        console.runCommand(instruction);
                    }
                    else
                    {
                        console.runCommand(inputData[console.getProcessIndex()]);
                    }
                }

                foundSwap = console.getProcessIndex() >= inputData.Length;
            }
            Console.WriteLine(console.getAccumulator());
        }
    }

    class HandHeldConsole
    {
        private long accumulator;
        private long processIndex;

        public HandHeldConsole()
        {
            accumulator = 0;
            processIndex = 0;
        }

        public long getAccumulator() { return accumulator; }

        private void adjustAccumulator(long amount)
        {
            accumulator += amount;
        }

        public void runCommand(string instruction)
        {
            switch (instruction.Split(" ")[0])
            {
                case "jmp":
                    processIndex += long.Parse(instruction.Split(" ")[1]);
                    break;
                case "nop":
                    processIndex += 1;
                    break;
                case "acc":
                    adjustAccumulator(long.Parse(instruction.Split(" ")[1]));
                    processIndex += 1;
                    break;
            }
        }

        public long getProcessIndex() { return processIndex; }
    }
}

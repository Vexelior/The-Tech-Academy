using System;

namespace Calling_Methods_Assignment
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            Math math = new Math();

            Console.WriteLine("Please input a integer to do some math with.");
            math.Input = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("\nPlease input another integer to do some math with.");
            math.Chosen_Num = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("\nAddition:");
            Console.WriteLine(math.Addition());

            Console.WriteLine("\nSubtraction:");
            Console.WriteLine(math.Subtraction());

            Console.WriteLine("\nMultiplication:");
            Console.WriteLine(math.Multiplication());

            Console.ReadKey();
        }
    }
}
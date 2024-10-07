using System;

namespace Class
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            Math math = new Math();

            Console.WriteLine("Please enter a number.");
            int userInput = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine($"\n{userInput} divided by 2 is:");
            math.Operation(userInput);

            Console.WriteLine("\nOverload method is:");
            math.Operation(userInput, 50);

            Console.WriteLine("\nMethod with output parameters:");
            math.OutMethod(out int i);

            Console.ReadKey();
        }
    }
}
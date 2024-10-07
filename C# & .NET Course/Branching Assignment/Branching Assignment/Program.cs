using System;

namespace Branching_Assignment
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Welcome to Package Express. Please follow the instructions below.");

            Console.WriteLine("Please enter the weight of your package:");
            int weight = Convert.ToInt32(Console.ReadLine());

            if (weight > 50)
            {
                Console.WriteLine("Package too heavy to be shipped via Package Express. Have a good day.");
                Environment.Exit(0);
            }

            Console.WriteLine("Please enter the length of your package:");
            int length = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Please enter the width of your package:");
            int width = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Please enter the height of your package:");
            int height = Convert.ToInt32(Console.ReadLine());

            if (length + width + height > 50)
            {
                Console.WriteLine("Package too big to be shipped via Package Express.");
                Environment.Exit(0);
            }

            double quote = (length * width * height) * weight / 100;

            Console.WriteLine("Your estimated total for shipping this package is: $" + quote.ToString("0.00"));
        }
    }
}

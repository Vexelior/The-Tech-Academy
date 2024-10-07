using System;

namespace Method_Assignment
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            Math math = new Math(); //Instantiate the class.

            //Input 1
            Console.WriteLine("Input a number.");
            math.input1 = Convert.ToInt32(Console.ReadLine()); //Stores the information entered by the user into math.input1

            //Try and catch to mimic skipping the second optional input.
            try
            {
                //Input 2
                Console.WriteLine("\nInput a second number. Press any key to skip.");
                math.input2 = Convert.ToInt32(Console.ReadLine());
            }
            catch (FormatException)
            {
                Console.WriteLine("\nYou have skipped the input.");
                math.input2 = 10;
            }

            //Sum calculation.
            int new_sum = math.Sum(math.input1, math.input2);
            Console.WriteLine("\nSum: " + new_sum);

            //End.
            Console.ReadLine();
        }
    }
}
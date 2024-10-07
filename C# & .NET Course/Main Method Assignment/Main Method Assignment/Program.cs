using System;

namespace Main_Method_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Math math = new Math(); //Instantiate


            //1st equation.
            Console.WriteLine("Please input an integer to feed into the program.");
            //1st user input
            math.integer = Convert.ToInt32(Console.ReadLine());
            //1st Sum
            Console.WriteLine(math.Equation(math.integer));

            //Pause
            Console.ReadLine();


            //2nd equation.
            Console.WriteLine("\nPlease input a decimal to feed into the program.");
            //2nd user input.
            math.dec = (int)Convert.ToDecimal(Console.ReadLine());
            //2nd sum
            Console.WriteLine(math.Equation(math.dec));


            //Pause
            Console.ReadLine();


            //3rd equation
            Console.WriteLine("\nPlease input another integer to feed into the program.");
            //3rd user input
            math.new_int = Convert.ToInt32(Console.ReadLine());
            //3rd sum
            Console.WriteLine(math.Equation(math.new_int));

            //Pause
            Console.ReadLine();

            //End
        }
    }
}

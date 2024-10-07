using System;

namespace Method_Class_Assignment
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Math math = new Math(); //Instantiate the class.

            //Parameters to pass.
            math.input1 = 10;
            math.input2 = 50;

            //Output 1
            Console.WriteLine("Output 1:");
            math.Sum(25, 50); //Passing two numbers.

            //Output 2
            Console.WriteLine("\nOutput 2:");
            math.Sum(input1: 10, input2: 60); //Passing the parameters specified above.

            //End
            Console.ReadLine();
        }
    }
}
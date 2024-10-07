using System;

namespace Method_Class_Assignment
{
    internal class Math
    {
        public int input1 { get; set; } //Grabs the numbers from the main program.
        public int input2 { get; set; }

        public void Sum(int input1, int input2)
        {
            int sum = input1 + 10; //Operation.
            Console.WriteLine(sum); //Write the operation
            Console.WriteLine(input2); //Display second integer.
            return; //Returns the values.
        }
    }
}
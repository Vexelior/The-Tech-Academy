using System;

namespace DateTime_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            //Current time and date to console.
            Console.WriteLine(DateTime.Now);

            //Promp
            Console.WriteLine("Please enter a number.");

            //User input
            int number = Convert.ToInt32(Console.ReadLine());

            //Adds hours the user input to the current time.
            Console.WriteLine(DateTime.Now.AddHours(number));
        }
    }
}

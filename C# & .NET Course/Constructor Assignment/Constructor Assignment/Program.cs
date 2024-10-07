using System;

namespace Constructor_Assignment
{
    public class Program : Person
    {
        static void Main(string[] args)
        {
            Person person = new Person();

            //Constant variable
            const int age = 26;

            //Variable using keyword "var".
            var firstName = "Alex";

            //Print
            Console.WriteLine($"My name is {firstName} and I am {age} years old.");

            //End
            Console.ReadLine();
        }
    }
}

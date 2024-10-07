using System;

namespace Daily_Report_Assingment
{
    class Program
    {
        static void Main()
        {
            //Start of the program displaying welcome message.
            Console.WriteLine("The Tech Academy");

            Console.WriteLine("Student Daily Report");

            //First question
            Console.WriteLine("What is your name?");
            string yourName = Console.ReadLine();

            //Second question
            Console.WriteLine("What course are you on?");
            string course = Console.ReadLine();

            //Third question, converts the typed answer into a boolean value from a string.
            Console.WriteLine("Do you need help with anything? Please answer “true” or “false.”");
            Convert.ToBoolean(Console.ReadLine());

            //Fourth question
            Console.WriteLine("Were there any positive experiences you’d like to share? Please give specifics.");
            string experiences = Console.ReadLine();

            //Fifth question
            Console.WriteLine("Is there any other feedback you’d like to provide? Please be specific.");
            string feedback = Console.ReadLine();

            //Sixth question, converts the typed answer into a byte from a string.
            Console.WriteLine("How many hours did you study today?");
            Convert.ToByte(Console.ReadLine());

            //End of the program displaying exit message.
            Console.WriteLine("Thank you for your answers. An Instructor will respond to this shortly. Have a great day!");
        }
    }
}

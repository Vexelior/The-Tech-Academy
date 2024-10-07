using System;

namespace Parsing_Enums_Assignment
{
    class Program
    {
        //Enum list for days of the week.
        public enum Days
        {
            None,
            Sunday,
            Monday,
            Tuesday,
            Wednesday,
            Thursday,
            Friday,
            Saturday
        }
        static void Main()
        {
            //Prompt
            Console.WriteLine("Enter the curent day of the week.");

            //User input
            string input = Console.ReadLine();
            
            //Instantiation
            Days days;

            //Checks to see if the input is in the list.
            try
            {
                days = (Days)Enum.Parse(typeof(Days),input);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Please enter an actual day of the week."); //Custom error message.
                Console.WriteLine(ex.Message); //Error message from console.

                //Fallback value of none.
                days = Days.None;
            }

            //Check if input is true.
            if (days == Days.Saturday)
            {
                Console.WriteLine("Today is Saturday."); //Output if true.
            }
            else
            {
                Console.WriteLine($"Today is not {input}."); //Output if false.
            }

            //End
            Console.ReadLine();
        }
    }
}

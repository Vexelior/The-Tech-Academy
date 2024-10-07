using System;

namespace Try_Catch_Assignment
{
    public class Program
    {
        private static void Main(string[] args)
        {
            bool validAnswer = false;
            while (!validAnswer)
            {
                try
                {
                    //Start
                    Console.WriteLine("How old are you?");
                    int age = Convert.ToInt32(Console.ReadLine());
                    if (age == 0 || age < 0)
                    {
                        throw new ZeroException();
                    }
                    //Equation for finding the birth year
                    var birthYear = DateTime.Now.Year - age;
                    //Writes the birth year of the user
                    Console.WriteLine(birthYear);
                }
                //Custom exception throw for entering a number less than or equal to zero.
                catch (ZeroException)
                {
                    Console.WriteLine("Please do not enter zero or negative numbers.");
                }
                catch (Exception)
                {
                    Console.WriteLine("An error has occured, please try again.");
                }
                break;
            }
            Console.ReadLine();
        }
    }
}
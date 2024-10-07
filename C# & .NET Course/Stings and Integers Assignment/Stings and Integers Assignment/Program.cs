using System;

using System.Collections.Generic;

namespace Stings_and_Integers_Assignment
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            var numbers = new List<int>();
            numbers.Add(20);
            numbers.Add(30);
            numbers.Add(50);
            numbers.Add(70);

            Console.WriteLine("Please enter a number to divide each number in the list by.");

            try
            {
                //User input
                int div_number = Convert.ToInt32(Console.ReadLine());
                //Loop to iterate through the list and divide by the number entered.
                foreach (int i in numbers)
                {
                    var equation = i / div_number;
                    Console.WriteLine(equation);
                }
            }
            catch (FormatException fm) //Format exception and displays the error message.
            {
                Console.WriteLine(fm.Message);
            }
            catch (DivideByZeroException z) //Divide by zero, throws error message to screen.
            {
                Console.WriteLine(z.Message);
            }
            finally //Write completion message & readline to stop from exiting automatically.
            {
                Console.WriteLine("The try/catch has been completed. Thank you.");
                Console.ReadLine();
            }
        }
    }
}
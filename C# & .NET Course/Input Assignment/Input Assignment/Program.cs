using System;
using System.IO;
using System.Threading.Tasks;

namespace Input_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            //Prompt
            Console.WriteLine("Please enter a number.");

            //User input
            int number = Convert.ToInt32(Console.ReadLine());

            //Writes the user input to a text file
            File.WriteAllText(@"H:/logfile.txt", Convert.ToString(number));

            //Stores the data read from the file into a variable
            string text = File.ReadAllText(@"H:/logfile.txt");

            //Write the data to the console
            Console.WriteLine("Contents of the file: {0}", text);
        }
    }
}

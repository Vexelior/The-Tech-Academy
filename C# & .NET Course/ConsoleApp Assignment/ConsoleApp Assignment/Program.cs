using System;
using System.Collections.Generic;

namespace ConsoleApp_Assignment
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            //Part One
            string[] names = { "Alex", "William", "Bill", "Jessica" };

            Console.WriteLine("\nPlease enter some text.");
            string input = Console.ReadLine();

            for (int i = 0; i < names.Length; i++)
            {
                names[i] += input;
            }

            foreach (string j in names)
            {
                Console.WriteLine("\n" + j);
            }
            Console.ReadLine();
            //End


            //Part Two
            int a = 10;

            while (a == 10)
            {
                Console.WriteLine("A is true.");
                break;
            }
            Console.ReadLine();
            //End


            //Part Three
            while (a < 20)
            {
                Console.WriteLine("A is less then 20");
                break;
            }

            while (a <= 20)
            {
                Console.WriteLine("A is less than or equal to 20");
                break;
            }


            //Part Four
            List<string> strings = new List<string>()
            {
                "Complex",
                "Weird",
                "Example",
                "Execution",
                "New"
            };

            foreach (string option in strings)
            {
                Console.WriteLine(option);
            }

            Console.WriteLine("Enter text to search the list.");

            string search = Console.ReadLine();
            bool found = false;
            foreach (string i in strings)
            {
                if (strings.Contains(search))
                {
                    found = true;
                }
                else
                {
                    Console.WriteLine("Your input is not on the list");
                }
            }

            if (found)
            {
                Console.WriteLine("Your input has been found.");
                int index = strings.IndexOf(search);
                Console.WriteLine("'" + search + "'" + " is index number: " + index + ".");
            }
            Console.ReadLine();
            //End


            //Part Five
            List<string> new_strings = new List<string>
            {
                "List",
                "Algebra",
                "Multiply",
                "List",
                "Subtraction"
            };

            Console.WriteLine("Please select a string from the list.");
            string input_2 = Console.ReadLine();

            for (int i = 0; i < new_strings.Count; i++)
            {
                if (new_strings[i] == input_2)
                {
                    Console.WriteLine("The index of " + input_2 + " is: " + i);
                }
                else
                {
                    Console.WriteLine("Your input is not on the list.");
                }
            }
            //End


            //Part Six
            List<string> titles = new List<string>() { "Junior", "Executive", "Manager", "Junior", "Lead" };
            List <string> dupes = new List<string>();

            foreach (string item in titles)
            {
                Console.WriteLine(item);
                if (dupes.Contains(item))
                {
                    Console.WriteLine(item + " has appeared already.");
                }
                else
                {
                    Console.WriteLine(item + " has not appeared yet.");
                }
                dupes.Add(item);
            }
            Console.ReadLine();
            //End
        }
    }
}
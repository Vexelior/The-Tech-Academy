using System;
using System.Collections.Generic;

namespace Array_Assignment
{
    class Program
    {
        static void Main()
        {
            //Array of Strings
            string[] myStrings = { "This", "Is", "A", "New", "String" };

            //Array of integers
            int[] myInts = { 5, 10, 15, 20, 25 };

            //List of Strings
            List<string> names = new List<string>()
            {
                "Alex",
                "Jessica",
                "Peter",
                "Mike",
                "William"
            };

            //Array of Strings I/O
            //Iterates and prints each string from the list to the console.
            foreach (string i in myStrings)
            {
                Console.WriteLine(i);
            }

            Console.WriteLine("Please select a item from the list. (0-4)");

            int selection1 = int.Parse(Console.ReadLine()); //User input of an integer selects the index of the array.

            //If statement for greater than index in the list, error message and exit application.
            if (selection1 > myStrings.Length - 1)
            {
                Console.WriteLine("That is not a valid selection.");
                Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("You have chosen: " + myStrings[selection1]); //Prints the selection to the console.
            }

            Console.ReadLine();
            //End


            //Array of Ints I/O
            //Iterates and prints each integer from the list to the console.
            foreach (int i in myInts)
            {
                Console.WriteLine(i);
            }

            Console.WriteLine("Please select an number from the list. (0-4)");

            int selection2 = int.Parse(Console.ReadLine()); //User input of an integer selects the index of the array.

            //If statement for greater than index in the list, error message and exit application.
            if (selection2 > myInts.Length - 1)
            {
                Console.WriteLine("That is not a valid selection.");
                Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("You have chosen: " + myInts[selection2]); //Prints the selection to the console.
            }

            Console.ReadLine();
            //End


            //List of strings I/O
            foreach (string i in names)
            {
                Console.WriteLine(i);
            }

            Console.WriteLine("Please select an number from the list. (0-4)");

            int selection3 = int.Parse(Console.ReadLine()); //User input of an integer selects the index of the array.

            //If statement for greater than index in the list, error message and exit application.
            if (selection3 > names.Count - 1)
            {
                Console.WriteLine("That is not a valid selection.");
                Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("You have chosen: " + names[selection3]); //Prints the selection to the console.

            }

            Console.ReadLine();
            //End
        }
    }
}

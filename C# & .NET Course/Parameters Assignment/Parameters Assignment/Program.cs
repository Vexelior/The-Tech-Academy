using System;
using System.Collections.Generic;
using System.Linq;

namespace Parameters_Assignment
{
    public class Program
    {
        static void Main(string[] args)
        {
            //Class Instantiation
            Employee<string> numbers = new Employee<string>();    
            numbers.Things = new List<string>() {"One", "Two", "Three", "Four", "Five"};
            
            Employee<int> integers = new Employee<int>();
            integers.Things = new List<int>() {1, 2, 3, 4, 5};
            
            for (int i = 0; i < numbers.Things.Count(); i++)
            {
                Console.WriteLine(numbers.Things[i] + " and " + integers.Things[i] + ".");
            }
            Console.ReadLine();
        }
    }
}

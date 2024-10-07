using System;
using System.Collections.Generic;

namespace Operators_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            //Instantiation of class.
            Employee employee = new Employee();
            Employee employee1 = new Employee();



            //Employee 1 information.
            employee.FirstName = "Bob";
            employee.LastName = "Jones";
            employee.Id = 0;


            //Employee 2 information.
            employee1.FirstName = "Jessica";
            employee1.LastName = "Williams";
            employee1.Id = 1;


            //Write employee information to the console.
            employee.EmployeeInformation();
            Console.WriteLine("\n"); //Create a new line for a cleaner look.
            employee1.EmployeeInformation();

            //Method call with an if/else statement.
            if (employee.Id == employee1.Id)
            {
                Console.WriteLine("\nThe Employee IDs are the same.");
            }
            else
            {
                Console.WriteLine("\nThe Employee IDs are NOT the same.");
            }

            //Pause
            Console.ReadLine();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;

namespace Operators_Assignment
{
    public class Employee : Person
    {
        public int Id { get; set; }

        public void EmployeeInformation()
        {
            string full_name = FirstName + " " + LastName;
            Console.WriteLine("Full name: " + full_name);
            Console.WriteLine("Employee ID: " + Id);
        }
        
        //Override the equals operator to check and see if the employee ids are the same.
        public static bool operator ==(Employee employee, Employee employee1)
        {
            if (employee.Id.Equals(employee1.Id))
            {
                Console.WriteLine("Overloaded ==");
                return true;
            }
            return false; //Returns false if not the same.
        }

        //Override the is not operator to check if the ids are not the same.
        public static bool operator !=(Employee employee, Employee employee1)
        {
            if (!employee.Id.Equals(employee1.Id))
            {
                Console.WriteLine("Overloaded !=");
                return true;
            }
            return false; //Returns false if they are the same.
        }

        //Override the Equals method
        public override bool Equals(object obj)
        {
            return base.Equals(obj);
        }

        //Override the GetHashCode method
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
    }
}

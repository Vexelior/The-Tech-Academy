using System;

namespace Methods_and_Objects
{
    class Program
    {
        static void Main(string[] args)
        {
            //Instantiation
            Person person = new Person();
            Employee employee = new Employee();

            //New person first and last name to the object 'employee'.
            employee.FirstName = "Sample ";
            employee.LastName = "Student";

            employee.SayName(); //Writes the name to the console.
            
            //End
            Console.ReadLine();
        }
    }
}

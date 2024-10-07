using System;

namespace Abstract_Class
{
    class Program
    {
        static void Main(string[] args)
        {
            //Instantiating the classes.
            Employee employee = new Employee();
            IQuittable quitter = new Employee();
            
            //Object params
            employee.FirstName = "Sample";
            employee.LastName = "Student";

            //Calling the method.
            employee.SayName();

            //Polymorhpism object
            quitter.Quit(employee);

            //End
            Console.ReadLine();
        }
    }
}

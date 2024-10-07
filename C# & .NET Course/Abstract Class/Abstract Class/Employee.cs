using System;
using System.Collections.Generic;
using System.Text;

namespace Abstract_Class
{
    public class Employee : Person, IQuittable
    {
        public override void SayName()
        {
            Console.WriteLine($"{FirstName} {LastName}");
        }
        
        public void Quit(Employee employee)
        {
            Console.WriteLine($"{employee.FirstName} {employee.LastName } has quit!");
        }
    }
}

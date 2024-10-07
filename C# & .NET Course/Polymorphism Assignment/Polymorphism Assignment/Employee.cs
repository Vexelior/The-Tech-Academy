using System;
using System.Collections.Generic;
using System.Text;

namespace Polymorphism_Assignment
{
    class Employee : Person, IQuittable
    {
        public void Quit()
        {
            Console.WriteLine("I quit!");
        }
    }
}

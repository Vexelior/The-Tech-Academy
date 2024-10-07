using System;
using System.Collections.Generic;
using System.Text;

namespace Polymorphism_Assignment
{
    class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public void SayName()
        {
            Console.WriteLine("Student Name: " + FirstName + " " + LastName);
        }
    }
}

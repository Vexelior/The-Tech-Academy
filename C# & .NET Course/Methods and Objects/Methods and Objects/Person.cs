using System;
using System.Collections.Generic;
using System.Text;

namespace Methods_and_Objects
{
    public class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        //Method that writes the first and last name to the console.
        public void SayName()
        {
            Console.WriteLine("Name: " + FirstName + LastName);
        }
    } 
}

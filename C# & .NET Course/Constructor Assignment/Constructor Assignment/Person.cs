using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor_Assignment
{
    public class Person
    {
        public string firstName { get; set; }
        public int age { get; set; }

        public Person()
        {
            //Placeholder for information to pass
        }

        public Person(string firstName)
        : this()
        {
            this.firstName = firstName;
        }

        public Person(string firstName, int age)
        : this(firstName)
        {
            this.age = age;
        }
    }
}

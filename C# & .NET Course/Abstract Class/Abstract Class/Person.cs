using System;
using System.Collections.Generic;
using System.Text;

namespace Abstract_Class
{
    public abstract class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public abstract void SayName();
    }
}

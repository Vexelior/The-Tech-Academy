using System;
using System.Collections.Generic;
using System.Text;

namespace Parameters_Assignment
{
    public class Employee<T>
    {
        public List<T> Things { get; set; }
    }
}

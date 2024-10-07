using System;
using System.Collections.Generic;
using System.Text;

namespace Main_Method_Assignment
{
    class Math
    {
        public int integer { get; set; }
        public int dec { get; set; }
        public int new_int { get; set; }

        public int Equation(int integer)
        {
            return integer * 20; //Returns the sum.
        }

        public decimal Equation(decimal dec)
        {
            return dec * 5; //Returns the sum.
        }

        public string Equation(string new_int)
        {
            return new_int + 50; //Returns the sum.
        }
    }
}

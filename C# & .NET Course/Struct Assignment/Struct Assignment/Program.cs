using System;

namespace Struct_Assignment
{
    //Create the struct
    struct Number
    {
        public decimal Amount; //Property 'Amount' with a decimal data type.
    };
    public class Program
    {
        static void Main(string[] args)
        {
            Number total1; //Declare total1 type.

            total1.Amount = 5.5M; //Assign it a value of decimal.

            Console.WriteLine("Amount #1 : {0}", total1.Amount); //Write to console.

            Console.ReadLine(); //End
        }
    }
}

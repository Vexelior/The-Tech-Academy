using System;

namespace Insurance_Approval_Assignment
{
    class Program
    {
        static void Main()
        {   
            //Question 1
            Console.WriteLine("What is your age?");
            int age = Convert.ToInt32(Console.ReadLine()); //Converts user input into an integer.

            //Question 2
            Console.WriteLine("Have you ever had a DUI?");
            bool dui = Convert.ToBoolean(Console.ReadLine()); //Converts user input 'true' or 'false' into a boolean.

            //Question 3
            Console.WriteLine("How mant speeding tickets do you have?");
            int tickets = Convert.ToInt32(Console.ReadLine()); //Converts user input into an integer.


            //Age Qualify
            bool qual_age = age > 15;
            
            //DUI Qualifiy
            bool qual_dui = dui == false;
            
            //Ticket Qualify
            bool qual_tickets = tickets < 3;

            //Qualification
            bool qualify = qual_age && qual_dui && qual_tickets; //Checks to see if all inputs are meeting the criteria with 'true' or 'false'.

            Console.WriteLine("Qualified?");
            Console.WriteLine(qualify);
            Console.ReadLine();

        }
    }
}

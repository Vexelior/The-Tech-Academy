using System;

namespace MathAndComparisonAssignment
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Anonymous Income Comparison Program");
            Console.ReadLine();

            //Person 1
            Console.WriteLine("Person 1");

            //Person 1: Hourly Rate
            Console.WriteLine("Hourly Rate:");
            int person1_rate = Convert.ToInt32(Console.ReadLine()); //Coverts user input into and integer for calculations later on.
            
            //Person 1: Hours worked per week.
            Console.WriteLine("Hours worked per week:");
            int person1_worked = Convert.ToInt32(Console.ReadLine());
            
            //Person 2
            Console.WriteLine("Person 2");
            
            //Person 2: Hourly Rate
            Console.WriteLine("Hourly Rate");
            int person2_rate = Convert.ToInt32(Console.ReadLine());
            
            //Person 2: Hours worked per week.
            Console.WriteLine("Hours worked per week?");
            int person2_week = Convert.ToInt32(Console.ReadLine());
            
            //Person 1: Annual salary
            Console.WriteLine("Person 1 - Annual salary:");
            int per1_salary = person1_rate * person1_worked * 52; //Times by 52(Number of weeks in a given year)
            Console.WriteLine(per1_salary);
            
            //Person 2: Annual Salary
            Console.WriteLine("Person 2 - Annual Salary:");
            int per2_salary = person2_rate * person2_week * 52; //Times by 52(Number of weeks in a given year)
            Console.WriteLine(per2_salary);
            Console.ReadLine();
            
            //Comparison
            Console.WriteLine("Does Person 1 make more money than Person 2?");
            bool comparison = per1_salary > per2_salary; //True or False depending on user input.
            Console.WriteLine(comparison);
            Console.ReadLine();
        }
    }
}

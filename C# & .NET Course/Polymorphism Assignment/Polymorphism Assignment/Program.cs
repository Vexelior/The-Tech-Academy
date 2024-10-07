using System;

namespace Polymorphism_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Person person = new Person();
            person.FirstName = "Sample";
            person.LastName = "Student";

            person.SayName();

            IQuittable quit = new Employee();
            quit.Quit();

            Console.ReadLine();
        }
    }
}

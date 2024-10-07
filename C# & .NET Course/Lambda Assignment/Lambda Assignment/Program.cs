using System;
using System.Collections.Generic;
using System.Linq;

namespace Lambda_Assignment
{
    internal class Program
    {
        private static void Main()
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { FirstName = "Alex", LastName = "Sanderson", Id = 1 },
                new Employee() { FirstName = "Joe", LastName = "Waltz", Id = 2 },
                new Employee() { FirstName = "William", LastName = "Gonzalez", Id = 3 },
                new Employee() { FirstName = "Paul", LastName = "Myers", Id = 4 },
                new Employee() { FirstName = "Alexandra", LastName = "Sanders", Id = 5 },
                new Employee() { FirstName = "Joe", LastName = "Michaels", Id = 6 },
                new Employee() { FirstName = "Keith", LastName = "Richardson", Id = 7 },
                new Employee() { FirstName = "Sadie", LastName = "Santo", Id = 8 },
                new Employee() { FirstName = "Angus", LastName = "Young", Id = 9 },
                new Employee() { FirstName = "Wesley", LastName = "Morford", Id = 10 }
            };

            List<Employee> JoeEmployees = new List<Employee>();

            Console.WriteLine("Foreach Loop:");
            foreach (Employee employee in employees)
            {
                if (employee.FirstName.Equals("Joe"))
                {
                    JoeEmployees.Add(employee);
                }
            }

            foreach (Employee joes in JoeEmployees)
            {
                Console.WriteLine($"Id: {joes.Id}, First Name: {joes.FirstName}, Last Name: {joes.LastName}");
            }

            Console.WriteLine("\n");

            IEnumerable<Employee> result = (from Employee in employees
                                            where Employee.FirstName.Equals("Joe")
                                            select Employee).ToList();

            Console.WriteLine("LINQ Expression:");
            foreach (Employee joe in result)
            {
                Console.WriteLine($"Id: {joe.Id}, First Name: {joe.FirstName}, Last Name: {joe.LastName}");
            }

            Console.WriteLine("\n");

            Console.WriteLine("Lambda Expression:");
            List<Employee> nameJoe = employees.Where(j => j.FirstName.Equals("Joe")).ToList();

            foreach (Employee m in nameJoe)
            {
                Console.WriteLine($"Id: {m.Id}, First Name: {m.FirstName}, Last Name: {m.LastName}");
            }

            Console.WriteLine("\n");

            Console.WriteLine("Employees whose Ids are greater than five. (Lambda):");
            IEnumerable<Employee> numEmployees = employees.Where(x => x.Id > 5).ToList();

            foreach (Employee k in numEmployees)
            {
                Console.WriteLine($"Id: {k.Id}, First Name: {k.FirstName}, Last Name: {k.LastName}");
            }
            
            Console.ReadLine();
        }
    }
}

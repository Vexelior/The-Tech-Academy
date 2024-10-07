using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace StudentApp
{
    class Program
    {
        static void Main()
        {
            using (var db = new StudentContext())
            {
                Console.WriteLine("Enter the name of the new student.");
                var name = Console.ReadLine();

                Console.WriteLine("\nEnter the date of birth of the new student.");
                var dob = Console.ReadLine();

                Console.WriteLine("\nEnter the Email of the new student.");
                var email = Console.ReadLine();

                var newStudent = new Student { Name = name, Dob = dob, Email = email };

                db.StudentSet.Add(newStudent);
                db.SaveChanges();
            }
        }
    }

    public class Student
    {
        [Key]
        public int StudentId { get; set; }
        public string Name { get; set; }
        public string Dob { get; set; }
        public string Email { get; set; }
    }


    public class StudentContext : DbContext
    {
        public DbSet<Student> StudentSet { get; set; }
    }
}

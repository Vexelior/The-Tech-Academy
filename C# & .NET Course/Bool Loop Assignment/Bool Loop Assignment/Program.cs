using System;

namespace Bool_Loop_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Guess the correct number chosen!");
            Console.WriteLine("Guess a number that is 1-10.");

            int number = Convert.ToInt32(Console.ReadLine());
            bool guess = false;

            do
            {
                switch (number)
                {
                    case 1:
                        Console.WriteLine("You guessed 1. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 2:
                        Console.WriteLine("You guessed 2. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 3:
                        Console.WriteLine("You guessed 3. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 4:
                        Console.WriteLine("That is correct!");
                        guess = true;
                        Environment.Exit(0);
                        break;
                    case 5:
                        Console.WriteLine("You guessed 5. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 6:
                        Console.WriteLine("You guessed 6. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 7:
                        Console.WriteLine("You guessed 7. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 8:
                        Console.WriteLine("You guessed 8. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 9:
                        Console.WriteLine("You guessed 9. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    case 10:
                        Console.WriteLine("You guessed 10. That is incorrect.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                    default:
                        Console.WriteLine("That is not a number 1-10, try again.");
                        Console.WriteLine("Guess a number that is 1-10.");
                        number = Convert.ToInt32(Console.ReadLine());
                        break;
                }
            }
            while (!guess);

            Console.ReadKey();
        }
    }
}

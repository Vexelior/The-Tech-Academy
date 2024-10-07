using System;

namespace Class
{
    internal class Math
    {
        public void Operation(int userInput)
        {                           
            Console.WriteLine((double)userInput / 2);
        }

        public void OutMethod(out int result)
        {
            result = 30;
            Console.WriteLine(result += result);
        }

        public void Operation(int userinput, int result)
        {
            Console.WriteLine(userinput + result);
        }
    }
}
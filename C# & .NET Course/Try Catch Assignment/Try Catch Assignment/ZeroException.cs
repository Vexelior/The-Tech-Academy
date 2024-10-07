using System;

namespace Try_Catch_Assignment
{
    public class ZeroException : Exception
    {
        public ZeroException()
            : base() { }

        public ZeroException(string message)
            : base(message) { }
    }
}
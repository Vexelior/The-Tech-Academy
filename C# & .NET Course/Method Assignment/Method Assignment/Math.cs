namespace Method_Assignment
{
    internal class Math
    {
        public int input1 { get; set; }
        public int input2 { get; set; }

        public int Sum(int input1, int input2 = 10)
        {
            int output = input1 + input2;
            return output;
        }
    }
}
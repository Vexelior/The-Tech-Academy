namespace Calling_Methods_Assignment
{
    public class Math
    {
        public int Input { get; set; }
        public int Chosen_Num { get; set; }

        public int Addition()
        {
            return Input + Chosen_Num;
        }

        public int Subtraction()
        {
            return Input - Chosen_Num;
        }

        public int Multiplication()
        {
            return Input * Chosen_Num;
        }
    }
}
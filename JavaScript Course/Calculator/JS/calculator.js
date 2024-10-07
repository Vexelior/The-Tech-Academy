//Creates an object to keep track of values.
const Calculator = {
  Display_Value: "0",
  First_Operand: null,
  Wait_Second_Operand: false,
  operator: null,
};
//This modifies values each time a button is clicked.
function Input_Digit(digit) {
  const { Display_Value, Wait_Second_Operand } = Calculator;
  if (Wait_Second_Operand === true) {
    Calculator.Display_Value = digit;
    Calculator.Wait_Second_Operand = false;
  } else {
    Calculator.Display_Value =
      Display_Value === "0" ? digit : Display_Value + digit;
  }
}

function Input_Decimal(dot) {
  if (Calculator.Wait_Second_Operand === true) return;
  if (!Calculator.Display_Value.includes(dot)) {
    Calculator.Display_Value += dot;
  }
}
//This section handles operators.
function Handle_Operator(Next_Operator) {
  const { First_Operand, Display_Value, operator } = Calculator
  const Value_of_Input = parseFloat(Display_Value);
  if (operator && Calculator.Wait_Second_Operand) {
    Calculator.operator = Next_Operator;
    return;
  }
  if (First_Operand == null) {
    Calculator.First_Operand = Value_of_Input;
  } else if (operator) {
      const Value_Now = First_Operand || 0;
      let result = Perform_Calculation[operator](Value_Now, Value_of_Input);
      result = Number(result).toFixed(9)
      result = (result * 1).toString()
      Calculator.Display_Value = parseFloat(result);
      Calculator.First_Operand = parseFloat(result);
  }
  Calculator.Wait_Second_Operand = true;
  Calculator.operator = Next_Operator;
}

const Perform_Calculation = {
  '/': (First_Operand, Second_Operand) => First_Operand / Second_Operand,
  '*': (First_Operand, Second_Operand) => First_Operand * Second_Operand,
  '+': (First_Operand, Second_Operand) => First_Operand + Second_Operand,
  '-': (First_Operand, Second_Operand) => First_Operand - Second_Operand,
  '=': (First_Operand, Second_Operand) => Second_Operand
};

function Calculator_Reset() {
  Calculator.Display_Value = "0";
  Calculator.First_Operand = null;
  Calculator.Wait_Second_Operand = false;
  Calculator.operator = null;
}
//Updates the screen with the current contents
function Update_Display() {
  const display = document.querySelector(".calculator-screen");
  display.value = Calculator.Display_Value;
}

Update_Display();
//Monitors key clicks
const keys = document.querySelector(".calculator-keys");
keys.addEventListener("click", (event) => {
  const { target } = event;
  if (!target.matches("button")) {
    return;
  }
  if (target.classList.contains("operator")) {
    Handle_Operator(target.value);
    Update_Display();
    return;
  }
  if (target.classList.contains("decimal")) {
    Input_Decimal();
    Update_Display();
      return;
  }
  //Ensures that AC clears the screen.
  if (target.classList.contains("all-clear")) {
    Calculator_Reset();
    Update_Display();
    return;
  }

  Input_Digit(target.value);
  Update_Display();
})

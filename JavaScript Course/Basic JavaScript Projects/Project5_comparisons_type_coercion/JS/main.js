document.write(typeof 10); //Displays the type of value.

function Zero() {
    document.getElementById('zero').innerHTML = 0/0;
} //Displays NaN because you cannot divide zero by zero.

function True() {
    document.getElementById('true').innerHTML = isNaN('This is not a number');
} //Displays true because a string is not an integer.

function False() {
    document.getElementById('false').innerHTML = isNaN(545);
} //Displays false because when checking if it is not a number, 545 is a number.

document.write(2E310); //Any number above 1.7976931348623157E308 will display infinity. 2E310 is more.

document.write(-3E310); //Displays negative infinity.

document.write(9 > 5); //Displays true with boolean data type.

document.write(10 < 7); //Displays false with boolean data type.

console.log(20 + 34); //Addition operator with console log.

document.write( '2' + 2); //Displays 22, cannot add a string to integer.

console.log(10 > 100); //Addition boolean logic 'false' with console log.

document.write(1000 == 1000); //Equality operator 'true'.

document.write(100 == 1000); //Equality operator 'false'.

t = 1500;
d = 1500;
document.write(t === d); //Scrict equal value and equal types. "True."

f = 'Hello';
h = 'Hello';
document.write(f === h); //"True"

z = '1500';
g = 1500;
document.write(z === g); //"False"

q = 1500;
w = 5600;
document.write(q === w); //End scrict equal value and equal types. "False"

document.write(5 > 1 && 10 > 2); //logical conjunctions. AND OPERATOR
document.write(1 > 5 && 2 > 10);

document.write(20 > 10 || 30 > 20); // Logical conjunction. OR OPERATOR
document.write(10 > 20 || 30 > 50);

function not_Function() {
    document.getElementById("Not").innerHTML = ! (50 > 45);
} // ! Operator, checks is function is false. If so, function will return 'true'.

function not_Function1() {
    document.getElementById("Not1").innerHTML = ! (10 > 15);
} //Double negative with ! operator.
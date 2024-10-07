function addition_Function() {
    var addition = 10 + 5;
    document.getElementById("Math").innerHTML = "10 + 5 = " + addition;
} //Applies math, gives sum using operator

function subtraction_Function() {
    var subtraction = 10 - 5;
    document.getElementById("newMath").innerHTML = "10 - 5 = " + subtraction;
} //Applies math, gives sum using operator

function multiply_Function() {
    var multiply = 10 * 5;
    document.getElementById("mMath").innerHTML = "10 * 5 = " + multiply;
} //Applies math, gives sum using operator

function division_Function() {
    var div = 10 / 5;
    document.getElementById("dMath").innerHTML = "10 / 5 = " + div;
} //Applies math, gives sum using operator

function more_Math() {
    var simple_Math = (10 + 5) * 5 / 10 - 5;
    document.getElementById("moreMath").innerHTML = "10 plus 5, multiplied by 5, divided by 10 and then subtracted by 5 equals " + simple_Math;
} //Applies math, gives sum using operator

function modulus_Operator() {
    var simple_Math = 25 % 6;
    document.getElementById('mod_Math').innerHTML = "When you divide 25 by 6, you have a reaminder of: " + simple_Math;
} //Applies math, gives sum using operator

function negation_Operator() {
    var x = 10;
    document.getElementById('nMath').innerHTML = -x;
} //Applies math, gives sum using operator

var z = 10;
z++;
document.write(z) //Adds 1 to 10 = 11

var e = 20;
e--;
document.write(e) //Subtracts 1 to 21 = 21

window.alert(Math.random() * 200); //Chooses random number from 0 - 200

var t = Math.sqrt(50); //Finds square root of 50
document.write(t);



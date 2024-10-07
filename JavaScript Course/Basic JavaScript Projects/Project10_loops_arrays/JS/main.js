function count_To_Ten() {
    var Digit = "";
    var X = 1;
    while (X < 11) {
        Digit += '<br>' + X;
        X++;
    }
    document.getElementById("Loop").innerHTML = Digit;
}
// While loop that adds one to var Digit as long as it is less than 11 and displays 1-10.

var str = "Hello, World!";
var n = str.length;
document.write(n);
// Displays how many characters there are in the string of var str.

var Instruments = ["Guitar", "Drums", "Piano", "Violin", "Trumpet", "Flute"];
var Content = "";
var Y;
function for_Loop() {
    for (Y = 0; Y < Instruments.length; Y++) {
    Content += Instruments[Y] + "<br>";
    }
    document.getElementById("List_of_Instruments").innerHTML = Content;
}
// A for loop that repeats as long as the original condition is true and displays each strirng in the array until the end.

function cat_pics() {
    var Cat_Picture = [];
    Cat_Picture[0] = "sleeping";
    Cat_Picture[1] = "playing";
    Cat_Picture[2] = "eating";
    Cat_Picture[3] = "purring";
    document.getElementById("Cat").innerHTML = "In this picture, the cat is " + Cat_Picture[2] + ".";
}
// We add an array property to Cat_Picture to select the string that we can add to the output of the function.

function constant_function() {
    const car = {type: "Civic", brand: "Honda", color: "black", speed: "fast"};
    car.color = "pink";
    car.price = "$1500";
    document.getElementById("Constant").innerHTML = "The cost of the " + car.type + " was " + car.price + "." + " The color of the car is " + car.color + "." + " It is also very " + car.speed + ".";
}
// Function consisting of added and over-ridden properties.

var o = 55;
document.write(o);
{
    let o = 78;
    document.write("<br>" + o);
}
document.write("<br>" + o);
// Block scope with the let keyword. 

var t = tFunction(46, 23);
function tFunction(x, y) {
    return x * y;
}
document.getElementById("tFunction").innerHTML = t;
// Takes the parameters from var t and returns the sum that is multiplied back to t.

let myGuitar = {
    make: "Fender ",
    model: "Stratocaster ",
    year: "2001 ",
    color: "red ",
    description : function() {
        return "My guitar is a " + myGuitar.year + myGuitar.color + myGuitar.make + myGuitar.model;
    }
};
document.getElementById("guitar").innerHTML = myGuitar.description();
// Creats the object of myGuitar and returns the attibutes created into a string.

var text = "";
var j;
for (j = 0; j < 21; j++) {
    if (j === 20) { break; }
    text += "The number is " + j + "<br>";
}
document.getElementById("break").innerHTML = text;
// This breaks the loop and continues executing the code after the loop.

var text_2 = "";
var h;
for (h = 0; h < 21; h++) {
    if (h === 10) { continue; }
    text_2 += "The number is " + h + "<br>";
}
document.getElementById("continue").innerHTML = text_2;
// A loop with a continue statement that skips the number 10 in the loop.


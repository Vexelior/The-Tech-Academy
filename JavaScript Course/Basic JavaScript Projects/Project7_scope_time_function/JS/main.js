var z = 100;
function Add_1() {
    document.write(z + 50 + '<br>');
}
function newFunction_1() {
    document.write(z + 500 + '<br>');
}
Add_1();
newFunction_1();
// Global variable, not inside the function.

function Add_2() {
    var p = 20;
    document.write(p + 200 + '<br>');
}
function newFunction_2() {
    document.write(p + 250);
}
Add_2();
newFunction_2();
// Local variable, inside the function. Var p is not defined.

function Add_3() {
    var p = 20;
    console.log(15 + p);
}
function newFunction_3() {
    console.log(p + 100);
}
Add_3();
newFunction_3();
// No result shown in the browser, open console and 'p' is not defined.

function get_Date() {
    if (new Date().getHours() > 12) {
        document.getElementById('Greeting').innerHTML = 'Good evening.';
    }
}
// If the time is greater than 12, displays 'Good evening'.

if (score > 10000) {
    call = 'You rock!';
} else {
    call = 'You suck!';
}
// If score is greater than 10,000, the variable call displays 'You rock!' otherwise, it displays 'You suck!'. 

function Age_Function() {
    Age = document.getElementById('Age').value;
    if (Age >= 17) {
        Movie = 'You are old enough to view this movie.'
    }
    else {
        Movie = 'You are not old enough to view this movie.'
    }
    document.getElementById('What_is_your_age?').innerHTML = Movie;
}
// if else statement in regards to seeing an r-rated movie.

function Time_Function() {
    var Time = new Date().getHours();
    var Reply;
    if (Time < 12 == Time >0) {
        Reply = 'It is the morning time!';
    }
    else if (Time > 12 == Time < 18) {
        Reply = 'It is the afternoon.';
    }
    else {
        Reply = 'It is the evening time.';
    }
    document.getElementById('Time_of_day').innerHTML = Reply;
}
// Pulls the local time from your device to display what time of the day it is.


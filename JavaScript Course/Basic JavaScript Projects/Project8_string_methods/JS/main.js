function full_Sentence() {
    var part_1 = 'RuneScape is ';
    var part_2 = 'the coolest ';
    var part_3 = 'game to play ';
    var part_4 = 'on the computer.';
    var whole_sentence = part_1.concat(part_2, part_3, part_4);
    document.getElementById('Concatenate').innerHTML = whole_sentence;
}
// Takes the strings from each variable called and puts them into an entire sentence.

function slice_Method() {
    var Sentence = 'All glory to Bandos!';
    var Section = Sentence.slice(13,20);
    document.getElementById('Slice').innerHTML = Section;
}

var word = 'Hello, World!';
var upperWord = word.toUpperCase();
document.write(upperWord);
// Makes the string in the variable 'word' and converts the text to uppercase.

var newWord = "Welcome to RuneScape";
var g = newWord.search('RuneScape');
document.write(g);
// Searches within the string to find the word 'RuneScape' from the newWord variable.

function string_Method() {
    var x = 523;
    document.getElementById('Num_to_string').innerHTML = x.toString();
}
// Converts the value of 523 to a string value, '523'.

function precision_Method() {
    var u = 15413.122346234;
    document.getElementById('Precision').innerHTML = u.toPrecision(10);
}
// Formats a number to the specified length which here is 10. (15413.12235)

var num = 3.4756
var n = num.toFixed(2);
document.write(n);
//Converts the number into a string, rounding the number to keep only two decimals.

var newTry = 123;
var d = newTry.valueOf();
document.write(d);
// Returns the original value of the var newTry.
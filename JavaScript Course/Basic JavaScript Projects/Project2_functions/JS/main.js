function myFunction () {
    var str = 'This is the string.';
    var result = str.fontcolor('blue');
    document.getElementById('Blue_Text').innerHTML = result;
} //Button to display string in blue text

function newFunction() {
    var sentence = 'I like to learn';
    sentence += ' JavaScript!';
    document.getElementById('new').innerHTML = sentence;
} //This displays a new paragraph with an onclick function to display the strings
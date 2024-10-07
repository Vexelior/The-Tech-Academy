function Vote_Function() {
    var Age, Can_Vote; // Variable consists of two calls, Age & Can_vote.
    Age = document.getElementById("Age").value;
    Can_Vote = (Age < 18) ? "You are too young":"You are old enough"; //Displays string whether less or greater than 18.
    document.getElementById("Vote").innerHTML = Can_Vote + " to vote.";
} // Displays data on page.

// Class/object created.
function Vehicle(Make, Model, Year, Color) {
    this.Vehicle_Make = Make;
    this.Vehicle_Model = Model;
    this.Vehicle_Year = Year;
    this.Vehicle_Color = Color;
} 
// Instances of the previously created class using keyword.
var Jack = new Vehicle("Dodge", "Viper", 2020, "Red");
var Emily = new Vehicle("Jeep", "Trail Hawk", 2019, "White and Black");
var Erik = new Vehicle("Ford", "Pinto", 1971, "Mustard");
// Execution function to call the instance of the new data.
function myFunction() {
    document.getElementById("Keywords_and_Constructors").innerHTML = 
    "Erik drives a " + Erik.Vehicle_Color + "-colored " + Erik.Vehicle_Model + 
    " manufactured in " + Erik.Vehicle_Year;
}
// Displays data on page.

function Person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
}
var new_Person = new Person('Alex', 'Sanderson', 25, 'Green'); //Declaring the instance.
function pFunction() {
    document.getElementById("New_and_This").innerHTML = "My name is " + new_Person.firstName + " " + new_Person.lastName + ", I am "
    + new_Person.age + " " + "years old and, I have " + new_Person.eyeColor + " eyes.";
} //Displays the new attributes from the insance.


// Makes the id the Count() and adds the next value from the next nested function as one entire function.
function add_Function() {
    document.getElementById('Nested_Function').innerHTML = Count(); 
    function Count() {
        var Start = 20;
        function Add_one() {Start += 100;}
        Add_one();
        return Start;
    }
}

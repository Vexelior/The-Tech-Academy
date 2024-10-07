function food_function() {
    var Food_Output;
    var foods = document.getElementById("food_input").value;
    var Food_String = " is a great food!";
    switch (foods) {
        case "Pizza":
            Food_Output = "Pizza" + Food_String;
        break;
        case "Sushi":
            Food_Output = "Sushi" + Food_String;
        break;
        case "Burger":
            Food_Output = "Burger" + Food_String;
        break;
        case "Chicken":
            Food_Output = "Chicken" + Food_String;
        break;
        case "Steak":
            Food_Output = "Steak" + Food_String;
        break;
        case "Sandwich":
            Food_Output = "Sandwich" + Food_String;
        break;
        default:
        Food_Output = "Please enter a food exactly as written on the list above.";
    }
    document.getElementById("output").innerHTML = Food_Output;
}
// Creates the output needed for when the user types in their answer from the list.

function Hello_World_Function() {
    var A = document.getElementsByClassName("Click");
    A[0].innerHTML = "The text has changed!";
}
// Changes the text according to the placement of the ID which is [0].

var c = document.getElementById("ID_Name");
var ctx = c.getContext("2d");
var grd = ctx.createLinearGradient (0, 0, 500, 250);

grd.addColorStop(0, "black");
grd.addColorStop(1, "white");

ctx.fillStyle = grd;
ctx.fillRect(50, 50, 400, 150);
ctx.strokeRect(50, 50, 400, 150);
// Creates a rectangle inside the canvas.


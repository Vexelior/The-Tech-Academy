//Form validation function
function validateForm() {
    var x = document.forms["myForm"]["Name"].value;
    if (x == "") {
        alert("Please fill out the required information");
        return false;
    }
}

//Popup Form function
function openForm() {
    document.getElementById('Login').style.display = "block";
}

function closeForm() {
    document.getElementById('Login').style.display = "none";
}
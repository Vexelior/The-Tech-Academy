function my_Dictionary() {
    var Car = {
        Model: 'Volkswagen',
        Color: 'White',
        Sub_Model: 'Bug',
        Age: 5,
        Sound: 'Honk!'
    }; //Object for a car
    delete Car.Sound; //Deleted the function property 'Sound: 'Honk!';
    document.getElementById('Dictionary').innerHTML = Car.Sound;
}

function new_Dictionary() {
    var Animal = {
        Type: 'Bird',
        Color: 'Red',
        Age: 2,
        Sound: 'Chirp!'
    }; //Second object to compare.
    document.getElementById('nDictionary').innerHTML = Animal.Sound;
}
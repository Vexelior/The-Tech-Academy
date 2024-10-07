function countdown() {
    var seconds = document.getElementById('seconds').value;

    function tick() {
        seconds = seconds -1;
        timer.innerHTML = seconds;
        setTimeout(tick, 1000);
    if(seconds == -1) {
        alert('Time is up!');
    }
        }
    tick();    
}
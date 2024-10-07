const dropdownMenu = document.querySelector(".dropdown-menu");
const button = document.getElementById("dropdownMenuButton");

$(button).click(function () {
    $(dropdownMenu).css("width", $(button).outerWidth());
});

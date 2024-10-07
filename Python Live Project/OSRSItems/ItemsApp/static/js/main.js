$(document).ready(function () {
    // Back to top button. \\
    var topButton = document.getElementsByClassName("top")[0];
    $(window).scroll(function () {
        if ($(window).scrollTop() > 300) {
            $(topButton).addClass('show');
        } else {
            $(topButton).removeClass('show');
        }
    });

    $(topButton).on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, '300');
    });

    // Alert messages. \\
    $(".alert").fadeTo(2000, 500).slideUp(500, function () {
        $(".alert").slideUp(1000);
    });

    var alerts = document.getElementById("alerts");
    if (alerts == null) {
        return;
    } else {
        alerts.style.width = "100%";
        alerts.style.position = "fixed";
        alerts.style.top = "0";
        alerts.style.zIndex = "1000";
        alerts.style.margin = "0";
        alerts.style.left = "0";
        alerts.style.textAlign = "center";
    }

    // Dropdown menu. \\
    $(".dropdown").hover(
        function () {
            $('.dropdown-menu', this).stop(true, true).fadeIn("fast");
            $(this).toggleClass('open');
            $('b', this).toggleClass("caret caret-up");
        },
        function () {
            $('.dropdown-menu', this).stop(true, true).fadeOut("fast");
            $(this).toggleClass('open');
            $('b', this).toggleClass("caret caret-up");
        }
    );
});

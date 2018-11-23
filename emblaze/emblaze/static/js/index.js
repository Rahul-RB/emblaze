$(document).ready(function() {
    var mainText = $("#mainText").offset().top;
    var topNavbar = $("#top-navbar").offset().top;

    var mainTextReached = false;
    var topNavbarReached = false;

    $(window).on("scroll", function(event) {

        if ($(window).scrollTop() >= topNavbar && !topNavbarReached) {
            console.log("made it 1");
            topNavbarReached = true;
        }

        if ($(window).scrollTop() >= mainText) {
            console.log("made it 2");
            mainTextReached = true;
        }
        if(topNavbarReached && mainTextReached)
        {
            $(window).off("scroll");
        }
    });
});
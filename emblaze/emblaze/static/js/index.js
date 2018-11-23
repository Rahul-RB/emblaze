$(document).ready(function() {
    var mainText = $("#mainText").offset().top;
    var topNavbar = $("#top-navbar").offset().top;

    var mainTextReached = false;
    var topNavbarReached = false;

    $(window).on("scroll", function(event) {

        if ($(window).scrollTop() >= topNavbar && !topNavbarReached) {
            console.log("made it 1");
            topNavbarReached = true;
            $.ajax({
                url: 'getAboutContents',
                type: 'GET',
            })
            .done(function(data) {
                console.log("<GET-1:>success",data);
                $("#about").append(data["content"]);
                // var imageUrl = "{{ url_for('static',filename='img/about4.jpg') }}";
                var imageUrl = 'static/img/about4.jpg';
                $("#back1").css("background-image", "url(" + imageUrl + ")");
            })
            .fail(function() {
                console.log("error");
            })
            .always(function() {
                console.log("complete");
            });
        }

        if ($(window).scrollTop() >= mainText) {
            console.log("made it 2");
            mainTextReached = true;
            $.ajax({
                url: 'getClientContents',
                type: 'GET',
            })
            .done(function(data) {
                console.log("<GET-2:>success",data);
                $("#clients").append(data["content"]);
                // var imageUrl = "{{ url_for('static',filename='img/about4.jpg') }}";
                var imageUrl = "static/img/background2.jpg";
                $("#back2").css("background-image", "url(" + imageUrl + ")");
            })
            .fail(function() {
                console.log("error");
            })
            .always(function() {
                console.log("complete");
            });
        }
        if(topNavbarReached && mainTextReached)
        {
            $(window).off("scroll");
        }
    });
});
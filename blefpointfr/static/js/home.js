jQuery(function() {
    "use strict";

    $('nav ul a li').on('mouseenter', function(event) {
        var color =  $(this).attr('class');

        $('.single_page .' + color).css('top', '0px');
    }).on('mouseleave', function(event) {
        var color =  $(this).attr('class');

        $('.single_page .' + color).css('top', '-10px');
    });
});
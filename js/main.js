$('document').ready(function () {
    var listHeight = 180;
    (function () {
        var h = $('.tab__item__content').first().height();
        $('.tab__list').css('height', h + listHeight);
    })();

    $('.tab__item__inner').on('click', function (e) {
        e.preventDefault();
        if(!$(this).hasClass('on')) {
            $('.tab__item__inner').removeClass('on');
            var h = $(this).next().height();
            $('.tab__list').css('height', h + listHeight);
            $(this).toggleClass('on');
        }
    });

    $('body').toggleClass(function() {
        if(isMobileDevice()) {
            return 'm';
        }
    });

    function isMobileDevice(){
        return (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent) ? true : false);
    }
});

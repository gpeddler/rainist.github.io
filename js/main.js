$('document').ready(function () {
    var listHeight = 50;
    (function () {
        var h = $('.tap__item__content').first().height();
        $('.tap__list').css('height', h + listHeight);
    })();

    $('.tap__item__inner').on('click', function (e) {
        e.preventDefault();
        if(!$(this).hasClass('on')) {
            var h = $(this).next().height();
            $('.tap__list').css('height', h + listHeight);
            $('.tap__item__inner').toggleClass('on');
        }
    });
});
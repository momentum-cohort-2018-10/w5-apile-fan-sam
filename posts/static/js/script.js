function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');



$('.voting i').off().on('click', function() {
    var box = $(this).closest('.container');
    var postSlug = $(this).attr('name');
    var vote = $(this).hasClass("fa-caret-up");

    $.ajax({
        type: "POST",
        data: {
            "vote": vote,
            'csrfmiddlewaretoken': csrftoken
        },
        url: `/posts/${postSlug}/vote`,
        dataType: "json"})
        .done(function(response) {
            if (response[0] === "success") {
                $(`.voting p[name*=${postSlug}]`).html(response[1]);
            } else {
                $('.notification').detach();
                $(box).prepend(`<div class="notification is-primary">
                ${response[1]}
              </div>`);
            }

        }).fail(function(rs, e) {
            console.log(rs.responseText);
        });
})
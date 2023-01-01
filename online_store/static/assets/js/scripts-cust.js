$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});


$(document).on("click", ".btn_narrow", function(e) {
    e.preventDefault()
    let form = $('#filter_product')
    $.ajax({
        type: form.attr('method'),
        url: form.action,
        data: form.serialize(),
        success: function(data) {
            // console.log(data)
            // history.pushState(null, null, 'start')
            $('.Card').remove()
            $("div.Cards").append(data);
            // window.addEventListener('popstate', function(e) {
            //     window.history.back() 
            // })
        }
    })
})

$(document).on("click", ".btn_default", function(e) {
    e.preventDefault()
    let link = $(this)
    $.ajax({
        type: 'GET',
        url: link.attr("href"),
        data: {'tag': link.html()},
        success: function(data) {
            $('.Card').remove()
            $("div.Cards").append(data);
        }
    })
    history.pushState(null, null, link.attr("href"))
})

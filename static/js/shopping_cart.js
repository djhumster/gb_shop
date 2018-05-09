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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$().ready(function() {
    var csrftoken = getCookie('csrftoken');
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.cart-list').on('click', 'input[type="number"]', function(e) {
        var t_href = e.target;

        $.ajax({
            type: 'POST',
            url: '/cart/edit/',
            data: {
                pk: t_href.name,
                quantity: t_href.value
            },

            success: function(data) {
                $('.cart-list').html(data.result);
                var quant = $('#cart-quantity-bottom').text();
                $('.cart-quantity-top').text(quant);
            },
        });

        e.preventDefault();
    });

    $('.cart-list').on('click', '.remove-btn', function(e) {
        var t_href = e.target;

        $.ajax({
            type: 'POST',
            url: '/cart/remove/',
            data: {
                pk: t_href.name
            },

            success: function(data) {
                $('.cart-list').html(data.result);
                var quant = $('#cart-quantity-bottom').text();
                $('.cart-quantity-top').text(quant);
            },
        });

        e.preventDefault();
    });
});
  
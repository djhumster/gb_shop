window.onload = function() {
    $('.cart-list').on('click', 'input[type="number"]', function(e) {
        var t_href = e.target;

        $.ajax({
            url: "/cart/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function(data) {
                $('.cart-list').html(data.result);
            },
        });

        e.preventDefault();
    });
    $('.cart-list').on('click', '.remove-btn', function(e) {
        var t_href = e.target;

        $.ajax({
            url: "/cart/remove/" + t_href.name + "/",

            success: function(data) {
                $('.cart-list').html(data.result);
            },
        });

        e.preventDefault();
    });
}
  
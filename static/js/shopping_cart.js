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
}
  
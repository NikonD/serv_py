function load_page(page) {
    jQuery.ajax({
        type:'POST',
        url: '/load',
        data: page,
        dataType: "html",
        success: function(respose) {
            var html_temp = jQuery.parseHTML(response)
            $('.content').html(html_temp);
        }
    });
}
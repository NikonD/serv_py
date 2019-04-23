/**
 * Created with PyCharm.
 * User: Администратор
 * Date: 23.04.19
 * Time: 15:02
 * To change this template use File | Settings | File Templates.
 */

function signup() {
    jQuery.ajax({
        type: 'POST',
        url:  '/signup',
        data: 'login='+$('#login').val()+'&password='+$('#password').val()+'&privileges='+$('#privileges').val(),
        dataType: 'html',
        success: function(response) {
            var html_temp = jQuery.parseHTML(response);
            $('body').html(html_temp);
        }
    });
}
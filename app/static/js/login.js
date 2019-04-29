/**
 * Created with PyCharm.
 * User: NekoNikon
 * Date: 09.04.19
 * Time: 14:05
 * To change this template use File | Settings | File Templates.
 **/


function get_key() {
    ckey = Math.round(Math.random() * Math.pow(10, 16));
    alert(ckey);
    return ckey;
}

function load_login() {
    jQuery.ajax({
        type: 'POST',
        url: '/load_login',
        dataType: 'html',
        success: function(response) {
            console.log(response);
            var html_temp = jQuery.parseHTML(response);
            $('#body').html(html_temp);
        }
    });
}

function login() {
   jQuery.ajax({
        type: 'POST',
        url: '/login',
        data: 'login='+$('#login').val()+'&password='+$('#password').val()+'&ckey='+SHA256(get_key().toString()),
        dataType: 'html',
        success: function(response) {
            var html_temp = jQuery.parseHTML(response);
            $('#body').html(html_temp);
        }
    });

}
function logout() {
    jQuery.ajax({
        type:   'POST',
        url:    '/exit',
        dataType: 'html',
        success: function(response) {
            var html_temp = jQuery.parseHTML(response);
            $('#body').html(html_temp);
        }
    });
}

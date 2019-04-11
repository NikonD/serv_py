/**
 * Created with PyCharm.
 * User: NekoNikon
 * Date: 09.04.19
 * Time: 14:05
 * To change this template use File | Settings | File Templates.
**/

function get_key() {
    var ckey = Math.round(Math.random()*Math.pow(10,16));
    alert(ckey);
    jQuery.ajax({
        url: '/gen_key',
        type:'GET',
        data: 'key='+ckey,
        success: function(response) {
            alert('cool');
        }
    });
}

function login() {
    var pass = $('#password').val();
    alert(pass);
    jQuery.ajax({
        url:'/login',
        type:'GET',
        data: $('#login-form').serialize(),
        dataType: 'html',
        success: function(response) {
            var html_temp = jQuery.parseHTML(response)
            $('.content').html(html_temp);
        }
    });
}

//$(document).ready(function() {
    $('#sbt').click(function(){
        get_key();
        login();
    });
//});




//$(document).ready(function(){
//    alert('dsd');
//  $('#btn_sbt').click(function() {
//     jQuery.ajax({
//        type: "POST",
//        url: "/login",
//        data: $('form').serialize(),
//        dataType: "html",
//        success: function(response) {
//          var html_temp = jQuery.parseHTML(response)
//          $('.content').html(html_temp);
//        },
//        error: function(error) {
//          console.log(error);
//        }
//      });
//  });
//});
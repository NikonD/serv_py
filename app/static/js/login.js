/**
 * Created with PyCharm.
 * User: NekoNikon
 * Date: 09.04.19
 * Time: 14:05
 * To change this template use File | Settings | File Templates.
**/

function login() {
    jQuery.ajax({
        url:'/login_ajax',
        type:'POST',
        data: $('#login-form').serialize(),
        dataType: 'html',
        success: function(response) {
            var html_temp = jQuery.parseHTML(response)
            $('.content').html(html_temp);

        }
    });
}




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
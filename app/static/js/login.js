
//$('#sbt').click(function() {
////    var XHR = new XMLHttpRequest();
////    XHR.onreadystatechange = function() {
////        if (this.readyState == 4 && this.status == 200) {
////            document.getElementById(".content").innerHTML = this.responseXML;
////        }
////    };
////    XHR.open('POST' , '/login');
////    XHR.send();
//    get_key();
//    login();
//
//});
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

function login() {
   jQuery.ajax({
        type: 'POST',
        url: '/login',
        data: 'login='+$('#login').val()+'&password='+$('#password').val()+'&ckey='+SHA256(get_key().toString()),
        dataType: 'html',
        success: function(response) {
            console.log(response);
            var html_temp = jQuery.parseHTML(response);
            $('body').html(html_temp);
        }
    });

}

function login_gen() {
    login();
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

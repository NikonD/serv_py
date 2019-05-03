/**
 * Created with PyCharm.
 * User: NekoNikon
 * Date: 03.05.19
 * Time: 9:59
 * To change this template use File | Settings | File Templates.
 */

function load_group_indicators() {
    jQuery.ajax({
        type: 'POST',
        url: '/load_group_inds',
        dataType:'html',
        success: function (response) {
            var html_temp = jQuery.parseHTML(response);
            $('#body').html(html_temp);
        }
    });
}
function load_indicators() {
    jQuery.ajax({
        type: 'POST',
        url: '/load_inds',
        dataType:'html',
        data: 'select='+$('#select_inds').val(),
        success: function (response) {
            var html_temp = jQuery.parseHTML(response);
            $('#ind').html(html_temp);
//            console.log(response)
//           $('#ind').html(response);
        }
    });
}

function add_group_inds() {
    jQuery.ajax({
        type: 'POST',
        url : '/add_group_inds',
        dataType: 'json',
        data: 'name_group_ind='+$('#nameind').val(),
        success: function(response) {
            console.log(response);
            load_group_indicators();
        }
    })
}

function del_group_inds() {
    jQuery.ajax({
        type: 'POST',
        url : '/del_group_inds',
        dataType: 'json',
        data: 'ind_group_id='+$('#ind_id').val(),
        success: function(response) {
            console.log(response);
            load_group_indicators();
        }
    })
}

function add_inds() {
    jQuery.ajax({
        type: 'POST',
        url : '/add_inds',
        dataType: 'json',
        data: 'select='+$('#select_inds').val()+'&name='+$('#text_name_ind').val(),
        success: function(response) {
            console.log(response);
            load_indicators();
        }
    })
}

function del_inds() {
    jQuery.ajax({
        type: 'POST',
        url : '/del_inds',
        dataType: 'json',
        data: 'ind_id='+$('#text_id_ind').val(),
        success: function(response) {
            console.log(response);
            load_indicators();
        }
    })
}
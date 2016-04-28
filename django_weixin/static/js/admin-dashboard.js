/**
 * Created by fengxiaolong on 16/4/15.
 */
$().ready(function () {
    var post_data = "";
    $("#create-meibo-menu").click(function(){
        $.ajax({
            url: '/django-weixin/api/create/menu/',
            data: JSON.stringify(post_data),
            type: 'POST', contentType: 'application/json', dataType: 'json',
            beforeSend: function (xhr, o) {
                xhr.setRequestHeader("X-CSRFToken", getCookieValue('csrftoken'));
            }
        })
        .done(function (data) {
        })
        .fail(function (data) {
        })
        .always(function (data) {
        })
    });
    $("#delete-meibo-menu").click(function(){
        $.ajax({
            url: '/django-weixin/api/delete/menu/',
            data: JSON.stringify(post_data),
            type: 'POST', contentType: 'application/json', dataType: 'json',
            beforeSend: function (xhr, o) {
                xhr.setRequestHeader("X-CSRFToken", getCookieValue('csrftoken'));
            }
        })
        .done(function (data) {

        })
        .fail(function (data) {
        })
        .always(function (data) {
        })
    });
});
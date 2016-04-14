/**
 * Created by fengxiaolong on 16/4/12.
 */
$(function () {
});

function confirm_button_click() {
    var final_string = "";
    var menu_1_array = new Array();
    var menu_2_array = new Array();
    var menu_3_array = new Array();
    var name_1_array = new Array();
    var name_2_array = new Array();
    var name_3_array = new Array();
    var type_1_array = new Array();
    var type_2_array = new Array();
    var type_3_array = new Array();
    for (i = 1; i < 16; i++) {
        if (i < 6) {
            name_1_array.push($("#name_" + i).val());
            menu_1_array.push($("#sub_" + i).val());
            type_1_array.push($("#st_" + i).val());
        }
        if (i > 5 && i < 11) {
            name_2_array.push($("#name_" + i).val());
            menu_2_array.push($("#sub_" + i).val());
            type_2_array.push($("#st_" + i).val());
        }
        if (i > 10) {
            name_3_array.push($("#name_" + i).val());
            menu_3_array.push($("#sub_" + i).val());
            type_3_array.push($("#st_" + i).val());
        }
    }
    var main_menu_1 = $("#main-menu-first").val();
    var main_menu_2 = $("#main-menu-second").val();
    var main_menu_3 = $("#main-menu-third").val();
    var final_json_string = {
        "menu_1": [
            {
                "menu_title": $("#main-menu-first-name").val(),
                "menu_content": main_menu_1,
                "menu_type": $("#menu_1_type").val()
            },
            {
                "child_menu_title": name_1_array,
                "child_menu_content": menu_1_array,
                "menu_type": type_1_array
            }
        ],
        "menu_2": [
            {
                "menu_title": $("#main-menu-second-name").val(),
                "menu_content": main_menu_2,
                "menu_type": $("#menu_2_type").val()
            },
            {
                "child_menu_title": name_2_array,
                "child_menu_content": menu_2_array,
                "menu_type": type_2_array
            }
        ],
        "menu_3": [
            {
                "menu_title": $("#main-menu-third-name").val(),
                "menu_content": main_menu_3,
                "menu_type": $("#menu_3_type").val()
            },
            {
                "child_menu_title": name_3_array,
                "child_menu_content": menu_3_array,
                "menu_type": type_3_array
            }
        ]
    };
    //console.log(menu_1_array);
    //console.log(menu_2_array);
    //console.log(menu_3_array);
    console.log(final_json_string);
    var post_data = final_json_string;
    $.ajax({
            url: '/django-weixin/basic/menu/create/',
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
}

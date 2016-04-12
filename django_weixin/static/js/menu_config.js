/**
 * Created by fengxiaolong on 16/4/12.
 */
$(function () {
    generate_create_menu_json();
});

function generate_create_menu_json() {
    var final_string = "";
    for (i = 1; i < 16; i++) { 
        final_string += $("sub_" + i).val();
    }
}

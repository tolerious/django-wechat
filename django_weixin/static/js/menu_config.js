/**
 * Created by fengxiaolong on 16/4/12.
 */
$(function () {
});

function confirm_button_click() {
    var final_string = "";
    var final_array = new Array();
    for (i = 1; i < 16; i++) {
        final_array.push($("#sub_" + i).val());
    }
    console.log(final_array);
}

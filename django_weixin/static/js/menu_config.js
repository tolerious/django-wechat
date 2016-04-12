/**
 * Created by fengxiaolong on 16/4/12.
 */
$(function () {
});

function confirm_button_click() {
    var final_string = "";
    for (i = 1; i < 16; i++) {
        final_string  =  $("#sub_" + i).val() + ",";
        console.log($("#sub_"+i).val());
    }
    console.log(final_string);
}

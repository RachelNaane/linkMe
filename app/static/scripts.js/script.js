$("form[name=register_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/register",
        type: "POST",
        data: data,
        success: function(resp) {
            console.log(resp);
        },
        error: function(resp) {
            console.log(resp)
            $error.text(resp.responseJSON.error).removeClass("error--hidden")
        }
    });

    e.preventDefaoult();
});
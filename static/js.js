$(document).ready(function(){
    $("#submit").click(function(){
        var values = {};
        $.each($('#formio').serializeArray(), function(i, field) {
            values[field.name] = field.value;
        });
        var code = $("textarea#code").val();
        var args = $("textarea#args").val();
        values['code'] =code;
        values['args'] =args;
        $.ajax({
            type: "POST",
            url : "",
            dataType:"json",
            data: values,
            beforeSend: function(){
                $(".out").addClass("hidden");
                $("#loader").removeClass("hidden");
            },
            success: function(data){
                data = data['response'];
                console.log(data);
                $("#push").html(data);
                $("#loader").addClass("hidden");
                $(".out").removeClass("hidden");
            }

        });
    });
});
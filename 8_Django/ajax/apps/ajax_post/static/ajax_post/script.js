$(document).ready(function(){
    $.ajax({
        url: "notes/",
        success: function(response){
            $("#placeholder1").html(response)
        },
    })
    $('#create_form').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            method: 'POST',
            data: $(this).serialize(),
            success: function(response){
                $("#placeholder1").html(response)
            },
        })
        return false;
    });
});
$(document).ready(function(){
    $.ajax({
        url: "notes/",
        success: function(response){
            $("#placeholder1").html(response)
            console.log("try")
        }
        });
    console.log("Document Ready")
    $.ajaxSetup({
        headers: { "X-CSRFToken": '{{csrf_token}}' }
      });
    $('#delete').click(function(e){
        console.log("clicked")
        $("#notes_form").submit()
        return false;
    });
    $("#notes_form").submit(function(e){
        console.log("submitted")
        $.ajax({
            method: "POST",
            beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRF-TOKEN", "${_csrf.token}");
            },
            url: "delete/",
            data : $(this).serialize(),
            success : function(e){
                $("#placeholder1").html("/notes")
            }
        });
        return false;
    });
});
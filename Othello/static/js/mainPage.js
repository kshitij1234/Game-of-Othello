$(document).ready(function(){
    $(" #tok").addClass("hidden");
    $(" #sub").addClass("hidden");
    $("#join_game").click(function(){
        $(" #tok").removeClass("hidden");
        $(" #sub").removeClass("hidden");
        $(" #sub").addClass("btn btn-info");
    });
    $("#sub").click(function(){
        var token=$("#tok").val();
        var url_mask = window.location.href+"game/"+token;
        window.location=url_mask;
    })
});
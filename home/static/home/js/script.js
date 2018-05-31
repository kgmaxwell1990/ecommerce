

    $("#empty_heart_form").mouseenter(function(){
        
        $("#tooltip").css("display", "inline-block")
        $("#tooltip_remove").css("display", "inline-block")
    });
    $("#empty_heart_form").mouseleave(function(){
        $("#empty_heart_icon").addClass("far fa-heart fa-2x");
        $("#tooltip").css("display", "none")
        $("#tooltip_remove").css("display", "none")
    });
    
    $("#full_heart_form").mouseenter(function(){
        $("#full_heart_icon").addClass("far fa-heart fa-2x");
        $("#tooltip").css("display", "inline-block")
        $("#tooltip_remove").css("display", "inline-block")
    });
    $("#full_heart_form").mouseleave(function(){
        $("#full_heart_icon").addClass("fas fa-heart fa-2x");
        $("#tooltip").css("display", "none")
        $("#tooltip_remove").css("display", "none")
    });

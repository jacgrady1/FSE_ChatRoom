$(document).ready(function() {
    console.log("what")    
    setInterval(refreshMessage, 1000);
});

var pageInitialized = false;
function refreshMessage(){
    if(pageInitialized) return;
    pageInitialized = true;

    // var current_user = $(".message_form").first().attr('current-user');
    // var csrf = $('[name="csrfmiddlewaretoken"]');
    // var csrfValue = $(csrf).attr('value');
    // var formURL = $(this).attr("action");
    //alert("Hello");
    //console.log("haha")
    //console.log(document.URL)
    $.ajax({
         url: "",
    }).success(function(data){
    // data is your response
    $("#messages").html(data);
    });
        
    // $.ajax(
    // {
    //     url: "/refresh/",
    //     type: "POST",
    //     data: {"current_user": current_user, "csrfmiddlewaretoken": csrfValue},
    //     success:function(data,testStatus,jqXHR){
    //         console.log(data)
    //         $(data).prependTo('#message-main');

    //     },
    //     complete: function(jqXHR,textStatus){
    //         //setTimeout(refreshMessage, 2000);
    //     },
    //     error: function(jqXHR, textStatus, errorThrown) 
    //     {
    //         console.log("mistake");//if fails      
    //     }

    // });
}
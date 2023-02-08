$(document).ready(function(){
    $(document).on("click",".editable",function(){
        var value=$(this).text();
        var data_type=$(this).data("type");
        var input_type="text";
        var input="<input type='"+input_type+"' class='input-data' value='"+value+"' class='form-control'>";
        $(this).html(input);
        $(this).removeClass("editable")
        $(this).remove("input")
    });

    $(document).on("blur",".input-data",function(){
        var value=$(this).val();
        var td=$(this).parent("td");
        $(this).remove();
        td.html(value);
        td.addClass("editable");
        var type=td.data("type");
        sendToServer(td.data("id"),value,type);
        $(this).remove("input")
    });


    $(document).on("keypress",".input-data",function(e){
        var key=e.which;
        if(key==27){
            var value=$(this).val();
            var td=$(this).parent("td");
            $(this).remove();
            td.html(value);
            td.addClass("editable");
        var type=td.data("type");
        }
    });

    $(document).on("keypress",".input-data",function(e){
        var key=e.which;
        if(key==13){
            var value=$(this).val();
            var td=$(this).parent("td");
            $(this).remove();
            td.html(value);
            td.addClass("editable");
        var type=td.data("type");
        sendToServer(td.data("id"),value,type);
        }
    });
    var urlo = window.location.href
    console.log("URL",urlo)
    // get url parameter
    function getIdCedolino(urlo) {
        return urlo.split('/')[4];
    }

    function keyPress (e) {
        if(e.key === "Escape") {
            // write your logic here.
        }
    };

    function sendToServer(id,value,type){
        console.log(id);
        console.log(value);
        console.log(type);
        console.log("URL",getIdCedolino(urlo));
        $.ajax({
            url:`/save-cedolino/${getIdCedolino(urlo)}`,
            type:"POST",
            data:{id:id,type:type,value:value},
        })
        .done(function(response){
            console.log(response);
            location.href = location.href;
            console.log("refreshed")
        })
        .fail(function(){
        console.log("Errore");
        });

    }
});


// -------------------------------------------------------------------------------


$(document).ready(function(){
    
    $("#azzera").click(function(){
        var id=$(this).attr('id')
        console.log(id)
        var name=$(this).attr('name')
        var value=$(this).attr('value')
        sendToServer(id,name,value);
    });

    $("#part").click(function(){
        var id=$(this).attr('id')
        console.log(id)
        var name=$(this).attr('name')
        var value=$(this).attr('value')
        // var perc = document.getElementById("perc");
        // var e = perc.value;
        var perc = $("#percentuale :selected").val() // The text content of the selected option
        console.log(perc)
        sendToServer(id,name,value,perc);});

    $("#full").click(function(){
        var id=$(this).attr('id')
        var name=$(this).attr('name')
        var value=$(this).attr('value')
        sendToServer(id,name,value);});

    var urlo = window.location.href
    // get url parameter
    function getIdCedolino(urlo) {
        return urlo.split('/')[4];
    }

function sendToServer(id,name,value,perc){
    console.log(id);
    console.log(name);
    console.log("URL",getIdCedolino(urlo));
    console.log("PERC",perc)
    $.ajax({
        url:`/set-ore/${getIdCedolino(urlo)}`,
        type:"POST",
        data:{id:id,name:name,value:value,perc:perc},
    })
    console.log(id,name,value)
    .done(function(response){
    })
    .fail(function(){
    console.log("Errore");
})
};

});

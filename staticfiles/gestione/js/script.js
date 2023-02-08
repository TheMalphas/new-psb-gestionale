
$(document).ready(function() {
    var parameter = getUrlParameter("area");
    var parameter = getUrlParameter("sede");
    var parameter = getUrlParameter("societa");
    var parameter = getUrlParameter("contratto");
    var parameter = getUrlParameter("mansione");
    var parameter = getUrlParameter("istruzione");
    var parameter = getUrlParameter("capiarea");
    var parameter = getUrlParameter("dirigenti");
    var parameter = getUrlParameter("responsabili");
    var parameter = getUrlParameter("responsabilisede");
    var parameter = getUrlParameter("referenti");

    
    if (parameter = getUrlParameter("area")) {; //parameterName should be replaced with the actual name of the parameter
        $("#area-anchor").attr("href", function(i, href) {
            return href + parameter;
        });
    }else if (parameter = getUrlParameter("sede")) {
        $("#sede-anchor").attr("href", function(i, href) {
            return href + parameter;
        });
    }
    else if (parameter = getUrlParameter("societa")) {
        $("#societa-anchor").attr("href", function(i, href) {
            return href + parameter;
        });
    }
    else if (parameter = getUrlParameter("contratto")) {
        $("#contratto-anchor").attr("href", function(i, href) {
            return href + parameter;
        });
    }
    else if (parameter = getUrlParameter("mansione")) {
        $("#mansione-anchor").attr("href", function(i, href) {
            return href + parameter;
        });
    }
    else if (parameter = getUrlParameter("istruzione")) {
        $("#istruzione-anchor").attr("href", function(i, href) {
            return href + parameter;
        });
    }
    else if (parameter = getUrlParameter("capiarea")) {
        $("#capoarea-anchor").attr("href", function(i, href) {
            $('#pills-dirigenti-tab').removeClass("active")
            $('#pills-responsabili-tab').removeClass("active")
            $('#pills-responsabilisede-tab').removeClass("active")
            $('#pills-referenti-tab').removeClass("active")
            $('#pills-capiarea-tab').addClass("active")
            return href + '?capiarea=' + parameter;
        });
    }
    else if (parameter = getUrlParameter("dirigenti")) {
        $("#capoarea-anchor").attr("href", function(i, href) {
            var sParameterName = ""
            var hrefToUpdate = $(this).attr("href")
            sParameterName = hrefToUpdate.split('?');
            $('#pills-capiarea-tab').removeClass("active")
            $('#pills-responsabili-tab').removeClass("active")
            $('#pills-responsabilisede-tab').removeClass("active")
            $('#pills-referenti-tab').removeClass("active")
            $('#pills-dirigenti-tab').addClass("active")
            return sParameterName[0] + '?dirigenti=' + parameter;        
        });
    }
    else if (parameter = getUrlParameter("responsabili")) {
        $("#capoarea-anchor").attr("href", function(i, href) {
            var sParameterName = ""
            var hrefToUpdate = $(this).attr("href")
            sParameterName = hrefToUpdate.split('?');
            $('#pills-capiarea-tab').removeClass("active")
            $('#pills-dirigenti-tab').addClass("active")
            $('#pills-responsabilisede-tab').removeClass("active")
            $('#pills-referenti-tab').removeClass("active")
            $('#pills-responsabili-tab').addClass("active")
            return sParameterName[0] + '?responsabili=' + parameter;    
        });
    }
    else if (parameter = getUrlParameter("responsabilisede")) {
        $("#capoarea-anchor").attr("href", function(i, href) {
            var sParameterName = ""
            var hrefToUpdate = $(this).attr("href")
            sParameterName = hrefToUpdate.split('?');
            $('#pills-capiarea-tab').removeClass("active")
            $('#pills-dirigenti-tab').addClass("active")
            $('#pills-responsabili-tab').removeClass("active")
            $('#pills-referenti-tab').removeClass("active")
            $('#pills-responsabilisede-tab').addClass("active")
            return sParameterName[0] + '?responsabilisede=' + parameter;    
        });
    }
    else if (parameter = getUrlParameter("referenti")) {
        $("#capoarea-anchor").attr("href", function(i, href) {
            var sParameterName = ""
            var hrefToUpdate = $(this).attr("href")
            sParameterName = hrefToUpdate.split('?');
            $('#pills-capiarea-tab').removeClass("active")
            $('#pills-dirigenti-tab').addClass("active")
            $('#pills-responsabili-tab').removeClass("active")
            $('#pills-responsabilisede-tab').removeClass("active")
            $('#pills-referenti-tab').addClass("active")
            return sParameterName[0] + '?referenti=' + parameter;    
        });
    }
});

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};

$(document).ready(function() {
    $('.nav-link').on('click', function(e) {
        var tab_id = $(this).attr('id');
        var tab_id_array = tab_id.split('-');
        var tab_name = tab_id_array[1];
        $(".id-field-onchange").attr("name", tab_name);
        var currentVal = $("#capoarea-anchor").attr("href")
        var splitVal = currentVal.split('=')
        var exactVal = splitVal[2]
        var splitVal2 = splitVal[1]
        const val = exactVal

            $("#capoarea-anchor").attr("href", function() {
                var sParameterName = ""
                var hrefToUpdate = $(this).attr("href")
                sParameterName = hrefToUpdate.split('?');
                const title = ["Capi Area", "Dirigenti", "Responsabili", "Responsabili Sede", "Referenti"];
                const tabs = ["capiarea", "dirigenti", "responsabili", "responsabilisede", "referenti"];

                for (let i = 0; i < tabs.length; i++) {
                    var currentSearch = getUrlParameter(tabs[i])
                };
                if (tab_name == "capiarea") {
                    $("#tag-name").text('Capi Area');
                    $("#link-crea-capo").attr("href");
                    linkcapo.attr("href","gestione/aggiungi_capo_area/")
                    linkcapo.text('Crea Nuovo Capo Area')
                }
                else if (tab_name == "dirigenti") {
                    $("#tag-name").text('Dirigenti');
                    $("#link-crea-capo").remove("href")
                    $("#link-crea-capo").attr("href","../aggiungi_dirigente/").text('Crea Nuovo Dirigente');
                }
                else if (tab_name == "responsabili") {
                    $("#tag-name").text('Responsabili');
                    $("#link-crea-capo").remove("href")
                    $("#link-crea-capo").attr("href","../aggiungi_responsabile/").text('Crea Nuovo Responsabile');
                }
                else if (tab_name == "responsabilisede") {
                    $("#tag-name").text('Responsabili Sede');
                    $("#link-crea-capo").remove("href")
                    $("#link-crea-capo").attr("href","../aggiungi_responsabile_sede/").text('Crea Nuovo Resp. Sede');
                }
                else if (tab_name == "referenti") {
                    $("#tag-name").text('Referenti');
                }
                if (currentSearch === undefined) {
                    console.log("if")
                return sParameterName[0] + '?' + tab_name + '=' + val;
                }
                else if (currentSearch != undefined ) {
                    console.log("else")
                    return sParameterName[0] + '?' + tab_name + '=';
                }
        });
        });
});


window.addEventListener("resize", function() {
    const cartaBox = document.querySelector(".cartaBox");
    if (window.innerWidth >= 500) {
      cartaBox.style.display = "grid";
      cartaBox.style.flexWrap = "wrap";
    } else {
      cartaBox.style.display = "wrap";
      cartaBox.style.flexWrap = "";
    }
});
  
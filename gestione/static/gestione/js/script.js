
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

function submitForm() {
    document.getElementById("reception-form-cerca").submit();
}

function submitFormPrecedente() {
    var form = document.getElementById("reception-form-giorno");
    var input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "precedente");
    input.setAttribute("value", "precedente");
    form.appendChild(input);
    form.submit();
}

document.getElementById("reception-button-precedente");


function submitFormGiorno() {
    var form = document.getElementById("reception-form-giorno");
    var input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "search-giorno");
    input.setAttribute("value", "search-giorno");
    form.appendChild(input);
    form.submit();
}

document.getElementById("reception-button-giorno");


function submitFormSuccessivo() {
    var form = document.getElementById("reception-form-giorno");
    var input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "successivo");
    input.setAttribute("value", "successivo");
    form.appendChild(input);
    form.submit();
}

function scaricaForm() {
    // Get the value of the input field
    var inputValue = document.getElementById("dipendente").value;

    if (inputValue === "") {
        // Replace the inputValue with an empty string
        inputValue = "none";
    }

    var inputGiorno = document.getElementById("giorno").value;

    if (inputGiorno === "") {
        // Replace the inputValue with an empty string
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
        var yyyy = today.getFullYear();

        today = yyyy + '-' + mm + '-' + dd;
        inputGiorno = today;
    }

    // Get the form element
    var form = document.createElement("form");

    // // Create a hidden input field to hold the CSRF token
    // var csrfToken = document.createElement("input");
    // csrfToken.setAttribute("type", "hidden");
    // csrfToken.setAttribute("name", "csrfmiddlewaretoken");
    // csrfToken.setAttribute("value", "{{ csrf_token }}");

    // // Add the CSRF token to the form
    // form.appendChild(csrfToken);

    // Set the action attribute of the form to the URL where the data should be submitted
    form.action = "../../gestione/richieste-accettate/scarica/" + inputGiorno + "/" + inputValue + "/";

    // Set the method attribute of the form to GET
    form.method = "post";

    // Add the form to the HTML document
    document.body.appendChild(form);

    // Submit the form
    form.submit();
}

$(document).ready(function() {
    var editor;
    $('#dipendenti-datas-head').clone(true).addClass('filters').appendTo('#reception-datas-head');
    // Clone the original table headers and add a class for styling purposes
    var tableIngressi = $("#dipendenti-datas").DataTable({
        // Specify the source of data for the table using the AJAX option
        ajax: {
            url: "../../../gestione/datatables/dipendenti_json/",
            type: "GET",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            dataSrc: "",
        },
        'columns': [
        { data: 'nominativo', title: "Nominativo" },
        { data: 'getsocieta', title: "Società" },
        { data: 'getsede', title: "Sede" },
        { data: 'getarea', title: "Area" },
        { data: 'capoareadi', title: "Capo Area?" },
        { data: 'getmansione', title: "Mansione" },
        { data: 'contratto', title: "Contratto" },
        { data: 'getinizio', title: "Inizio Rapporto" },
        { data: 'getscadenza', title: "Fine Contratto" },
        { data: 'getsesso', title: "Sesso" },
        { data: 'codice_fiscale', title: "Codice Fiscale" },
        { data: 'getcitta', title: "Indirizzo" },
        { data: 'getprovincia', title: "Provincia" },
        { data: 'iban', title: "IBAN" },
        { data: 'p_iva', title: "P. Iva" },
        ],
        paging:true,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'copy',
                className: 'btn btn-secondary',
                text: 'Copia'
            },
            {
                extend: 'excel',
                className: 'btn btn-success',
                text: 'Excel'
            },
            {
                extend: 'pdfHtml5',
                className: 'btn btn-danger',
                text: 'PDF',
                orientation: 'landscape',
                pageSize: 'A2',
                exportOptions: {
                columns: ':visible'
                },
                customize: function(doc) {
                    doc.content.forEach(function(item) {
                    if (item.text) {
                    item.text[0].fontSize = 8 // Set the font size to 8pt
                    }
                });
                }
            },
        ],
        pageLength: 10,
        datetime:true,
        responsive: true,
        lengthChange:true,
        autoFill:true,
        keys: {
            columns: ':not(:first-child)',
            editor:  editor
        },        searching:true,
        scrollX:true,
        scrollY:true,
        bInfo:true,
        bSort:true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.13.1/i18n/it-IT.json"},
        // Set the processing option to true to show a loading indicator
        processing: true,
    });
});

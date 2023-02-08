$(document).ready(function() {
    var editor;
    $('#reception-datas-head').clone(true).addClass('filters').appendTo('#reception-datas-head');
    // Clone the original table headers and add a class for styling purposes
    var tableIngressi = $("#reception-datas").DataTable({
        'ajax':'/ingressi_json/',
        'columns': [
        { data: 'nominativo', title: "Nominativo" },
        { data: "giorno", title: "Giorno",className: "text-nowrap" },
        { data: "in_permState", title: "In Permesso" },
        { data: "entrata", title: "Entrata" },
        { data: "uscita", title: "Uscita" },
        { data: "seconda_entrata", title: "Seconda Entrata" },
        { data: "seconda_uscita", title: "Seconda Uscita" },
        { data: "anticipo", title: "Anticipo" },
        { data: "ritardo", title: "Ritardo" },
        { data: "straordinario", title: "Straordinario" },
        { data: "ingressoArea", title: "Area" },
        { data: "ingressoSede", title: "Sede" },
        // { data: "ingressoSocieta", title: "Società" },
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
                extend: 'pdf',
                className: 'btn btn-danger',
                text: 'PDF'
            }
        ],
        pageLength: 8,
        autoWidth:true,
        datetime:true,
        responsive: true,
        lengthChange:true,
        autoWidth: true,
        autoFill:true,
        keys: {
            columns: ':not(:first-child)',
            editor:  editor
        },        searching:true,
        scrollX:true,
        bInfo:true,
        bSort:true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.13.1/i18n/it-IT.json"},
        // Specify the source of data for the table using the AJAX option
        ajax: {
            url: "../../ingressi_json/",
            type: "GET",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            dataSrc: "",
        },
        // Set the processing option to true to show a loading indicator
        processing: true,
    });
});


$('#precedente').click(function() {
    var value = "prec";
    var csrf_token = $('[name=csrfmiddlewaretoken]').val();
    var giorno = $('#giorno').val()
    console.log(giorno,value)
    $.ajax({
        url: "/reception/presenze/",
        type: 'POST',
        data: {
            'prec': value,
            'date': giorno,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken').val(),
        },
        headers: {
            'X-CSRFToken': csrf_token
        },
    });
});

$('#successivo').click(function() {
    var value = "succ";
    var csrf_token = $('[name=csrfmiddlewaretoken]').val();
    var giorno = $('#giorno').val()
    console.log(giorno,value)
    $.ajax({
        url: "/reception/presenze/",
        type: 'POST',
        data: {
            'succ': value,
            'date': giorno,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken').val(),
        },
        headers: {
            'X-CSRFToken': csrf_token
        },
    });
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
    input.setAttribute("name", "giorno");
    input.setAttribute("value", "giorno");
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

document.getElementById("reception-button-successivo");
$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#reception-datas tfoot th').each( function (i) {
        var title = $('#reception-datas thead th').eq( $(this).index() ).text();
        $(this).html( '<input type="text" placeholder="'+title+'" data-index="'+i+'" />' );
    } );

    $('#reception-datas thead tr').clone(true).addClass('filters').appendTo( '#reception-datas thead' );

    // var editor;
    // $('#reception-datas-head').clone(true).addClass('filters').appendTo('#reception-datas-head');
    // // Clone the original table headers and add a class for styling purposes

    var tableIngressi = $("#reception-datas").DataTable({
        // Specify the source of data for the table using the AJAX option
        ajax: {
            url: "../../reception/datatables/ingressi_json/",
            type: "GET",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            dataSrc: "",
        },
        'columns': [
        { data: 'nominativo', title: "Nominativo",},
        { data: "giorno", title: "Giorno",className: "text-nowrap" },
        { data: "in_permState", title: "In Permesso" },
        { data: "entrata", title: "Entrata" },
        { data: "uscita", title: "Uscita" },
        { data: "seconda_entrata", title: "Seconda Entrata" },
        { data: "seconda_uscita", title: "Seconda Uscita" },
        { data: "anticipo", title: "Anticipo" },
        { data: "ritardo", title: "Ritardo" },
        { data: "straordinario", title: "Straordinario" },
        { data: "getarea", title: "Area" },
        { data: "getsede", title: "Sede" },
        { data: "getsocieta", title: "Società" },
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
                pageSize: 'A3',
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
            {
                text: 'Mese',
                className: 'btn btn-primary',
                action: function ( e, dt, node, config ) {
                        // Set the window location to the desired URL
                        window.open('/reception/datatables_mese/')
                    }
            }
        ],
        pageLength: 20,
        datetime:true,
        responsive: true,
        lengthChange:true,
        autoWidth: false,
        autoFill:true,
        // keys: {
        //     columns: ':not(:first-child)',
        //     editor:  editor
        // },        
        searching:true,
        bInfo:true,
        bSort:true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.13.1/i18n/it-IT.json"},
        // Set the processing option to true to show a loading indicator
        processing: true,
    });
});

$(document).ready(function() {
    var editor;
    $('#reception-datas-head-mese').clone(true).addClass('filters').appendTo('#reception-datas-head-mese');
    // Clone the original table headers and add a class for styling purposes
    var tableIngressi = $("#reception-datas-mese").DataTable({
         // Specify the source of data for the table using the AJAX option
        ajax: {
            url: "../../reception/datatables/mese_json/",
            type: "GET",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            dataSrc: "",
        },
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
        { data: "getarea", title: "Area" },
        { data: "getsede", title: "Sede" },
        { data: "getsocieta", title: "Società" },
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
                pageSize: 'A3',
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
            {
                text: 'Giorno',
                className: 'btn btn-primary',
                action: function ( e, dt, node, config ) {
                    // Set the window location to the desired URL
                    window.open('/reception/datatables/')
                }
            }
        ],
        pageLength: 20,
        datetime:true,
        responsive: true,
        lengthChange:true,
        autoWidth: false,
        autoFill:true,
        fixedColumns: true,
        // keys: {
        //     columns: ':not(:first-child)',
        //     editor:  editor
        // },        
        searching:true,
        bInfo:true,
        bSort:true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.13.1/i18n/it-IT.json"},
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

function submitFormDipendente() {
    var form = document.getElementById("reception-form-cerca");
    var input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "giorno");
    input.setAttribute("value", document.getElementById("giorno").value);
    form.appendChild(input);
    console.log(input);
    form.submit();
}
 
document.getElementById("button-cerca-dipendente");



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
    var input = document.createElement("solo");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", "solo");
    input.setAttribute("value", "solo");
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



function submitFormData() {
    var form = document.getElementById("reception-form-data");
    form.submit();
}

document.getElementById("excel-giorno-presenze");


function submitFormPerDipendente() {
    var form = document.getElementById("reception-form-per-dipendente");
    
    var start = document.createElement("input");
    start.setAttribute("type", "hidden");
    start.setAttribute("name", "start");
    start.setAttribute("value", document.getElementById("start").value);
    console.log(document.getElementById("start").value);
    form.appendChild(start);

    var end = document.createElement("input");
    end.setAttribute("type", "hidden");
    end.setAttribute("name", "end");
    end.setAttribute("value", document.getElementById("end").value);
    form.appendChild(end);
    console.log(document.getElementById("end").value);
    form.submit();
}

document.getElementById("reception-form-per-dipendente-button");


/* Create and submit form on presenze_per_dip */

const submitButton = document.getElementById('reception-scarica-dipendente-button');

submitButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent default button behavior

  const form = document.createElement('form');
  form.action = 'presenze/download/excel/presenze-per-dipendente/';
  form.method = 'POST';

  const input1 = document.createElement('input');
  input1.type = 'text';
  input1.name = 'dipendente';
  input1.placeholder = document.getElementById("dipendente").value;
  form.appendChild(input1);

  document.body.appendChild(form);
  form.submit();
});
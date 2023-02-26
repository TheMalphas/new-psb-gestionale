$(document).ready(function() {
    var editor;
    $('#contratti_datas_head').clone(true).addClass('filters').appendTo('#contratti_datas_head');
    // Clone the original table headers and add a class for styling purposes
    var tableIngressi = $("#contratti_datas").DataTable({
        // Specify the source of data for the table using the AJAX option
        ajax: {
            url: "../../../gestione/datatables/contratti_json/",
            type: "GET",
            // data: {
            //     csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            // },
            // dataSrc: "",
        },
        'columns': [
        { data: 'getdipendente', title: "Dipendente"  },
        { data: 'getsocieta', title: "Società"  },
        { data: 'gettipologia', title: "Tipologia"  },
        { data: 'getccnl', title: "CCNL"  },
        { data: 'getpercentuale', title: "Percentuale"  },
        { data: 'datainizio', title: "Data Inizio"  },
        { data: 'datafine', title: "Data Termine"  },
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
        pageLength: 30,
        autoWidth: false,
        datetime:true,
        responsive: true,
        lengthChange:true,
        autoFill:true,
        fixedColumns: true,
        keys: {
            columns: ':not(:first-child)',
            editor:  editor
        },
        searching:true,
        bInfo:true,
        bSort:true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.13.1/i18n/it-IT.json"},
        // Set the processing option to true to show a loading indicator
        processing: true,
    });
});

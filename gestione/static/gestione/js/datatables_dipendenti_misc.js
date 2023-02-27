$(document).ready(function() {
    var editor;
    $('#dipendenti-datas-head-misc').clone(true).addClass('filters').appendTo('#dipendenti-datas-head-misc');
    // Clone the original table headers and add a class for styling purposes
    var tableIngressi = $("#dipendenti-datas-misc").DataTable({
        // Specify the source of data for the table using the AJAX option
        ajax: {
            url: "../../../../gestione/datatables/dipendenti_misc_json",
            type: "GET",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            dataSrc: "",
        },
        drawCallback: function(settings) {
            var api = this.api();
            var recordsFiltered = api.page.info().recordsDisplay; // Get the number of rows that match the current filter criteria
            $(this.api().table().footer()).find('#filtered-count').text(recordsFiltered); // Update the count in the footer
        },
        'columns': [
        { data: 'nominativo', title: "Nominativo"  },
        { data: 'getsocieta', title: "Società"   },
        { data: 'getsede', title: "Sede"   },
        { data: 'getarea', title: "Area"   },
        { data: 'getmansione', title: "Mansione"   },
        { data: 'getsesso', title: "Sesso"   },
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
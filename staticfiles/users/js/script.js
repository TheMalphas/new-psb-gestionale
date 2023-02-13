$(document).ready(function () {
    $("#da_giorno").prop("disabled", true);
    $("#a_giorno").prop("disabled", true);
    $("#urgente").prop("checked", false);
  });

  
$(document).ready(function (){
    $("#id_permessi_richieste option[value='15']").remove()
});

$(".disabled").prop("disabled", true);
// $("#urgente").prop("disabled", true);

const addDays = (date, period) => {
  date.setDate(date.getDate() + period);
};

var urgentCheck = false;
$(document).ready(function () {
    $('#urgente').click(function() {
    var value = $(this).val()
    console.log(value)
    if (urgentCheck == false) {
        var permesso = document.getElementById('id_permessi_richieste').value;
        var oneDayToAdd = new Date()
        addDays(oneDayToAdd, 1);
        var dd = String(oneDayToAdd.getDate()).padStart(2, '0');
        var mm = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
        var yyyy = oneDayToAdd.getFullYear();

        var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
        var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
        var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

        todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
        if (urgentCheck = true) {
            $('#da_giorno').attr('min',todayPlusOne);
            $('#a_giorno').attr('min',todayPlusOne);
        }
        urgentCheck = true
    }
    else if (urgentCheck == true) {
        statoPermessi = $('#id_permessi_richieste').val()
        var permesso = document.getElementById('id_permessi_richieste').value;
        var value = $(this).val()
        console.log(value)
        if (permesso == "1" || permesso == "16") {
        $('#da_giorno').attr('min',todayPlusOne);
        $('#a_giorno').attr('min',todayPlusOne);
        } else if (permesso == "9") {
        $('#da_giorno').attr('min',todayPlusFive);
        $('#a_giorno').attr('min',todayPlusFive);
        } else if (permesso == "6" || permesso == "7" || permesso == "8" || permesso == "10" || permesso == "11" || permesso == "12" || permesso == "14" ) {
        $('#da_giorno').attr('min',todayPlusTen);
        $('#a_giorno').attr('min',todayPlusTen);
        } else if (permesso == "3" || permesso == "4") {
        $('#da_giorno').attr('min',todayPlusFifteen);
        $('#a_giorno').attr('min',todayPlusFifteen);
        } else if (permesso == "2") {
        $('#da_giorno').attr('min',todayPlusTwoMonths);
        $('#a_giorno').attr('min',todayPlusTwoMonths);
        }
        urgentCheck = !urgentCheck
    }
    });
});
// $(document).ready(function(){
//   $('#id_permessi_richieste').change(function(){
//     value = $(this).val()
//     console.log(value)
//   })
// });

$(document).ready(function(){
  $('#id_permessi_richieste').change(function(){
    if ($(this).val() == "") //start if empty if block
    {
      $("#da_giorno").prop("disabled", true);
      $("#a_giorno").prop("disabled", true);
    } //end if empty if block
    else if ($(this).val() == 1 || $(this).val() == "5" || $(this).val() == "13" || $(this).val() == "16") { //start else if 1 day block
      $("#da_giorno").prop("disabled", false);
      $("#a_giorno").prop("disabled", false);
      var oneDayToAdd = new Date()
      addDays(oneDayToAdd, 1);
      var dd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mm = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = oneDayToAdd.getFullYear();

      var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

      todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
      $('#da_giorno').attr('min',todayPlusOne);
      $('#a_giorno').attr('min',todayPlusOne);
    } //else if oneDay endblock
    else if (($(this).val() == "9") && urgentCheck == true) { //start else if 5 days and urgent block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var oneDayToAdd = new Date()
      addDays(oneDayToAdd, 1);
      var dd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mm = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = oneDayToAdd.getFullYear();

      var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

      todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
      $('#da_giorno').attr('min',todayPlusOne);
      $('#a_giorno').attr('min',todayPlusOne);
    } //else if fiveDays endblock
    else if ($(this).val() == "9") { //start else if 5 days and urgent block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var fiveDaysToAdd = new Date()
      addDays(fiveDaysToAdd, 5);
      var dd = String(fiveDaysToAdd.getDate()).padStart(2, '0');
      var mm = String(fiveDaysToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = fiveDaysToAdd.getFullYear();

      var ddfiveDaysToAdd = String(fiveDaysToAdd.getDate()).padStart(2, '0');
      var mmfiveDaysToAdd = String(fiveDaysToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyfiveDaysToAdd = fiveDaysToAdd.getFullYear();

      todayPlusFive = yyyyfiveDaysToAdd + '-'  + mmfiveDaysToAdd + '-' + ddfiveDaysToAdd;
      $('#da_giorno').attr('min',todayPlusFive);
      $('#a_giorno').attr('min',todayPlusFive);
    } //else if fiveDays endblock
    else if (($(this).val() == "6" || $(this).val() == "7" || $(this).val() == "8" || $(this).val() == "10" || $(this).val() == "11" || $(this).val() == "12" || $(this).val() == "14") && urgentCheck == true) { //start else if 10 days and urgent block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var oneDayToAdd = new Date()
      addDays(oneDayToAdd, 1);
      var dd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mm = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = oneDayToAdd.getFullYear();

      var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

      todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
      $('#da_giorno').attr('min',todayPlusOne);
      $('#a_giorno').attr('min',todayPlusOne);
    } //else if tenDays and urgent endblock
    else if ($(this).val() == "6" || $(this).val() == "7" || $(this).val() == "8" || $(this).val() == "10" || $(this).val() == "11" || $(this).val() == "12" || $(this).val() == "14") { //start else if 10 days block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var tenDaysToAdd = new Date()
      addDays(tenDaysToAdd, 10);
      var dd = String(tenDaysToAdd.getDate()).padStart(2, '0');
      var mm = String(tenDaysToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = tenDaysToAdd.getFullYear();

      var ddTenDaysToAdd = String(tenDaysToAdd.getDate()).padStart(2, '0');
      var mmTenDaysToAdd = String(tenDaysToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyTenDaysToAdd = tenDaysToAdd.getFullYear();

      todayPlusTen = yyyyTenDaysToAdd + '-'  + mmTenDaysToAdd + '-' + ddTenDaysToAdd;
      $('#da_giorno').attr('min',todayPlusTen);
      $('#a_giorno').attr('min',todayPlusTen);
    } //else if tenDays endblock
    else if (($(this).val() == "3" || $(this).val() == "4") && urgentCheck == true) { //start else if 15 days and urgent block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var oneDayToAdd = new Date()
      addDays(oneDayToAdd, 1);
      var dd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mm = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = oneDayToAdd.getFullYear();

      var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

      todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
      $('#da_giorno').attr('min',todayPlusOne);
      $('#a_giorno').attr('min',todayPlusOne);
    } //else if fifteenDays endblock
    else if ($(this).val() == "3" || $(this).val() == "4") { //start else if 15 days and urgent block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var fifteenDaysToAdd = new Date()
      addDays(fifteenDaysToAdd, 15);
      var dd = String(fifteenDaysToAdd.getDate()).padStart(2, '0');
      var mm = String(fifteenDaysToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = fifteenDaysToAdd.getFullYear();

      var ddFifteenDaysToAdd = String(fifteenDaysToAdd.getDate()).padStart(2, '0');
      var mmFifteenDaysToAdd = String(fifteenDaysToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyFifteenDaysToAdd = fifteenDaysToAdd.getFullYear();

      todayPlusFifteen = yyyyFifteenDaysToAdd + '-'  + mmFifteenDaysToAdd + '-' + ddFifteenDaysToAdd;
      $('#da_giorno').attr('min',todayPlusFifteen);
      $('#a_giorno').attr('min',todayPlusFifteen);
    } //else if fifteenDays endblock
    else if (($(this).val() == "2") && urgentCheck == true) { //start else if 2 months and urgent block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var oneDayToAdd = new Date()
      addDays(oneDayToAdd, 1);
      var dd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mm = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyy = oneDayToAdd.getFullYear();

      var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
      var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
      var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

      todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
      $('#da_giorno').attr('min',todayPlusOne);
      $('#a_giorno').attr('min',todayPlusOne);
    } //else if 2 months and urgent endblock
    else if ($(this).val() == "2") { //start else if 2 months block
        $("#da_giorno").prop("disabled", false);
        $("#a_giorno").prop("disabled", false);
      var todayPlusTwoMonths = new Date()

      var dd = String(todayPlusTwoMonths.getDate()).padStart(2, '0');
      var addTwomm = String(todayPlusTwoMonths.getMonth() + 3).padStart(2, '0');
      var yyyy = todayPlusTwoMonths.getFullYear();

      todayPlusTwoMonths = yyyy + '-' + addTwomm + '-' + dd;
      $('#da_giorno').attr('min',todayPlusTwoMonths);
      $('#a_giorno').attr('min',todayPlusTwoMonths);
    } //else if 2 months endblock
  })
});

/// ==================================================================================================================================///

$(document).ready(function () {
  var oneDayToAdd = new Date()
  addDays(oneDayToAdd, 1);

  var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
  var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
  var yyyyOneDayToAdd = oneDayToAdd.getFullYear();

  todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;
  $('#da_giorno_richiestaOra').attr('min',todayPlusOne);
  $("#da_ora_ora").prop("disabled", false);
  $("#a_ora_ora").prop("disabled", false);
  $("#urgenteOra").prop("checked", false);
});

var permesso = true

$(document).ready(function () {
    $('#urgenteOra').click(function() {
      console.log(permesso)
    if (permesso == true) {   
      $("#urgenteOra").prop("checked", true);

        var today = new Date()
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0');
        var yyyy = today.getFullYear();
        today  = yyyy + '-'  + mm + '-' + dd;

        $('#da_giorno_richiestaOra').attr('min',today);
        permesso = false
    }
    else if (permesso == false) {
        $("#urgenteOra").prop("checked", false);
        console.log(permesso)
        statoPermessi = $('#urgenteOra').val()

        var oneDayToAdd = new Date()
        addDays(oneDayToAdd, 1);
        var ddOneDayToAdd = String(oneDayToAdd.getDate()).padStart(2, '0');
        var mmOneDayToAdd = String(oneDayToAdd.getMonth() + 1).padStart(2, '0');
        var yyyyOneDayToAdd = oneDayToAdd.getFullYear();
        todayPlusOne  = yyyyOneDayToAdd + '-'  + mmOneDayToAdd + '-' + ddOneDayToAdd;

        $('#da_giorno_richiestaOra').attr('min',todayPlusOne);
        permesso = true
    }
    });
});
$(function () {

    var iteration
    var citations
    var firstTimestamp
    var secondTimestamp
    var count


    $("#begincitation").change(function () {
        numbermax = 300 - $("#begincitation").val() + 1
        $("#numbercitation").attr("max", numbermax)
        if ($("#numbercitation").val() > numbermax) {
            $("#numbercitation").val(numbermax)
        }
    });

    $("#numbercitation").change(function () {
        numbermax = 300 - $("#numbercitation").val() + 1
        $("#begincitation").attr("max", numbermax)
        if ($("#begincitation").val() > numbermax) {
            $("#begincitation").val(numbermax)
        }
    });

    $("#Run").click(function () {

        iteration = 1;
        BeginCitation = $('#begincitation').val();
        NumberCitation = $('#numbercitation').val();
        TypeOfSort = $('#typeofsort').val();

        //problem with the input number and step 10 that doesn't work if min is not equal to zero
        if (NumberCitation == 0) {
        alert("Ne pas choisir zero")
        return; //
        }

        $.ajax({
            url: '/RequestCitations',
            type: 'POST',
            data: JSON.stringify([BeginCitation, NumberCitation, TypeOfSort]),
            success: function (dicts) {
                citations = dicts;
                $("#ShowCitation").css({ "font-size": "60px", "text-align": "center" });
                $("#ShowCitation").html(citations[iteration][0]);

            }
        });

        firstTimestamp = new Date().getTime();
        $('#Suivant').attr("disabled", "disabled")
        $("#ShowSRRandTRT").html('')
    });

    $("#Plusone").click(function () {
        NewSRR = parseInt(citations[iteration][2]) + 1;
        ShowCitation()
    });

    $("#Minusone").click(function () {
        NewSRR = parseInt(citations[iteration][2]) - 1;
        ShowCitation()
    });

    $("#Suivant").click(function () {

        iteration = iteration + 1;
        firstTimestamp = new Date().getTime();
        $("#ShowCitation").html(citations[iteration][0]);
        $("#ShowCitation").css({ "font-size": "60px", "text-align": "center" })
        $('#Suivant').attr("disabled", "disabled")
        $("#ShowSRRandTRT").html('')
    });


    function  ShowCitation() {
        secondTimestamp = new Date().getTime();
        NewTRT = (secondTimestamp - firstTimestamp) / 1000;
        NewTRT = parseFloat(NewTRT).toFixed(1);

        CurrentCitationNumber = citations[iteration][0]

        citations[iteration][2] = NewSRR.toString()

        $.ajax({
            url: '/SaveTrainingResults',
            type: 'POST',
            data: JSON.stringify({ 'CurrentCitationNumber': CurrentCitationNumber, 'NewSRR': NewSRR, 'NewTRT': NewTRT }),
            success: function (saved) {
                //alert(saved);
                $("#ShowSRRandTRT").html('New SRR= ' + saved[0] + '; New TRT= ' + saved[1])

            }
        });
        $("#ShowCitation").html(citations[iteration][1]);
        $("#ShowCitation").removeAttr('style');

        count = Object.keys(citations).length;
        if (iteration < count) {
            $('#Suivant').removeAttr('disabled');
        }
    }

});
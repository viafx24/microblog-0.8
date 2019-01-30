$(function () {

    var iteration
    var citations
    var firstTimestamp
    var secondTimestamp

    $("#Run").click(function () {


        iteration = 1;
        variable = Number($('#numbercitation').val());


        $.ajax({
            url: '/RequestCitations',
            type: 'POST',
            data: JSON.stringify(variable),
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

        secondTimestamp = new Date().getTime();
        NewTRT = Math.floor((secondTimestamp - firstTimestamp) / 1000);
        CurrentCitationNumber = citations[iteration][0]
        NewSRR = parseInt(citations[iteration][2]) + 1
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
        $('#Suivant').removeAttr('disabled');

    });

    $("#Suivant").click(function () {
        iteration = iteration + 1;
        firstTimestamp = new Date().getTime();
        //$("#ShowCitation").html(citations.keys()[iteration]);
        $("#ShowCitation").html(citations[iteration][0]);
        $("#ShowCitation").css({ "font-size": "60px", "text-align": "center" })
        $('#Suivant').attr("disabled", "disabled")
        $("#ShowSRRandTRT").html('')
    });

});
$(function () {

    var iteration
    var citations
    var firstTimestamp
    var secondTimestamp
    var count
    //var RandomSample = []


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

    //$('#typeofsort').change(function () {
    //    if ($('#typeofsort').val() == 'rand')
    //        alert('rand')
        
    //});



    $("#Run").click(function () {

        iteration = 1;
        BeginCitation = $('#begincitation').val();
        NumberCitation = $('#numbercitation').val();
        TypeOfSort = $('#typeofsort').val();

        if ($('#typeofsort').val() == 'rand') {

            debut = parseInt(BeginCitation)
            fin = parseInt(BeginCitation) + parseInt(NumberCitation)
            Sample = range(debut, fin, 1)
            var RandomSample = getRandomSubarray(Sample, Sample.length);
            alert(RandomSample)
            var RandomSampleOld = RandomSample.slice()
            var person = prompt("Enter a number");
            for (var iter = 0; iter < RandomSample.length; iter++) {
                RandomSample[iter] = RandomSample[iter] + parseInt(person)
                while (RandomSample[iter] > (fin - 1)) {
                    RandomSample[iter] = debut + (RandomSample[iter] - fin)
                }
            }
            alert('The first : ' + RandomSampleOld + '\n\n\n The second : ' + RandomSample)

            RandomSample = RandomSample.toString();
        }
        else {
            RandomSample =[]
        }
       
    

        //problem with the input number and step 10 that doesn't work if min is not equal to zero
        if (NumberCitation == 0) {
        alert("Ne pas choisir zero")
        return; //
        }

        $.ajax({
            url: '/RequestCitations',
            type: 'POST',
            data: JSON.stringify([BeginCitation, NumberCitation, TypeOfSort, RandomSample]),
            success: function (ReceivedDict) {
                citations = ReceivedDict;
                ShowNumber();
            },
            error: function (xhr, status, error) {
                var errorMessage = xhr.status + ': ' + xhr.statusText;
                alert('Erreur - ' + errorMessage);
            }
        });
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
        ShowNumber();
    });

    function ShowNumber() {

        firstTimestamp = new Date().getTime();
        $("#ShowCitation").html(citations[iteration][0]);
        $("#ShowCitation").css({ "font-size": "60px", "text-align": "center" })
        $('#Suivant').attr("disabled", "disabled")
        $("#ShowSRRandTRT").html('Count=' + iteration)

    }

    function  ShowCitation() {
        secondTimestamp = new Date().getTime();
        NewTRT = (secondTimestamp - firstTimestamp) / 1000;
        NewTRT = parseFloat(NewTRT).toFixed(1); 

        CurrentCitationNumber = citations[iteration][0];
        citations[iteration][2] = NewSRR.toString(); /*important*/

        $.ajax({
            url: '/SaveTrainingResults',
            type: 'POST',
            data: JSON.stringify({ 'CurrentCitationNumber': CurrentCitationNumber, 'NewSRR': NewSRR, 'NewTRT': NewTRT }),
            success: function (ReceivedData) {
                $("#ShowSRRandTRT").html('New SRR= ' + ReceivedData[0] + '; New TRT= ' + ReceivedData[1])
            },
            error: function(xhr, status, error) {
                var errorMessage = xhr.status + ': ' + xhr.statusText;
            //      alert('Erreur - ' + errorMessage);
            }
        });
        $("#ShowCitation").html(citations[iteration][1]);
        $("#ShowCitation").removeAttr('style');

        // disabled button "suivant" when have passed all the citations
        count = Object.keys(citations).length;
        if (iteration < count) {
            $('#Suivant').removeAttr('disabled');
        }




        // change the fontsize of ctiation text when the text is too long
        var NumberLetter = citations[iteration][1].length

        if (NumberLetter > 440) {
            if ($(window).width() > 850) {
                $("#ShowCitation").css("font-size", "24px")
            }
            else {
                $("#ShowCitation").css("font-size", "11px")
            }
        }
    }
    //find on the web
    function getRandomSubarray(arr, size) {
        var shuffled = arr.slice(0), i = arr.length, temp, index;
        while (i--) {
            index = Math.floor((i + 1) * Math.random());
            temp = shuffled[index];
            shuffled[index] = shuffled[i];
            shuffled[i] = temp;
        }
        return shuffled.slice(0, size);
    }

    //find on the web
    function range(start, stop, step) {
        if (typeof stop == 'undefined') {
            // one param defined
            stop = start;
            start = 0;
        }

        if (typeof step == 'undefined') {
            step = 1;
        }

        if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
            return [];
        }

        var result = [];
        for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
            result.push(i);
        }

        return result;
    };
});
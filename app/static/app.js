
    $(function () {
        // write start up code here

        $('GetData').click(function () {
            $.getJSON('/RequestCitations', function (data) {
                alert(data.citations[1].text);
            });
        });

        //$('#Hide').click(function () {
        //    $('span.text').hide();
        //});

    });

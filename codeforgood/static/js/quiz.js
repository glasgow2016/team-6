$(document).ready(function () {

    $(document.body).on('click', '#category-list', function () {
        //
        // var answer = $('#answer').find("input[type=radio]:checked").val();
        // console.log(answer);

        /* Send the ajax request */
        $.ajax({
            type: "GET",
            traditional: true,
            url: '/quiz/',
            data: {
                'answer': answer
            },
            success: function (data) {
                //
            }
        });
    });

});



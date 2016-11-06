$(function(){
    if($('#progress-circle-container').length != 0) {
        console.log("here");

        $('.water').animate({
            height: '25%'
        }, 1000);


        $('add-new-distance').on('submit', function (event) {
            console.log("Stopped form submission");
            event.preventDefault();
            console.log("Stopped form submission");
        });

        var bar = new ProgressBar.Circle("#progress-circle-container", {
            color: '#aaa',
            // This has to be the same size as the maximum width to
            // prevent clipping
            strokeWidth: 4,
            trailWidth: 5,
            easing: 'easeInOut',
            duration: 1400,
            text: {
                autoStyleContainer: false
            },
            from: {color: '#aaa', width: 1},
            to: {color: '#333', width: 4},
            // Set default step function for all animate calls
            step: function (state, circle) {
                circle.path.setAttribute('stroke', state.color);
                circle.path.setAttribute('stroke-width', state.width);

                var value = Math.round(circle.value() * 100);
                if (value === 0) {
                    circle.setText('');
                } else {
                    circle.setText(value);
                }

            }
        });
        bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
        bar.text.style.fontSize = '2rem';

        bar.animate(0.05);  // Number from 0.0 to 1.0
    }
});

/* functions about interacting with the daterange picker */
$(function () {
    var start = moment().subtract(14, 'days');
    var end = moment().subtract(7, 'days');

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
    }

    $('#reportrange span').daterangepicker({
        autoUpdateInput: false,
        locale: {
            cancelLabel: 'Clear'
        }
    });

    $('#reportrange').daterangepicker({
        startDate: start,
        endDate: end,
        ranges: {
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);
    cb(start, end);
});

function getDateRangePickerEndDate() {
    /* If there is no range displayed inside the span, this means we want to get
     * all the orders, so simply return undefined in that case
     */
    var span_content = $('#daterange-picker-holder').html();
    if(span_content === ''){
        return undefined;
    }
    return $('#reportrange').data('daterangepicker').endDate.format('YYYY-MM-DDT23:59:59');
}

function getDateRangePickerStartDate(){
    /* If there is no range displayed inside the span, this means we want to get
     * all the orders, so simply return undefined in that case
     */
    var span_content = $('#daterange-picker-holder').html();
    if(span_content === ''){
        return undefined;
    }
    return $('#reportrange').data('daterangepicker').startDate.format('YYYY-MM-DDT00:00:00');
}


function addNewDistance() {

    let target_distance = 2000;
    let new_distance = $("#new-distance-input").val();
    console.log(new_distance);



    return false;

}

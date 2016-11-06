var bar;

$(function () {
    if ($('#progress-circle-container').length != 0) {

        $('.water').animate({
            height: '25%'
        }, 1000);

        let target_distance = parseInt($("#goal").text());

        bar = new ProgressBar.Circle("#progress-circle-container", {
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

                var value = Math.round(circle.value() * target_distance);
                if (value === 0) {
                    circle.setText('0');
                } else {
                    circle.setText(value);
                }
            }
        });
        bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
        bar.text.style.fontSize = '2rem';

        //let goal_achieved = parseInt($("#goal-achieved").text());
        let goal_achieved = parseInt($("#goal-achieved").attr('value'));
        let percentage_achieved = goal_achieved / target_distance;
        bar.animate(percentage_achieved);  // Number from 0.0 to 1.0
    }
});

/* functions about interacting with the daterange picker */
$(function () {
    var today = moment();

// Handles the form submission and
// takes care that the necessary parts of the page are updated

    function cb(time) {
        $('#reportrange span').html(time.format('MMMM D, YYYY'));
        $('#final-date')
            .attr('value', time.format('YYYY-MM-DD'));
    }

    $('#reportrange').daterangepicker({
        singleDatePicker: true
    }, function (date) {
        cb(date);

    });
    cb(today);
});

function addNewDistance() {
    let target_distance = parseInt($("#goal").text());
    let new_distance = parseInt($("#new-distance-input").val());
    var current_distance = parseInt($("#goal-achieved").attr('value'));
    $('#goal-achieved').attr('value', new_distance + current_distance);
    var full_distance = new_distance + current_distance;
    console.log("New distance is " + new_distance + " current distance is " + current_distance);
    console.log(full_distance);

    if (!isInt(new_distance)) {
        return false;
    }
    let new_percentage = new_distance / target_distance;
    let existing_percentage = 0;
    if (!bar['text']['firstChild']) {
        existing_percentage = 0;
    } else {
        existing_percentage = bar['text']['firstChild']['data'] / target_distance;
    }
    // updates the progress chart
    var done = false;
    var newCO2;
    var newMoney;
    if (new_percentage + existing_percentage >= 1) {
        done = true;
        newCO2 = updateCO2(target_distance);
        newMoney = updateMoney(target_distance);
        bar.animate(1);
    } else {
        bar.animate(new_percentage + existing_percentage);
        newCO2 = updateCO2(new_distance);
        newMoney = updateMoney(new_distance);
    }

    var project_id = $('#project_id').attr('value');
    /* update the database */
    $.ajax({
        type: "GET",
        url: '/update_performance/',
        data: {
            'new_distance': new_distance,
            'project_id': project_id,
            'newCO2': newCO2,
            'newMoney': newMoney
        },
        success: function (data) {

        }
    });

    if(done) {
        $('#modal-co2-report').html(newCO2);
        $('#modal-cash-report').html(newMoney);
        $('#modal-miles-report').html(full_distance);
        $('#success-modal').modal('show');
    }

    return false;
}

function updateCO2(new_distance) {

    // An average day without a car saves 26lbs of CO2 ~ 12kg
    // Assuming an average day is with a car is 20 miles, a mile not
    // driven would amount to 0.6kg.

    let existing_co2 = parseInt($('#co2-text').text());
    let new_co2 = parseInt(new_distance) * 0.6 + existing_co2;
    $('#co2-text').text(new_co2);
    return new_co2;

}

function updateMoney(new_distance) {

    // An average 20 mile day with a car
    // Average 5 miles per litre
    // Average litre price = 1.10 pounds
    // Average mile not driven saves 0.22 pence

    let existing_dollar = parseInt($('#dollar-text').text());
    let new_dollar = parseInt(new_distance) * 0.22 + existing_dollar
    $('#dollar-text').text(new_dollar);
    return new_dollar;
}

// Stackoverflow rules!
function isInt(value) {
    return !isNaN(value) &&
        parseInt(Number(value)) == value && !isNaN(parseInt(value, 10));
}

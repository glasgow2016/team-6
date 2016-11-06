var bar;

$(function(){

    console.log("here");

    $('.water').animate({
        height: '25%'
    }, 1000);


    $('add-new-distance').on('submit', function(event) {
        console.log("Stopped form submission");
        event.preventDefault();
        console.log("Stopped form submission");
    });

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
        from: { color: '#aaa', width: 1 },
        to: { color: '#333', width: 4 },
        // Set default step function for all animate calls
        step: function(state, circle) {
            circle.path.setAttribute('stroke', state.color);
            circle.path.setAttribute('stroke-width', state.width);
            var value = Math.round(circle.value() * 2000);
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
});

// Handles the form submission and
// takes care that the necessary parts of the page are updated
function addNewDistance() {

    let target_distance = 2000;
    let new_distance = $("#new-distance-input").val();

    if (!isInt(new_distance)) {
        return false;
    }

    let new_percentage = new_distance/target_distance;
    let existring_percentage = bar['text']['firstChild']['data']/target_distance;

    // updates the progress chart
    bar.animate(new_percentage + existring_percentage);

    updateCO2(new_distance);
    updateMoney(new_distance);

    return false;
}

function updateCO2(new_distance) {

    let existing_co2 = parseInt($('#co2-text').text());
    $('#co2-text').text(parseInt(new_distance) + existing_co2);

}

function updateMoney(new_distance) {

    let existing_dollar = parseInt($('#dollar-text').text());
    $('#dollar-text').text(parseInt(new_distance) + existing_dollar);

}

// Stackoverflow rules!
function isInt(value) {
  return !isNaN(value) &&
         parseInt(Number(value)) == value &&
         !isNaN(parseInt(value, 10));
}

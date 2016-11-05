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

});

function addNewDistance() {

    let target_distance = 2000;
    let new_distance = $("#new-distance-input").val();
    console.log(new_distance);



    return false;

}

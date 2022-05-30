function showForms(){
    // var form = document.getElementById('formModal');
    // form.style.display = "flex";
    console.log("Hello")

    var modal = document.getElementById("formModal");
    modal.style.display = "flex";

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {

        // form.style.display = "none";
        modal.style.display = "none";
        }
    }
}

// function initializePlaceForm(instance_data){
// // function initializePlaceForm(formid='PlaceForm', instance_data){
//     // $('#some_field').val(data.some_value);
//     console.log("Hello")
//     console.log(instance_data);

// }
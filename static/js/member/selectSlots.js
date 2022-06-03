// METHOD 1 For getting dynamically added jquery dom elements

$(document).ready(() => {
    function timeslotClick(){
        var item = this;
        var day = item.classList.value.split(" ").pop();
        console.log("Classes: ", day);

        var day_headers = [...selected_container.querySelectorAll(`.body1.header.${day}`)];
        console.log("Day Headers", day_headers);
        
        if (available_container.contains(item)) {
            this.classList.add("selected");
            var fragment = document.createDocumentFragment();
            fragment.appendChild(this);

            // Checking if the selected timeslots section 
            // has a header with classname thats the same 
            // as one in the timeslots classlist
            day_headers = Array.from(day_headers.filter((e) => {
                return e.classList.value.indexOf(day) >= 0;
            }));
            console.log(day_headers);

            var header;
            if (day_headers.length == 0){
                console.log("No headers found; ");
                header = document.createElement("div");
                header.textContent = day;
                header.classList.add('body1', 'header', day);
                
                selected_container.appendChild(header);
            }
            else if (day_headers.length > 0){
                console.log("Headers found; ");
                header = day_headers[0];
                // selected_container.appendChild(header);
            }
            header.after(fragment);
        } 
        else if (selected_container.contains(item)) {
            // alert('Item is a child of selected slots');
            this.classList.remove("reserved");
            var original_box = available_container.querySelector(`#${day}`);
            original_box = original_box.querySelector(".rectangle");

            console.log(original_box)
            // original_box.appendChild(item);

            
        }

        
    }

    var available_container = document.getElementById("available");

    var selected_container = document.getElementById("selected");

    console.log(available_container);

    $("#available-container").ready(function () {

        var elements = document.getElementsByClassName("timeslot");

        for (var i = 0; i < elements.length; i++) {
            elements[i].addEventListener('click', timeslotClick);
        }

    });
})
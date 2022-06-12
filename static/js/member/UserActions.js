
// METHOD 1 For getting dynamically added jquery dom elements
function timeslotClickHandler() {
    var available_container = document.getElementById("available");
    var selected_container = document.getElementById("selected");
    console.log(available_container);

    const element = this;
    console.log("element.classList:", element.classList);
    const classlist_array = [...element.classList];
    const day = classlist_array[1];

    
    const selected_day_exists = (day) => {
        var selected_days = [...selected_container.querySelectorAll(`.body1.header.${day}`)];
        var selected_day = Array.from(selected_days.filter((e) => {
            return e.classList.value.indexOf(day) >= 0;
        }));

        if (selected_days.length > 0)  return selected_day[0];
        else console.log(`No header found for ${day}; `); return false;
        
    }

    if (available_container.contains(element)) {
        element.classList.add("selected");
        var fragment = document.createDocumentFragment().appendChild(element);;

        var day_header = selected_day_exists(day);
        if (day_header == false) {
            day_header = document.createElement("div");
            day_header.textContent = day;
            day_header.classList.add('body1', 'header', day);
            selected_container.appendChild(day_header);
        }
        else{
            console.log("Headers found; ");
            day_header = selected_days[0];
            // selected_container.appendChild(header);
        }
        day_header.after(fragment);
    }
    else if (selected_container.contains(element)) {
        this.classList.remove("selected");
        console.log("Wagwan Father", classlist_array);
        const og_box = $(`#${day}`).first().find('.rectangle');
        og_box.append(element);
    }
}

// function timeslotsClickHandler(){
//     const element = this;
//     const parent = this.parent;
//     console.log("Hot girls have cold hearts");
//     console.log(element);
//     const origin_card_element = this.origin_card.getElementRectangle();
//     const destination_card_element = this.destination_card.getElementRectangle();
//     // if (this.parent == this.origin_card){
//     //     destination_card_element.appendChild(this.element);
//     // }
//     // else if (this.parent == this.destination_card){
//     //     origin_card_element.appendChild(this.element);
//     // }
// }

// $(document).ready(() => {
//     $("#available-container").ready(function () {
//         var timeslots = document.getElementsByClassName("timeslot");
//         for (var i = 0; i < timeslots.length; i++) {
//             timeslots[i].addEventListener('click', timeslotsClickHandler);
//         }
//     });
// })
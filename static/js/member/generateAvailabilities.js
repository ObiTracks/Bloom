// console.log(jsonTimeslots);
const stage = document.getElementById('stage');

{/* <div class="container-card style4" id="available-container"></div> */}

$(document).ready(
    function generateAvailabilities() {

        var container_card = document.createElement('div');
            container_card.classList.add('container-card', 'style4');
            container_card.setAttribute('id', 'available');
        stage.appendChild(container_card);

        jsonTimeslots.forEach((obj) => {
            // var timeslotsHTML;
            

            // cardHTML = `
            // <div class="availability-card" id="${obj.day}">
            //     <div class="header2 color-shade-grey">${obj.day}</div>
            //     <div class="body1 color-shade-grey">MM/DD/YYYY</div>
            //     <div class="rectangle">
            //         ${timeslotsHTML}
            //         <div class="timeslot ">
            //             <div class="body2">{{timeslot}}</div>
            //         </div>
            //     </div>
            // </div>`

            var availability_card = document.createElement('div');
            availability_card.classList.add('availability-card');
            availability_card.setAttribute('id', `${obj.day}`);
            let unwrap = ({day, index}) => ({day, index});
            availability_card.setAttribute('data', `${JSON.stringify(unwrap(obj))}`);
            availability_card.innerHTML = `
                <div class="header2 color-shade-grey">${obj.day}</div>
                <div class="body1 color-shade-grey">MM/DD/YYYY</div>
            `;

            var rectangle = document.createElement('div');
            rectangle.classList.add('rectangle');

            obj.slots.forEach(slot => {
                var window = slot.window;
                // var str = `<div class="timeslot">\n<div class="body2">\n` 
                // + window[0] + ` - ` + window[1] + `\n</div>\n</div>\n\n`;
                // // console.log(timeslotsHTML);

                // timeslotsHTML += str;

                var time_slot = document.createElement('div');
                time_slot.classList.add('timeslot', `${obj.day}`);
                time_slot.setAttribute('data', `${JSON.stringify(slot)}`);
                time_slot.innerHTML = `
                <div class="body2">${window[0]} - ${window[1]}</div>
               `;
               rectangle.appendChild(time_slot);
            })

            container_card.appendChild(availability_card);
            availability_card.appendChild(rectangle);



        }
    );
});

// 1:1 refactor of generateAvailabilities.js
import {Card, Timeslot} from './Classes.js';

var card = new Card(null, 'Sun', 'Some Date');
console.log(card.getDate());

$(document).ready(() => {
    loadAvailabilities();
});

function loadAvailabilities() {
    const container_card = document.getElementById('available');
    const staging_card = document.getElementById('selected');

    const createAvailabilityCard = (day_obj) => {
        const unwrap = ({ day, index }) => ({ day, index });
        const card = document.createElement('div');
        const rectangle = document.createElement('div');

        card.classList.add('availability-card');
        card.setAttribute('id', `${day_obj.day}`);
        card.setAttribute('data', `${JSON.stringify(unwrap(day_obj))}`);
        card.innerHTML = `
                <div class="header2 color-shade-grey">${day_obj.day}</div>
                <div class="body1 color-shade-grey">MM/DD/YYYYkydktdrtj</div>
            `;

        rectangle.classList.add('rectangle');
        card.appendChild(rectangle);
        return card;
    };

    const createTimeslotCard = (slot_obj) => {
        const window = slot_obj.window;
        const day = slot_obj.day;
        var timeslot = document.createElement('div');
        timeslot.classList.add('timeslot', `${day}`);
        timeslot.setAttribute('data', `${JSON.stringify(slot_obj)}`);
        timeslot.innerHTML = `
            <div class="body2">${window[0]} - ${window[1]}</div>
           `;
        return timeslot;
    }
    console.log(AmenityJSON);

    for (var i = 0; i < AmenityJSON.length; i++){
        const obj = AmenityJSON[i];
        const slots = obj.slots
        console.log(obj.day);
        
        const card = new Card(obj.day, "Date", obj.slots, container_card);
        card.attachElementToParent(); 
        slots.forEach(slot => {
            var timeslot = new Timeslot(slot.window, slot.capacity, card, staging_card);
            // timeslot.attachEventHandler();
            card.appendTimeslotToSelf(timeslot);
        })

    }
};

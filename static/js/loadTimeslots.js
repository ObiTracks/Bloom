
container = $("#available-timeslots")

container.text(JSON.stringify(jsonTimeslots));
// container.text("welhl");
console.log(jsonTimeslots);


for (var day in jsonTimeslots){
    var timeslotsArray = jsonTimeslots[day];
    var cardHTML = `
    <div class="card" id="timeslots-${day}">
        ${day}
    </div>
    `;
    container.append(cardHTML);

    var dayCard = $(`#timeslots-${day}`, day);
    console.log(timeslotsArray);
    // dayCard.append(timeslotsHTML)

    dayCard.append(`<span>${timeslotsArray.toString()}</span>`);


    // for (var timeslots in jsonTimeslots[day]){
    //     var timeslotsHTML = `<span>${timeslots}</span>`;
    //     dayCard.append(timeslotsHTML);
    // }

    


};
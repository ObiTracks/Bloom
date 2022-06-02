// console.log(jsonTimeslots);
var container = $("#container");

$(document).ready(
    function generateAvailabilities() {
        jsonTimeslots.forEach((obj) => {
            var timeslotsHTML;

            obj.slots.forEach(slot => {
                var window = slot.window;
                var str = `<div class="timeslot">\n<div class="body2">\n` 
                + window[0] + ` - ` + window[1] + `\n</div>\n</div>\n\n`
                console.log(timeslotsHTML);

                timeslotsHTML += str;
            })

            cardHTML = `
            <div class="availability-card" id="${obj.day}">
                <div class="header2 color-shade-grey">${obj.day}</div>
                <div class="body1 color-shade-grey">MM/DD/YYYY</div>
                <div class="rectangle">
                    ${timeslotsHTML}
                    <div class="timeslot ">
                        <div class="body2">{{timeslot}}</div>
                    </div>
                </div>
            </div>`

            // var cardBody = $(`#${obj}`);
            container.append(cardHTML);


        }
        // Object.entries(timeslotJson).forEach(function ([day, windows]) {
        //     column_index = tableHeaders.filter(function (x) {
        //         return $(this).text() == day;
        //     }).first().index();

        //     windows.forEach(function (window) {
        //         curr_timeslot = timeConverter(window[0], "f");
        //         timeslot_end = timeConverter(window[1], "f");

        //         while (curr_timeslot <= timeslot_end) {
        //             row = tableRows.filter(function (x) {
        //                 return $(this).children().eq(0).text() == timeConverter(curr_timeslot, "s");
        //             }).first()
        //             cell = row.children().eq(column_index)
        //             cell.addClass("selected")

        //             curr_timeslot = curr_timeslot + (15 / 60);
        //         }
        //     })
        // }
    );
});

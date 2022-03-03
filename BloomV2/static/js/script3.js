// For preselecting the timeslot picker table with an objects saved timeslots
//Accesses timeslotJSON variable from script tag added in the html page


$("#table").on('click','table>tbody>tr>td', function() {  });
function loadTable() {
    var x = $("#table tr");
    var timeslotJson = timeslotJson;


    console.log("Length", x);
}

loadTable();
// $(document).ready(loadTable());



// var tableHeaders = $("#table thead th");
// var testHead = "Mon"

// var columnCells = ""



// var day = tableHeaders.eq(cell.index()).text();
// var timeslot = cell.parent().children().eq(0).text().trim();
// var test = timeConverter(timeslot, "f")

// if (!timeslotsDict.has(day)) {
//     timeslotsDict.set(day, [timeslot]);
//     var timeslots = timeslotsDict.get(day);
//     // console.log(day, timeslots);

// } else {
//     var timeslots = timeslotsDict.get(day);
//     timeslots.push(timeslot);
//     // console.log(day, timeslots);
// }


// var json = getSelectedTimeslotIntervals(timeslotsDict);
// console.log(json);
// $("#results").text(JSON.stringify(json));
// $("#id_timeslots").text(JSON.stringify(json));
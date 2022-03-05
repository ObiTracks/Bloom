// METHOD 1 For getting dynamically added jquery dom elements

$("table").ready(function () {
    var tableBody = null;
    var tableRows = $(this).find("tbody tr");
    console.log("Yeo", tableRows);
});


function preLoadTable() {
    console.log("Table rows ", tableRows.length);
}

preLoadTable();
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
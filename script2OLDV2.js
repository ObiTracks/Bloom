var table = $("#table");

var isMouseDown = false;
var startRowIndex = null;
var startCellIndex = null;

var maxSelectionRange = new Set(); //Used to change the
var lastSelection = new Set(); //Used to change the
var currentSelection = new Set();

var timeslotsDict = new Map();
var windows = [];


function selectTo(cell) {
    var row = cell.parent();
    var cellIndex = cell.index();
    var rowIndex = row.index();

    var rowStart, rowEnd, cellStart, cellEnd;

    if (rowIndex < startRowIndex) {
        rowStart = rowIndex;
        rowEnd = startRowIndex;
    } else {
        rowStart = startRowIndex;
        rowEnd = rowIndex;
    }

    if (cellIndex < startCellIndex) {
        cellStart = cellIndex;
        cellEnd = startCellIndex;
    } else {
        cellStart = startCellIndex;
        cellEnd = cellIndex;
    }


    lastSelection = new Set(currentSelection);
    currentSelection.clear();
    for (var i = rowStart; i <= rowEnd; i++) {
        // var rowCells = table.find("tr").eq(i).find("td");
        var rowCells = table.find("tr").slice(1).eq(i).find("td"); //Removing the first item from each row (the rowheader) to prevent cell selection offset
        for (var j = cellStart; j <= cellEnd; j++) {

            // console.log("Iterated cell");
            cell = rowCells.eq(j);
            index = "" + i + j
            tuple = [index, cell];
            lastSelectionIndicies = [...lastSelection].map(tuple => {
                // console.log(tuple[0]);
                return tuple[0];
            })

            if (cell.attr("class") == "rowheader") {
                return
            }

            currentSelection.add(tuple);
            if (!lastSelectionIndicies.includes(index)) {
                cell.toggleClass("selected");
                // console.log("Selected", tuple);
            } else {
                // console.log("Exists", tuple);
            }
        }
    }
    // console.log("LastSelection Set:", lastSelection.size);
    // console.log("CurrentSelection Set:", currentSelection.size);
}

function findSetDifferenceAndToggle(set1, set2) {
    var diff = null; //For finding items that are no longer in the current range but were in the previous larger range

    if (set1.size > set2.size) { // If the range has reduced back in size, toggle the items that left it back to their original state
        set1Array = [...set1];
        set1Array_numbers = set1Array.map(x => {
            return x[0];
        });
        set2Array = [...set2];
        set2Array_numbers = set2Array.map(x => {
            return x[0];
        });

        diff = set1Array.filter(x => {
            var n = x[0];
            return !set2Array_numbers.includes(n);
        });
    }
    return diff;
}


table.on({ // Binding objects that weren't added to the DOM on the page load to event handle
    "mousedown": function (e) {

        // table.find("td").mousedown(function (e) {
        console.log("Mouse Clicked Down ");
        lastSelection.clear();
        currentSelection.clear();
        isMouseDown = true;
        var cell = $(this);

        if (e.shiftKey) {
            // console.log("Eureka");
            selectTo(cell);
        } else {
            startCellIndex = cell.index();
            startRowIndex = cell.parent().index();
            selectTo(cell);

        }
        return false; // prevent text selection
    },
    "mouseover": function () {
        if (!isMouseDown) {
            return
        };

        selectTo($(this));

        if (lastSelection.size > currentSelection.size) { //The range reduced in size, so we need to toggle the cells that left it back
            // console.log("Reducing size");
            diff = findSetDifferenceAndToggle(lastSelection, currentSelection);
            diff.forEach(item => {
                // console.log("\tOut of Range: ", item);
                item[1].toggleClass("selected");
            })
        }
        // getSchedule();


    },
}, "td").bind("selectstart", function () {
    return false;
});


$(document).ready($(document).mouseup(function () {
    isMouseDown = false;
}));





$("#showresults").click(
    function getTimeslots() {
        console.clear();
        timeslotsDict = new Map();
        var tableHeaders = $("#table thead th");
        var selectedCells = $("#table td.selected");

        selectedCells.each(function () {
            cell = $(this);
            var day = tableHeaders.eq(cell.index()).text();
            var timeslot = cell.parent().children().eq(0).text().trim();
            var test = timeStringToFloat(timeslot)

            if (!timeslotsDict.has(day)) {
                timeslotsDict.set(day, [timeslot]);
                var timeslots = timeslotsDict.get(day);
                // console.log(day, timeslots);

            } else {
                var timeslots = timeslotsDict.get(day);
                timeslots.push(timeslot);
                // console.log(day, timeslots);
            }
        });

        var windows = getSelectedTimeslotIntervals(timeslotsDict);
        console.log(windows);
        $("#results").text(windows);
    });

console.log(timeslotsDict);

function isGap(curr, stack) {
    result = false;
    if (stack.length >= 1) {
        result = (curr - stack[stack.length - 1]) > 1
    }

    // console.log("Checking Gap in Stack: ", stack, stack[stack.length - 1], result);
    // console.log(result);
    return result;
}

function getSelectedTimeslotIntervals(dict) {

    dict.forEach(

        function (timeslots, day) { // Going through each day and its selected timeslots
            var intervals = timeslots.map(function (x) {
                // console.log("YEOOO", x);
                return parseInt(x, 10);
            })
            // intervals.forEach(x => {
            //     console.log(x);
            // })


            var i = 0;
            var n = timeslots.length;
            var stack = [];

            while (i < n) {
                var curr = intervals[i];
                is_gap = isGap(curr, stack);

                if (is_gap) {
                    if (stack.length == 1) {
                        stack.push(stack[stack.length - 1])
                    }
                    windows.push(stack)
                    stack = [];
                }

                if (i == (n - 1)) {
                    if (stack.length == 0) {
                        stack.push(curr);
                    }
                    if (stack.length >= 2) {
                        stack.pop();
                    }

                    windows.push(stack);
                }

                while (stack.length >= 2) {
                    stack.pop();
                }

                stack.push(curr);


                i++;
            }
            console.log("Day: ", day, " Windows: ", windows);
            console.log("End");
        })

    return windows;
}

function timeStringToFloat(time) {
    var hoursMinutes = time.split(/[.:]/);
    var hours = parseInt(hoursMinutes[0], 10);
    var minutes = hoursMinutes[1] ? parseInt(hoursMinutes[1], 10) : 0;
    return hours + minutes / 60;
}
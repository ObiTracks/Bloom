var table = $("#table");

var isMouseDown = false;
var startRowIndex = null;
var startCellIndex = null;

var maxSelectionRange = new Set(); //Used to change the
var lastSelection = new Set(); //Used to change the
var currentSelection = new Set();

var timeslotsDict = new Map();
// var windows = [];
var resultsDict = {};


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
    // function collectSelectedSlots() {
    //     console.clear();
    //     timeslotsDict = new Map();
    //     var tableHeaders = $("#table thead th");
    //     var selectedCells = $("#table td.selected");

    //     selectedCells.each(function () {
    //         cell = $(this);
    //         var day = tableHeaders.eq(cell.index()).text();
    //         var timeslot = cell.parent().children().eq(0).text().trim();
    //         var test = timeConverter(timeslot, "f")

    //         if (!timeslotsDict.has(day)) {
    //             timeslotsDict.set(day, [timeslot]);
    //             var timeslots = timeslotsDict.get(day);
    //             // console.log(day, timeslots);

    //         } else {
    //             var timeslots = timeslotsDict.get(day);
    //             timeslots.push(timeslot);
    //             // console.log(day, timeslots);
    //         }
    //     });

    //     var json = getSelectedTimeslotIntervals(timeslotsDict);
    //     console.log(json);
    //     $("#results").text(JSON.stringify(json));
    //     $("#id_timeslots").text(JSON.stringify(json));

        
    //     showForms();
    // });
    () => {
        updateJSON();
    }

);
    

function updateJSON(){
    console.clear();
    var selectedTimeslots = collectSelectedSlots();
    var consolidatedJSON = getSelectedTimeslotIntervals(selectedTimeslots);
    var finalizedJSON = summarizeJSON(consolidatedJSON);

    console.log("Consolidated JSON: ", consolidatedJSON);
    $("#results").text(JSON.stringify(finalizedJSON));
    $("#id_timeslots").text(JSON.stringify(finalizedJSON));
    // showForms();
    return
};

// STEP 1
function collectSelectedSlots() {
    console.log("COLLECTING SELECTED SLOTS\n---------------------\n\n\n");
    
    function createDayObject(index, day){
        obj = {
            'day' : day,
            'index' : index,
            'slots' : [],
        }
        return (obj)
    }
    function createSlot(index, day){
        slot = {
            "current_capacity": 0,
            "window":[]
        }
        return (slot)
    }
    
    timeslotsDict = new Map();
    var tableHeaders = $("#table thead th");
    var selectedCells = $("#table td.selected");
    var temp_slot = [];
    var updatedJSON = [];

    selectedCells.each(function () {
        cell = $(this);
        var index = cell.index()
        var day = tableHeaders.eq(index).text();
        var timestamp = cell.parent().children().eq(0).text().trim();
        var test = timeConverter(timestamp, "f")

        

        // // console.log("timestamp:", timestamp)
        // if (!jsonTimeslots.some(item => item.hasOwnProperty(day))){
        //     dayObj = createDayObject(index, day);
        //     updatedJSON.push(dayObj);
        //     temp_slot.push(timestamp)
            
        //     // console.log("Wakanda")
        //     // This code creates the json object for day that there are timeslots selected for
            
            
        //     // if (dayObj['slots'].some(item => !item.hasOwnProperty('current_capacity'))) {
        //     //     obj['slots']['current_capacity'] = "0";
        //     // }
        //     // if (!obj.hasOwnProperty('current_capacity')) {
        //     //     obj['current_capacity'] = "0";
        //     // }
        // }
        // else{
        //     var dayObj = get_day_object_or_create_one(jsonArray, key)
        //     var dayObj = jsonTimeslots.find(item => item.day === day)
        //     // updatedJSON.push(dayObj);
        //     temp_slot.push(timestamp)
        // }

        if (!timeslotsDict.has(day)) {
            timeslotsDict.set(day, [timestamp]);
            var timeslots = timeslotsDict.get(day);
            // console.log(day, timeslots);

        } else {
            var timeslots = timeslotsDict.get(day);

            temp_slot.push(timestamp)
            timeslots.push(timestamp);
            // console.log(day, timeslots);
        }
    });
    console.log(timeslotsDict);
    return(timeslotsDict)
    
}
// STEP 2
function getSelectedTimeslotIntervals(selectedTimeslots) {
    console.log("GENERATING TIMESLOT INTERVALS\n-------------------------\n\n\n");
    console.log("Selected Timeslots: ", selectedTimeslots);
    function isGap(curr, stack, interval) {
        result = false;
        if (stack.length >= 1) {
            result = (curr - stack[stack.length - 1]) > interval;
        }
    
        // console.log("Checking Gap in Stack: ", stack, stack[stack.length - 1], result);
        // console.log(result);
        return result;
    }
    

    selectedTimeslots.forEach((timeslots, day) => { // Going through each day and its selected timeslots
        console.log("Day & Timeslots", day, timeslots);
    
        var windows = []; //Initializing the windows array
        var stack = []; //Initializing the stack
        var intervals = timeslots.map((x) =>{
            x = timeConverter(x, "f");
            // console.log("YEOOO", x);
            return x;
        })
        var interval = 0.25; // 15 minutes/60minutes
        var i = 0;
        var n = timeslots.length;
        var stack = [];

        while (i < n) {
            var curr = intervals[i];
            is_gap = isGap(curr, stack, interval);

            if (is_gap) {
                if (stack.length == 1) {
                    stack.push(stack[stack.length - 1])
                }
                windows.push(stack)
                stack = [];
            }

            if (i == (n - 1)) { //Last index of the array
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
            // console.log(curr);
            stack.push(curr);

            i++;
        }

        resultsDict[day] = windows;
        // console.log(resultsDict);
        // console.log("Day: ", day, " Windows: ", windows);
        console.log("End");
    })


    for (var key in resultsDict) {
        var day_ = key;
        var windows_ = resultsDict[day_]

        // console.log("Day: ", day_, "Windows: ", windows_);
        for (var i = 0; i < windows_.length; i++) {
            window_ = windows_[i];
            // console.log("WINDOW", window_.length);

            for (var n = 0; n < window_.length; n++) {
                window_[n] = timeConverter(window_[n], "s");
            }
        }

    }
    var consolidatedJSON = JSON.parse(JSON.stringify(resultsDict));

    return (consolidatedJSON);
}
// STEP 3
function summarizeJSON(consolidatedJSON){
    function arrays_are_equal(a, b){
        if (a === b) return true;
        if (a == null || b == null) return false;
        if (a.length !== b.length) return false;

        a.forEach((x, i) => {
            if(x != b[i]){
                return false
            }

        })
        return true;
    }
    function check_if_slot_exists_and_pop(obj, slot){
        var obj_slots = obj["slots"];

        obj_slots.forEach((item, i) => {
            if (arrays_are_equal(item, slot)){
                console.log("Slots Equal\n\n");
                console.log(obj);
                console.log(slot);

                obj_slots.pop(curr_slot); 
                return true;
            }
        })
        
        return false;
    }
    function create_slot(arr){
        var slot = {
            "current_capacity": 0,
            "window":arr
        }
        
        return slot;
    }

    console.log("SUMMARIZING JSON UPDATES\n-------------------------\n\n\n");
    // console.log("Consolidated JSON: ", consolidatedJSON);
    // console.log("Loaded Amenity JSON: ", jsonTimeslots);
    updatedJSON = [];
    // console.log(consolidatedJSON);

    for(var day of Object.keys(consolidatedJSON)){

        // 1. Check if the amenity json contains the dame day object
        //          If not, create a new day object and save in a varaible for building out
        //          If so, get that object and copy it into a variable

        // 2. Add all the timeslots to the saved object variable's "slot" array
        //          If the object's "slot" array already contains the timeslot, skip past it
        //          If not add the timeslot to the object

        var obj = get_object_or_create_one(jsonTimeslots, 'day', day);
        var collected_slots = consolidatedJSON[day];
        
        slots = obj["slots"];
        for (i=0; i < collected_slots.length; i++){
            var curr_slot = collected_slots[i];
            var slot_exists = check_if_slot_exists_and_pop(obj, curr_slot);
            var slot;
            
            if (slot_exists == false){
                
                slot = create_slot(curr_slot);
            }
            slots.push(slot);
        }

        updatedJSON.push(obj);


    }

    console.log("Updated Json", updatedJSON);
    return updatedJSON;

}

function timeConverter(time, convertTotype) {
    if (!convertTotype || convertTotype == "f") {
        var hoursMinutes = time.split(/[.:]/);
        var hours = parseInt(hoursMinutes[0], 10);
        var minutes = hoursMinutes[1] ? parseInt(hoursMinutes[1], 10) : 0;
        return hours + minutes / 60;
    } else if (convertTotype == "s") {
        var hours = Math.floor(time);
        hours = hours < 10 ? "0" + hours : "" + hours;

        var minutes = "" + Math.abs(hours - time);
        minutes = minutes == 0 ? "00" : 60 * minutes;
        time = hours + ":" + minutes;

        return time
    }
}

// UTILITY FUNCTIONS
function get_object_or_create_one(jsonArray, search_key, search_value){
    const day_indices = [['Sun',1],['Mon',2],['Tues',3],['Wed',4],['Thurs',5],['Fri',6],['Sat',7]]
    var jsonArray = JSON.parse(JSON.stringify(jsonArray));

    for(i=0; i < jsonArray.length; i++){
        obj = jsonArray[i];
        if(obj[search_key] === search_value){
            return(obj);
        }
    }

    obj = {
        'day' : search_value,
        'index' : day_indices.find((item) => {return item[0] === search_value})[1],
        'slots' : [],
    }
    return (obj);
}

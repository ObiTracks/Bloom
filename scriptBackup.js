var table = $("#table");

var isMouseDown = false;
var startRowIndex = null;
var startCellIndex = null;

var pastSelectedCellSet = new Set(); //Used to change the
var currentSelectedCellSet = new Set(); //Used to change the
var tempCellSet = new Set();



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


    
    for (var i = rowStart; i <= rowEnd; i++) {
        // var rowCells = table.find("tr").eq(i).find("td");
        var rowCells = table.find("tr").slice(1).eq(i).find("td"); //Removing the first item from each row (the rowheader) to prevent cell selection offset
        for (var j = cellStart; j <= cellEnd; j++) {

            console.log("Iterated cell");
            cell = rowCells.eq(j);
            tuple = ["" + i + j, cell];
            
            if (pastSelectedCellSet.has(tuple) == false && currentSelectedCellSet.has(tuple) == false) {

                cell.toggleClass("selected");
                currentSelectedCellSet.add(tuple);
                // pastSelectedCellSet.add(tuple);
            }
        }
    }

    if (pastSelectedCellSet.size > currentSelectedCellSet.size) {
        console.log("Reducing size")
        diff = findSetDifferenceAndToggle(pastSelectedCellSet, currentSelectedCellSet);
        diff.forEach(item => {
            console.log(item);
            item[1].toggleClass("selected");
        })
    }
    console.log("Past Set: ", pastSelectedCellSet.size, "\nCurrent Set:", currentSelectedCellSet.size);
    pastSelectedCellSet = new Set(currentSelectedCellSet);
    currentSelectedCellSet.clear();


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

        // console.log("Difference: ");
        // diff.forEach(e => {
        //     console.log(e);
        //     e[1].toggleClass("selected");
        // })

    }
    return diff;
}

table.find("td").mousedown(function (e) {
        // console.log("Mouse Clicked Down ");

        currentSelectedCellSet.clear();
        pastSelectedCellSet.clear();
        isMouseDown = true;
        var cell = $(this);
        // table.find(".selected").removeClass("selected"); // deselect everything

        if (e.shiftKey) {
            console.log("Eureka");
            selectTo(cell);
        } else {
            // currentSelectedCellSet.clear();
            cell.toggleClass("selected");
            // currentSelectedCellSet.add(cell)
            startCellIndex = cell.index();
            startRowIndex = cell.parent().index();
        }


        return false; // prevent text selection
    })
    .mouseover(function () {
        if (!isMouseDown) {
            return
        };
        console.log("Mouse Moved over ");
        selectTo($(this));
        // pastSelectedCellSet = new Set(); //Used to change the
        // currentSelectedCellSet = new Set(); //Used to change the
    })
    .bind("selectstart", function () {
        return false;
    });

$(document).mouseup(function () {
    isMouseDown = false;
    console.log("Mouse released  ");

});

$("#showresults").click(function () {
    $("#results").text("Hello")

    var $heads = $('#table thead th').slice(1);
    // $heads = $heads.slice(1);

    //iterate over each selected item
    var array = $('#table td.selected').map(function () {
        var $this = $(this);
        //for each item find the first td in the same row and the header element at the same index
        return $this.parent().children().eq(0).text() + ' ' + $heads.eq($this.index()).text();
    }).get()
    // console.log(array)
})
var table = $("#table");

$(document).ready(
    function generateTable() {

        // var thead = table.find("thead");
        table.html(`
            <thead>
                <tr>
                    <th class="rowheader"></th>
                    <th>Sun</th>
                    <th>Mon</th>
                    <th>Tues</th>
                    <th>Wed</th>
                    <th>Thurs</th>
                    <th>Fri</th>
                    <th>Sat</th>    
                </tr>
            </thead>
        `);
        table.append(`
            <tbody>
            </tbody>
        `);
        var tableBody = $("tbody");
        var n = 0;

        for (var i = 0; i <= 23; i++) {
            var html;
            hour = ((i / 10 < 1) ? "0" + i : i);

            for (var n = 0; n <= 3; n++) {
                var minutes = (n * 15).toString();
                minutes = n == 0 ? minutes + "0" : minutes;

                var rowclass = (n == 0 ? "rowhour" : "");

                html = `
                <tr class=${rowclass}>
                    <td class="rowheader">${hour}:${minutes}</td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                `

                tableBody.append(html);
            }
        }

    });
document.head = document.head || document.getElementsByTagName('head')[0];

var total_money = 100;

var days = 0;
var new_week = true;
var week = 1;
var bets = [];
bets.push(['2019-06-28','SKT vs KZ','First Dragon','$20','$12']);    
bets.push(['2019-06-30','JAG vs DWG','First Turret','$20','$0']); 
bets.push(['2019-07-02','SKT vs JAG','First Dragon','$20','$15']);
bets.push(['2019-07-05','JAG vs KZ','First Dragon','$20','$10']);
bets.push(['2019-07-06','SKT vs DWG','First Blood','$20','$0']);
bets.push(['2019-07-11','GEN.G vs KZ','First Baron','$20','$13']);
bets.push(['2019-07-12','SKT vs KZ','First Dragon','$20','$12']); 
bets.push(['2019-07-13','JAG vs KZ','First Dragon','$20','$10']);
bets.push(['2019-07-15','DWG vs GEN.G','First Turret','$20','$22']);

function create_history() {
    var history_table = '<table id="bet_history_table">';
    history_table = '<thead><tr><th>Date</th><th>Match</th><th>Objective</th><th>Bet Amount</th><th>Outcome</th><th>Total</th></tr></thead><tbody>';
    history_table += '<tr><td colspan="6";>';
    history_table += '<b>'
    history_table += 'Week ' + week;
    history_table += '</b>'
    history_table += '</td></tr>';

    // Calculate days
    for (i = 0; i < bets.length; i++) { 
        if (i > 0) {
            if (bets[i-1][0].split("-")[0] == bets[i][0].split("-")[0]) {
                if (bets[i][0].split("-")[1] > bets[i-1][0].split("-")[1]) {
                    if (bets[i-1][0].split("-")[1] == '01') { // January - 31 days
                        days = days + +(31 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '02') { // February - 28 days in a common year and 29 days in leap years
                        if (bets[i][0].split("-")[0] % 4 === 0) {
                            days = days + +(29 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                        } else { 
                            days = days + +(28 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                        }
                    } else if (bets[i-1][0].split("-")[1] == '03') { // March - 31 days
                        days = days + +(31 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '04') { // April - 30 days
                        days = days + +(30 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '05') { // May - 31 days
                        days = days + +(31 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '06') { // June - 30 days
                        days = days + +(30 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '07') { // July - 31 days
                        days = days + +(31 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '08') { // August - 31 days
                        days = days + +(30 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '09') { // September - 30 days
                        days = days + +(30 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '10') { // October - 31 days
                        days = days + +(31 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else if (bets[i-1][0].split("-")[1] == '11') { // November - 30 days
                        days = days + +(30 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    } else { // December - 31 days
                        days = days + +(31 - +bets[i-1][0].split("-")[2]) + +bets[i][0].split("-")[2]
                    }
                } else {
                    if (bets[i][0].split("-")[2] > bets[i-1][0].split("-")[2]) {
                        days = days + (bets[i][0].split("-")[2] - bets[i-1][0].split("-")[2]);
                    }
                }
            } else {
                // If year changes
            }
        }

        if (days >= 7) {
            days = 0;
            new_week = true;
        } else {
            new_week = false;
        }
        
        if (new_week == true) {
            week = week + 1;
            history_table += '<tr>';
            history_table += '<td colspan="6";>';
            history_table += '<b>'
            history_table += 'Week ' + week;
            history_table += '</b>'
            history_table += '</td>';
            history_table += '</tr>';
            new_week = false;
        }

        if (bets[i][4].split("$")[1] > 0) {
            history_table += '<tr bgcolor="#008000">';
        } else {
            history_table += '<tr bgcolor="#FF0000">';
        }

        history_table += '<td>';
        history_table += bets[i][0];
        history_table += '</td>';

        history_table += '<td>';
        history_table += bets[i][1];
        history_table += '</td>';

        history_table += '<td>';
        history_table += bets[i][2];
        history_table += '</td>';

        history_table += '<td>';
        history_table += bets[i][3];
        history_table += '</td>';

        history_table += '<td>';
        if (bets[i][4].split("$")[1] > 0) {
            history_table += '+' + bets[i][4];
        } else {
            history_table += '-' + bets[i][3];
        }
        history_table += '</td>';

        history_table += '<td>';
        if (bets[i][4].split("$")[1] > 0) {
            history_table += total_money = +total_money + +bets[i][4].split("$")[1];
        } else {
            history_table += total_money = +total_money - +bets[i][3].split("$")[1];
        }
        history_table += '</td>';

        history_table += '</tr>';
    }

    history_table+='</tbody></table>';
    $('#historyDiv').html(history_table);   
}

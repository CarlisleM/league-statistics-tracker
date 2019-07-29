document.head = document.head || document.getElementsByTagName('head')[0];

var total_money = 100;

var days = 0;
var new_week = true;
var week = 1;
var bets = [];
bets.push(['2019-07-24','Origen BCN vs Team Queso','OBCN First Blood','$20','$0']);    
bets.push(['2019-07-25','SKT vs GEN.G','SKT First Turret','$20','$0']); 
bets.push(['2019-07-27','Kingzone DragonX vs Afreeca Freecs','KZ First Dragon','$20','$0']); 
bets.push(['2019-07-27','Splyce vs S04','SPY First Dragon','$20','$16.80']); 
bets.push(['2019-07-28','Optic vs Golden Guardians','OPT First Tower','$6','$0']); 
bets.push(['2019-07-28','Team Liquid vs Cloud9','TL First Dragon','$30','$21.30']); 
bets.push(['2019-07-28','Clutch Gaming vs Flyquest','CG First Tower','$20','$15.60']); 
bets.push(['2019-07-29','G2 Heretics vs Movistar Riders','G2 First Blood','$20','$15.20']); 
bets.push(['2019-08-01','DAMWON Gaming vs Afreeca Freecs','DWG First Dragon','$20','$0']); 
bets.push(['2019-08-02','Griffin vs SANDBOX Gaming','GRF First Tower','$20','$0']);
bets.push(['2019-08-02','Fnatic vs Schalke 04','FNC First Blood','$2.90','$0']);
bets.push(['2019-08-03','G2 vs Fnatic','G2 First Tower','$20','$0']);
bets.push(['2019-08-03','Schalke 04 vs Origen','S04 First Dragon','$20','$0']);
bets.push(['2019-08-03','Schalke 04 vs Origen','S04 First Baron','$20','$0']);

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
            history_table += total_money = +total_money.toFixed(2) + +bets[i][4].split("$")[1];
        } else {
            history_table += total_money = +total_money.toFixed(2) - +bets[i][3].split("$")[1];
        }
        history_table += '</td>';

        history_table += '</tr>';
    }

    history_table+='</tbody></table>';
    $('#historyDiv').html(history_table);   
}

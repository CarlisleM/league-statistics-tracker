document.head = document.head || document.getElementsByTagName('head')[0];

function fetchJSONFile(path, callback) {
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200) {
                var data = JSON.parse(httpRequest.responseText);
                if (callback) callback(data);
            }
        }
    };

    httpRequest.open('GET', 'https://league-statistics-tracker.herokuapp.com/games');
    httpRequest.send();
}

function display_match_stats(team_1, team_2) {
    change_team_one_select(team_1);
    change_team_one_select(team_2);
}

// Table one
function change_team_one_select(selected_team) {
    var number_of_games = 0;
    var k = 0;
    var table_one_body = '<table class="team_results" id="team_one_table" border="0" cellpadding="0" cellspacing="0">';
    table_one_body += '<thead><tr><th>Game Date</th><th>VS</th><th>FB</th><th>FT</th><th>FD</th><th>FI</th><th>FBaron</th><th>W/L</th></tr></thead><tbody>';

    //fetchJSONFile('matches_played.json', function(data) {
    fetchJSONFile('my_data_dump.json', function(data) {
        for(j in data.matches) {
           if (((league == data.matches[k].league_id) && (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team)) || ((league == 0) && (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team))) {
            // if (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team) {
                number_of_games = number_of_games + 1;

                table_one_body += '<tr>';

                table_one_body += '<td>';
                table_one_body += data.matches[k].game_date.split("T")[0];
                table_one_body += '</td>';

                table_one_body += '<td>';
                if (selected_team == data.matches[k].blue_team) {
                    table_one_body += data.matches[k].red_team;
                } else { 
                    table_one_body += data.matches[k].blue_team;
                }
                table_one_body += '</td>';

                if (selected_team == data.matches[k].first_blood) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (selected_team == data.matches[k].first_tower) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (selected_team == data.matches[k].first_dragon) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (selected_team == data.matches[k].first_inhibitor) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (selected_team == data.matches[k].first_baron) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (selected_team == data.matches[k].winner) {
                    table_one_body += '<td style="background-color: DeepSkyBlue; color:black; border-right: 1px solid black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black; border-right: 1px solid black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                table_one_body += '</tr>';
            }
            k++;
        }        

        var fb_array = [];
        var ft_array = [];
        var fd_array = [];
        var fi_array = [];
        var fbaron_array = [];
        var win_array = [];

        for (i = 0; i < (data.matches).length; i++) { 
            if (data.matches[i].blue_team == selected_team || data.matches[i].red_team == selected_team) {
                fb_array.push(data.matches[i].first_blood);
                ft_array.push(data.matches[i].first_tower);
                fd_array.push(data.matches[i].first_dragon);
                fi_array.push(data.matches[i].first_inhibitor)
                fbaron_array.push(data.matches[i].first_baron);
                win_array.push(data.matches[i].winner);
            } 
        }

        fb_array = fb_array.slice(-1 * 10);
        ft_array = ft_array.slice(-1 * 10);
        fd_array = fd_array.slice(-1 * 10);
        fi_array = fi_array.slice(-1 * 10);
        fbaron_array = fbaron_array.slice(-1 * 10);
        win_array = win_array.slice(-1 * 10);

        var fb_count = 0;
        var ft_count = 0;
        var fd_count = 0;
        var fi_count = 0;
        var fbaron_count = 0;
        var win_count = 0;

        for(var i = 0; i < 10; ++i){
            if (fb_array[i] == selected_team) {
                fb_count++;
            }
            if (ft_array[i] == selected_team) {
                ft_count++;
            }
            if (fd_array[i] == selected_team) {
                fd_count++;
            }
            if (fi_array[i] == selected_team) {
                fi_count++;
            }
            if (fbaron_array[i] == selected_team) {
                fbaron_count++;
            }
            if (win_array[i] == selected_team) {
                win_count++;
            }
        }

        table_one_body += '<tr>';
        table_one_body += '<td colspan=2></td>';

        table_one_body += '<td>';
        table_one_body += fb_count + '0%';
        table_one_body += '</td>'
        
        table_one_body += '<td>';
        table_one_body += ft_count + '0%';
        table_one_body += '</td>'

        table_one_body += '<td>';
        table_one_body += fd_count + '0%';
        table_one_body += '</td>'

        table_one_body += '<td>';
        table_one_body += fi_count + '0%';
        table_one_body += '</td>'

        table_one_body += '<td>';
        table_one_body += fbaron_count + '0%';
        table_one_body += '</td>'

        table_one_body += '<td style="border-right: 1px solid black;">';
        table_one_body += win_count + '0%';
        table_one_body += '</td>'

        table_one_body += '</tr>';

        table_one_body+='</tbody></table>';
        $('#tableDiv').html(table_one_body);

        var x = document.getElementById("tableDiv");
        if (x.style.display == "none") {
            x.style.display = "block";
        }      

        const thElements = tableDiv.getElementsByTagName('th'),
              tdElements = tableDiv.getElementsByTagName('td');

        for (let i = 0; i < thElements.length; i++) {
            const widerElement = thElements[i].offsetWidth > tdElements[i].offsetWidth ? thElements[i] : tdElements[i],
            width = window.getComputedStyle(widerElement).width;
            thElements[i].style.width = tdElements[i].style.width = width;
        }

        var objDiv = document.getElementById('tableDiv');   
        objDiv.scrollTop = objDiv.scrollHeight;

    });
}

// Table two
function change_team_two_select(selected_team) {
    var k = 0;
    var table_two_body = '<table class="team_results" id="team_two_table" border="0" cellpadding="0" cellspacing="0">';
    table_two_body += '<thead><tr><th>Game Date</th><th>VS</th><th>FB</th><th>FT</th><th>FD</th><th>FI</th><th>FBaron</th><th>W/L</th></tr></thead><tbody>';

    fetchJSONFile('my_data_dump.json', function(data) {
        for(j in data.matches) {
            if (((league == data.matches[k].league_id) && (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team)) || ((league == 0) && (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team))) {
                table_two_body += '<tr>';

                table_two_body += '<td>';
                table_two_body += data.matches[k].game_date.split("T")[0];
                table_two_body += '</td>';

                table_two_body += '<td>';
                if (selected_team == data.matches[k].blue_team) {
                    table_two_body += data.matches[k].red_team;
                } else { 
                    table_two_body += data.matches[k].blue_team;
                }
                table_two_body += '</td>';

                if (selected_team == data.matches[k].first_blood) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (selected_team == data.matches[k].first_tower) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (selected_team == data.matches[k].first_dragon) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (selected_team == data.matches[k].first_inhibitor) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (selected_team == data.matches[k].first_baron) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (selected_team == data.matches[k].winner) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black; border-right: 1px solid black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black; border-right: 1px solid black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                table_two_body += '</tr>';
            }
            k++;
        }

        var fb_array = [];
        var ft_array = [];
        var fd_array = [];
        var fi_array = [];
        var fbaron_array = [];
        var win_array = [];

        for (i = 0; i < (data.matches).length; i++) { 
            if (data.matches[i].blue_team == selected_team || data.matches[i].red_team == selected_team) {
                fb_array.push(data.matches[i].first_blood);
                ft_array.push(data.matches[i].first_tower);
                fd_array.push(data.matches[i].first_dragon);
                fi_array.push(data.matches[i].first_inhibitor)
                fbaron_array.push(data.matches[i].first_baron);
                win_array.push(data.matches[i].winner);
            } 
        }

        fb_array = fb_array.slice(-1 * 10);
        ft_array = ft_array.slice(-1 * 10);
        fd_array = fd_array.slice(-1 * 10);
        fi_array = fi_array.slice(-1 * 10);
        fbaron_array = fbaron_array.slice(-1 * 10);
        win_array = win_array.slice(-1 * 10);

        var fb_count = 0;
        var ft_count = 0;
        var fd_count = 0;
        var fi_count = 0;
        var fbaron_count = 0;
        var win_count = 0;

        for(var i = 0; i < 10; ++i){
            if (fb_array[i] == selected_team) {
                fb_count++;
            }
            if (ft_array[i] == selected_team) {
                ft_count++;
            }
            if (fd_array[i] == selected_team) {
                fd_count++;
            }
            if (fi_array[i] == selected_team) {
                fi_count++;
            }
            if (fbaron_array[i] == selected_team) {
                fbaron_count++;
            }
            if (win_array[i] == selected_team) {
                win_count++;
            }
        }

        table_two_body += '<tr>';
        table_two_body += '<td colspan=2></td>';

        table_two_body += '<td>';
        table_two_body += fb_count + '0%';
        table_two_body += '</td>'
        
        table_two_body += '<td>';
        table_two_body += ft_count + '0%';
        table_two_body += '</td>'

        table_two_body += '<td>';
        table_two_body += fd_count + '0%';
        table_two_body += '</td>'

        table_two_body += '<td>';
        table_two_body += fi_count + '0%';
        table_two_body += '</td>'

        table_two_body += '<td>';
        table_two_body += fbaron_count + '0%';
        table_two_body += '</td>'

        table_two_body += '<td style="border-right: 1px solid black;">';
        table_two_body += win_count + '0%';
        table_two_body += '</td>'

        table_two_body+='</tbody></table>';
        $('#tableDiv2').html(table_two_body);

        var x = document.getElementById("tableDiv2");
        if (x.style.display == "none") {
            x.style.display = "block";
        }

        const thElements = tableDiv2.getElementsByTagName('th'),
              tdElements = tableDiv2.getElementsByTagName('td');

        for (let i = 0; i < thElements.length; i++) {
            const widerElement = thElements[i].offsetWidth > tdElements[i].offsetWidth ? thElements[i] : tdElements[i],
            width = window.getComputedStyle(widerElement).width;
            thElements[i].style.width = tdElements[i].style.width = width;
        }
    });
} 
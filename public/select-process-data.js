document.head = document.head || document.getElementsByTagName('head')[0];

var db = require('./public/collect-data')

// Site logo
function changeFavicon(src) {
    var link = document.createElement('link'),
    oldLink = document.getElementById('dynamic-favicon');
    link.id = 'dynamic-favicon';
    link.rel = 'shortcut icon';
    link.href = src;
    if (oldLink) {
        document.head.removeChild(oldLink);
    }
    document.head.appendChild(link);
}

changeFavicon('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3773894d-0ef2-416b-b2b8-dd34a5086e30/datwehc-379c8f4a-786b-40cd-979f-b22cd7b59782.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzM3NzM4OTRkLTBlZjItNDE2Yi1iMmI4LWRkMzRhNTA4NmUzMFwvZGF0d2VoYy0zNzljOGY0YS03ODZiLTQwY2QtOTc5Zi1iMjJjZDdiNTk3ODIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.CGJoLp7X540QYBJeyOFiedL0ljbK1tr3dTB-jr_GqSQ');

// Get json data
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
    httpRequest.open('GET', 'league-statistics-tracker.herokuapp.com/games');
    // httpRequest.open('GET', 'https://api.myjson.com/bins/12fvuj');
    // https://api.myjson.com/bins/iuo1f
    // http://localhost:5000/games
    httpRequest.send(); 
}

function change_team_options() {
    var number_of_options = document.querySelector('#team_one_select').options;
    var options_length = number_of_options.length;

    var x = document.getElementById("tableDiv");
    if (x.style.display != "none") {
        x.style.display = "none";
    }
    var x = document.getElementById("tableDiv2");
    if (x.style.display != "none") {
        x.style.display = "none";
    }

    for(var i=0; i<options_length; i++) {
      if (i != 0) {
           document.querySelector('#team_one_select').remove(1);
           document.querySelector('#team_two_select').remove(1);
        }
    }

    if (document.querySelector('#select_league').selectedOptions[0].text == 'LCK') {
        var teams = {
            skt : 'SK Telecom T1',
            jag : 'Jin Air Green Wings',
            dwg : 'DAMWON Gaming',
            gen : 'Gen.G',
            af : 'Afreeca Freecs',
            sb : 'SANDBOX Gaming',
            hle : 'Hanwha Life Esports',
            grf : 'Griffin',
            kt : 'KT Rolster',
            kz : 'KINGZONE DragonX'
        };
    }  else if (document.querySelector('#select_league').selectedOptions[0].text == 'LEC') {
        var teams = {
            fnc : 'Fnatic',
            g2 : 'G2 Esports',
            vit : 'Team Vitality',
            sk : 'SK Gaming',
            og : 'Origen',
            msf : 'Misfits',
            s04 : 'Schalke 04',
            xl : 'Excel Esports',
            rge : 'Rogue',
            spy : 'Splyce'
        };
    } else if (document.querySelector('#select_league').selectedOptions[0].text == 'OPL') {
        var teams = {
            av : 'Avant Gaming',
            dw : 'Dire Wolves',
            ord : 'ORDER',
            lgc : 'Legacy',
            mmm : 'MAMMOTH',
            grv : 'Gravitas',
            bmr : 'Bombers',
            chf : 'Chiefs Esports Club'
        };
    } else if (document.querySelector('#select_league').selectedOptions[0].text == 'LFL') {
        var teams = {
            ldlc : 'LDLC',
            'vit.b' : 'Vitality.Bee',
            'msf.p' : 'Misfits Premier',
            aaa : 'against All authority',
            rog : 'ROG Esport',
            go : 'Gamers Origin',
            sly : 'Solary',
            mces : 'Team MCES'
        };
    } else if (document.querySelector('#select_league').selectedOptions[0].text == 'LVP') {
        var teams = {
            g2h : 'G2 Heretics',
            s2v : 'S2V Esports',
            mrs : 'Movistar Riders',
            emz : 'eMonkeyz',
            x6 : 'x6tence',
            mad : 'MAD Lions',
            gia : 'Vodafone Giants',
            pgm : 'Penguins',
            ogb : 'Origen BCN',
            svp : 'Splyce Vipers',
            tq : 'Team Queso'
        };
    } else if (document.querySelector('#select_league').selectedOptions[0].text == 'LMS') {
        var teams = {

        };
    } else {
        var teams = {
            skt : 'SK Telecom T1',
            jag : 'Jin Air Green Wings',
            dwg : 'DAMWON Gaming',
            gen : 'Gen.G',
            af : 'Afreeca Freecs',
            sb : 'SANDBOX Gaming',
            hle : 'Hanwha Life Esports',
            grf : 'Griffin',
            kt : 'KT Rolster',
            kz : 'KINGZONE DragonX',
            fnc : 'Fnatic',
            g2 : 'G2 Esports',
            vit : 'Team Vitality',
            sk : 'SK Gaming',
            og : 'Origen',
            msf : 'Misfits',
            s04 : 'Schalke 04',
            xl : 'Excel Esports',
            rge : 'Rogue',
            spy : 'Splyce',
            av : 'Avant Gaming',
            dw : 'Dire Wolves',
            ord : 'ORDER',
            lgc : 'Legacy',
            mmm : 'MAMMOTH',
            grv : 'Gravitas',
            bmr : 'Bombers',
            chf : 'Chiefs Esports Club',
            ldlc : 'LDLC',
            'vit.b' : 'Vitality.Bee',
            'msf.p' : 'Misfits Premier',
            aaa : 'against All authority',
            rog : 'ROG Esport',
            go : 'Gamers Origin',
            sly : 'Solary',
            mces : 'Team MCES',
            g2h : 'G2 Heretics',
            s2v : 'S2V Esports',
            mrs : 'Movistar Riders',
            emz : 'eMonkeyz',
            x6 : 'x6tence',
            mad : 'MAD Lions',
            gia : 'Vodafone Giants',
            pgm : 'Penguins',
            ogb : 'Origen BCN',
            svp : 'Splyce Vipers',
            tq : 'Team Queso'
        };
    }

    var select = document.getElementById("team_one_select");
    for(index in teams) {
        select.options[select.options.length] = new Option(teams[index], index);
    }

    var select = document.getElementById("team_two_select");
    for(index in teams) {
        select.options[select.options.length] = new Option(teams[index], index);
    }
}

// Table one
function change_team_one_select(sel) {
    var k = 0;
    var table_one_body = '<table border="1" id="team_two_table"><thead><tr><th>Game Date</th><th>VS</th><th>FB</th><th>FT</th><th>FD</th><th>FI</th><th>FBaron</th><th>W/L</th></tr></thead><tbody>';
    fetchJSONFile('my_data_dump.json', function(data) {
        for(j in data.matches) {
            if (data.matches[k].blue_team == sel || data.matches[k].red_team == sel) {

                table_one_body += '<tr class="one">';

                table_one_body += '<td>';
                table_one_body += data.matches[k].game_date.split("T")[0];
                table_one_body += '</td>';

                table_one_body += '<td>';
                if (sel == data.matches[k].blue_team) {
                    table_one_body += data.matches[k].red_team;
                } else { 
                    table_one_body += data.matches[k].blue_team;
                }
                table_one_body += '</td>';

                table_one_body += '<td style="display:none;">';
                if (sel == data.matches[k].blue_team) {
                    table_one_body += data.matches[k].blue_team;
                } else { 
                    table_one_body += data.matches[k].red_team;
                }
                table_one_body += '</td>';

                if (sel == data.matches[k].first_blood) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (sel == data.matches[k].first_tower) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (sel == data.matches[k].first_dragon) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (sel == data.matches[k].first_inhibitor) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (sel == data.matches[k].first_baron) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                if (sel == data.matches[k].winner) {
                    table_one_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_one_body += '✓';
                } else {
                    table_one_body += '<td style="background-color:red;color:black;">';
                    table_one_body += '✘';
                }
                table_one_body += '</td>';

                table_one_body += '</tr>';
            }
            k++;
        }

        table_one_body+='</tbody></table>';
        $('#tableDiv').html(table_one_body);

        var x = document.getElementById("tableDiv");
        if (x.style.display == "none") {
            x.style.display = "block";
        }      
    });
}

// Table two
function change_team_two_select(sel) {
    var k = 0;
    var table_two_body = '<table border="1" id="team_two_table"><thead><tr><th>Game Date</th><th>VS</th><th>FB</th><th>FT</th><th>FD</th><th>FI</th><th>FBaron</th><th>W/L</th></tr></thead><tbody>';
    fetchJSONFile('my_data_dump.json', function(data) {
        for(j in data.matches) {
            if (data.matches[k].blue_team == sel || data.matches[k].red_team == sel) {

                table_two_body += '<tr class="one">';

                table_two_body += '<td>';
                table_two_body += data.matches[k].game_date.split("T")[0];
                table_two_body += '</td>';

                table_two_body += '<td>';
                if (sel == data.matches[k].blue_team) {
                    table_two_body += data.matches[k].red_team;
                } else { 
                    table_two_body += data.matches[k].blue_team;
                }
                table_two_body += '</td>';

                table_two_body += '<td style="display:none;">';
                if (sel == data.matches[k].blue_team) {
                    table_two_body += data.matches[k].blue_team;
                } else { 
                    table_two_body += data.matches[k].red_team;
                }
                table_two_body += '</td>';

                if (sel == data.matches[k].first_blood) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (sel == data.matches[k].first_tower) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (sel == data.matches[k].first_dragon) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (sel == data.matches[k].first_inhibitor) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (sel == data.matches[k].first_baron) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                if (sel == data.matches[k].winner) {
                    table_two_body += '<td style="background-color:DeepSkyBlue;color:black;">';
                    table_two_body += '✓';
                } else {
                    table_two_body += '<td style="background-color:red;color:black;">';
                    table_two_body += '✘';
                }
                table_two_body += '</td>';

                table_two_body += '</tr>';
            }
            k++;
        }

        table_two_body+='</tbody></table>';
        $('#tableDiv2').html(table_two_body);

        var x = document.getElementById("tableDiv2");
        if (x.style.display == "none") {
            x.style.display = "block";
        }      
    });
} 
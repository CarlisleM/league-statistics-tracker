document.head = document.head || document.getElementsByTagName('head')[0];

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

 //   httpRequest.open('GET', 'https://league-statistics-tracker.herokuapp.com/games');
    httpRequest.open('GET', 'http://localhost:5000/games');
    httpRequest.send(); 
}

function change_team_options(leaguename) {
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
    
    if (leaguename == 'LCK') {
        document.getElementById("league").innerHTML = "LCK";
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
    }  else if (leaguename == 'LEC') {
        document.getElementById("league").innerHTML = "LEC";
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
    } else if (leaguename == 'OPL') {
        document.getElementById("league").innerHTML = "OPL";
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
    } else if (leaguename == 'LFL') {
        document.getElementById("league").innerHTML = "LFL";
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
    } else if (leaguename == 'LVP') {
        document.getElementById("league").innerHTML = "LVP";
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
    } else if (leaguename == 'LMS') {
        document.getElementById("league").innerHTML = "LMS";
        var teams = {
            mad : 'MAD Team',
            fw : 'Flash Wolves',
            jt : 'J Team',
            ahq : 'ahq e-Sports Club',
            hka : 'Hong Kong Attitude',
            grx : 'G-Rex',
            alf : 'Alpha Esports',
            dg : 'Dragon Gate Team'
        };
    } else if (leaguename == 'LCS') {
        document.getElementById("league").innerHTML = "LCS";
        var teams = {
          tl : 'Team Liquid',
          clg : 'Counter Logic Gaming',
          c9 : 'Cloud9',
          tsm : 'Team SoloMid',
          ggs : 'Golden Guardians',
          opt : 'OpTic Gaming',
          '100' : '100 Thieves',
          cg : 'Clutch Gaming',
          fly : 'FlyQuest',
          fox : 'Echo Fox'
        };
    } else if (leaguename == 'NA_Academy_League') {
        document.getElementById("league").innerHTML = "NA_Academy_League";
        var teams = {
            'tl.a' : 'Team Liquid Academy',
            'clg.a' : 'Counter Logic Gaming Academy',
            'c9.a' : 'Cloud9 Academy',
            'tsm.a' : 'Team SoloMid Academy',
            'ggs.a' : 'Golden Guardians Academy',
            'opt.a' : 'OpTic Gaming Academy',
            '100.a' : '100 Thieves Academy',
            'cg.a' : 'Clutch Gaming Academy',
            'fly.a' : 'FlyQuest Academy',
            'fox.a' : 'Echo Fox Academy'
        };
    } else if (leaguename == 'LLA') {
        document.getElementById("league").innerHTML = "LLA";
        var teams = {
          isg : 'Isurus Gaming',
          ak : 'All Knights',
          fg : 'Furious Gaming',
          inf : 'Infinity Esports',
          r7 : 'Rainbow7',
          xten : 'XTEN Esports',
          klg : 'Kaos Latin Gamers',
          pix : 'Pixel Esports Club'
        };
    } else if (leaguename == 'Ultraliga') {
        document.getElementById("league").innerHTML = "Ultraliga";
        var teams = {
          rec : 'Rogue Esports Club',
          dv1 : 'devils.one',
          prd : 'PRIDE',
          ave : 'AVEZ Esport',
          ihg : 'Illuminar Gaming',
          apr : 'piratesports',
          pct : 'ACTINA PACT',
          wp : 'Wisla Plock eSports'
        };
    }  else {
        document.getElementById("league").innerHTML = "All Leagues";
        var teams = {
            skt : 'SK Telecom T1',
            dwg : 'DAMWON Gaming',
            grf : 'Griffin',
            fnc : 'Fnatic',
            g2 : 'G2 Esports',
            spy : 'Splyce',
            jt : 'J Team',
            ahq : 'ahq e-Sports Club',
            hka : 'Hong Kong Attitude',
            tl : 'Team Liquid',
            c9 : 'Cloud9',
            cg : 'Clutch Gaming',
            ig : 'Invictus Gaming',
            rng : 'Royal Never Give Up',
            gam : 'GAM Esports',
            fpx : 'FunPlus Phoenix'
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
function change_team_one_select(selected_team) {
    if (document.getElementById("league").innerHTML == "LCK") {
        var league = 1;
    } else if (document.getElementById("league").innerHTML == "LEC") { 
        var league = 2;
    } else if (document.getElementById("league").innerHTML == "OPL") { 
        var league = 3;
    } else if (document.getElementById("league").innerHTML == "LFL") { 
        var league = 4;
    } else if (document.getElementById("league").innerHTML == "LVP") { 
        var league = 5;
    } else if (document.getElementById("league").innerHTML == "LMS") { 
        var league = 6;
    } else if (document.getElementById("league").innerHTML == "LCS") { 
        var league = 7;
    }  else if (document.getElementById("league").innerHTML == "LLA") { 
        var league = 8;
    }  else if (document.getElementById("league").innerHTML == "Ultraliga") { 
        var league = 9;
    }  else {
        var league = 0;
    }

    var number_of_games = 0;
    var k = 0;
    var table_one_body = '<table class="team_results" id="team_one_table" border="0" cellpadding="0" cellspacing="0">';
    table_one_body += '<thead><tr><th>Game Date</th><th>VS</th><th>FB</th><th>FT</th><th>FD</th><th>FI</th><th>FBaron</th><th>W/L</th></tr></thead><tbody>';
    fetchJSONFile('my_data_dump.json', function(data) {
        for(j in data.matches) {
            if (((league == data.matches[k].league_id) && (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team)) || ((league == 0) && (data.matches[k].blue_team == selected_team || data.matches[k].red_team == selected_team))) {

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
    if (document.getElementById("league").innerHTML == "LCK") {
        var league = 1;
    } else if (document.getElementById("league").innerHTML == "LEC") { 
        var league = 2;
    } else if (document.getElementById("league").innerHTML == "OPL") { 
        var league = 3;
    } else if (document.getElementById("league").innerHTML == "LFL") { 
        var league = 4;
    } else if (document.getElementById("league").innerHTML == "LVP") { 
        var league = 5;
    } else if (document.getElementById("league").innerHTML == "LMS") { 
        var league = 6;
    } else if (document.getElementById("league").innerHTML == "LCS") { 
        var league = 7;
    }  else if (document.getElementById("league").innerHTML == "LLA") { 
        var league = 8;
    }  else if (document.getElementById("league").innerHTML == "Ultraliga") { 
        var league = 9;
    }  else {
        var league = 0;
    }

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
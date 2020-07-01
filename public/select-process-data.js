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

    httpRequest.open('GET', 'https://league-statistics-tracker.herokuapp.com/games');
    httpRequest.send();
}

function testFetch(path, callback) {
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200) {
                var data = JSON.parse(httpRequest.responseText);
                if (callback) callback(data);
            }
        }
    };

    httpRequest.open('GET', 'https://league-statistics-tracker.herokuapp.com/upcoming');
    httpRequest.send();
}

function isOdd(num) { return num % 2;}

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
        var current_league = 2;
        document.getElementById("league").innerHTML = "LCK";
        var teams = {
            drx : 'DRX',
            sb : 'SANDBOX Gaming',
            gen : 'Gen.G',
            sp : 'SeolHaeOne Prince',
            t1 : 'T1',
            kt : 'KT Rolster',
            dwg : 'DAMWON Gaming',
            hle : 'Hanwha Life Esports',
            af : 'Afreeca Freecs',
            dyn : 'Team Dynamics'
        };
    }  else if (leaguename == 'LEC') {
        var current_league = 3;
        document.getElementById("league").innerHTML = "LEC";
        var teams = {
            msf : 'Misfits Gaming',
            xl : 'Excel Esports',
            rge : 'Rogue',
            vit : 'Team Vitality',
            fnc : 'Fnatic',
            og : 'Origen',
            g2 : 'G2 Esports',
            sk : 'SK Gaming',
            s04 : 'FC Schalke 04',
            mad : 'MAD Lions'
        };
    } else if (leaguename == 'OPL') {
        var current_league = 4;
        document.getElementById("league").innerHTML = "OPL";
        var teams = {
            lgc : 'Legacy',
            grv : 'Gravitas',
            mmm : 'MAMMOTH',
            pgg : 'Pentanet.GG',
            av : 'Avant Gaming',
            ord : 'ORDER',
            dw : 'Dire Wolves',
            chf : 'Chiefs Esports Club'
        };
    } else if (leaguename == 'LFL') {
        var current_league = 5;
        document.getElementById("league").innerHTML = "LFL";
        var teams = {
            'msf.p' : 'Misfits Premier',
            sly : 'Solary',
            ldlc : 'LDLC OL',
            mces : 'Team MCES',
            go : 'GamersOrigin',
            gw : 'GameWard',
            id : 'Izi Dream',
            'vit.b' : 'Vitality.Bee'
        };
    } else if (leaguename == 'LVP_SuperLiga_Orange') {
        var current_league = 6;
        document.getElementById("league").innerHTML = "LVP_SuperLiga_Orange";
        var teams = {
            bts : 'Cream Real Betis',
            emz : 'eMonkeyz',
            mrs : 'Movistar Riders',
            g2ar : 'G2 Arctic',
            vgia : 'Vodafone Giants',
            madm : 'MAD Lions Madrid',
            bcn : 'BCN Squad',
            s2v : 'S2V Esports',
            ucam : 'UCAM Esports Club',
            ttq : 'Team Queso'
        };
    } else if (leaguename == 'PCS') {
        var current_league = 7;
        document.getElementById("league").innerHTML = "PCS";
        var teams = {
            hka : 'Hong Kong Attitude',
            ahq : 'ahq eSports club',
            alf : 'Alpha Esports',
            jt : 'J Team',
            bjd : 'Berjaya Dragons',
            lyb : 'Liyab Esports',
            mcx : 'Machi Esports',
            nov : 'Nova Esports',
            psg : 'PSG Talon',
            rsg : 'Resurgence'
        };
    } else if (leaguename == 'LCS') {
        var current_league = 1;
        document.getElementById("league").innerHTML = "LCS";
        var teams = {
            tl : 'Team Liquid',
            clg : 'Counter Logic Gaming',
            c9 : 'Cloud9',
            tsm : 'Team SoloMid',
            gg : 'Golden Guardians',
            imt : 'Immortals',
            '100' : '100 Thieves',
            dig : 'Dignitas',
            fly : 'FlyQuest',
            eg : 'Evil Geniuses'
        };
    } else if (leaguename == 'NA_Academy_League') {
        var current_league = 11;
        document.getElementById("league").innerHTML = "NA_Academy_League";
        var teams = {
            'tl.a' : 'Team Liquid Academy',
            'clg.a' : 'Counter Logic Gaming Academy',
            'c9.a' : 'Cloud9 Academy',
            'tsm.a' : 'Team SoloMid Academy',
            'gg.a' : 'Golden Guardians Academy',
            'eg.a' : 'Evil Geniuses Academy',
            '100.a' : '100 Thieves Academy',
            'dig.a' : 'Dignitas Academy',
            'fly.a' : 'FlyQuest Academy',
            'imt.a' : 'Immortals Academy'
        };
    } else if (leaguename == 'LLA') {
        var current_league = 8;
        document.getElementById("league").innerHTML = "LLA";
        var teams = {
            isg : 'Isurus Gaming',
            ak : 'All Knights',
            fg : 'Furious Gaming',
            inf : 'Infinity Esports',
            r7 : 'Rainbow7',
            xtn : 'XTEN Esports',
            uch : 'Azules Esports',
            pix : 'Pixel Esports Club'
        };
    } else if (leaguename == 'Ultraliga') {
        var current_league = 9;
        document.getElementById("league").innerHTML = "Ultraliga";
        var teams = {
            ago : 'AGO ROGUE',
            '7pt' : '7more7 Pompa Team',
            prd : 'PRIDE',
            gg : "Gentlemen's Gaming",
            ihg : 'Illuminar Gaming',
            arr : 'piratesports',
            hit : 'Komputronik H34T',
            'k1ck' : 'K1CK Neosurf'
        };
    } else if (leaguename == 'LJL') {
        var current_league = 13;
        document.getElementById("league").innerHTML = "LJL";
        var teams = {
            'v3' : 'V3 Esports',
            sg : 'Sengoku Gaming',
            cga : 'Crest Gaming Act',
            dfm : 'DetonatioN FocusMe',
            shg : 'Fukuoka SoftBank Hawks gaming',
            axz : 'AXIZ',
            bc : 'Burning Core',
            rj : 'Rascal Jester'
        };
    } else if (leaguename == 'TCL') {
        var current_league = 14;
        document.getElementById("league").innerHTML = "TCL";
        var teams = {
            bjk : 'Beşiktaş Esports',
            dp : 'Dark Passage',
            gal : 'Galakticos',
            iw : 'Istanbul Wildcats',
            fb : '1907 Fenerbahçe',
            gs : 'Galatasaray Esports',
            '5r' : '5 Ronin',
            sup : 'Papara SuperMassive',
            ryl : 'Royal Youth',
            aur : 'Team AURORA'
        };
    } else if (leaguename == 'CBLOL') {
        var current_league = 16;
        document.getElementById("league").innerHTML = "CBLOL";
        var teams = {
            san : 'Santos e-Sports',
            kbm : 'KaBuM! e-Sports',
            png : 'paiN Gaming',
            itz : 'INTZ',
            fla : 'Flamengo eSports',
            fur : 'FURIA Esports',
            prg : 'Prodigy Esports',
            vk : 'Vivo Keyd'
        };
    } else if (leaguename == 'VCS') {
        var current_league = 15;
        document.getElementById("league").innerHTML = "VCS";
        var teams = {
            per : 'Percent Esports',
            opg : 'OverPower Esports',
            ces : 'CERBERUS Esports',
            evs : 'EVOS Esports',
            gam : 'GAM Esports',
            ts : 'Team Secret',
            sgb : 'Saigon Buffalo',
            fl : 'Team Flash'
        };
    }  else {
        document.getElementById("league").innerHTML = "All Leagues";
        var teams = {

        };
    }

    var match_buttons = document.querySelectorAll(".upcoming-match-button");

    for (var i = 0; i < match_buttons.length; i++) {
        match_buttons[i].remove();
    }

    var week_divs = document.querySelectorAll(".week_row");
    var match_divs = document.querySelectorAll(".match_row");

    for (var i = 0; i < week_divs.length; i++) {
        week_divs[i].remove();
    }

    for (var i = 0; i < match_divs.length; i++) {
        match_divs[i].remove();
    }

    test = 0;

    var k = 0;
    let body = document.getElementsByClassName("upcoming-matches")[0];
    testFetch('my_data_dump.json', function(data) {
        for(j in data.upcoming_matches) {
            if (data.upcoming_matches[k].league_id == current_league) {
                // Upcoming match div
                current_week = data.upcoming_matches[k-1].match_week;
                next_week = data.upcoming_matches[k].match_week;

                if (current_week != next_week || test == 0)
                {
                    var week = document.createElement("div");
                    week.setAttribute('class', 'week_row');
                    let week_text = document.createElement("week_text");
                    week_text.innerHTML = "Week " + data.upcoming_matches[k].match_week;
                    week.append(week_text);
                    body.appendChild(week);
                    test += 1;
                }

                var match = document.createElement("div");
                match.setAttribute('class', 'match_row');
                match.id = '' + data.upcoming_matches[k].blue_team + ' ' + data.upcoming_matches[k].red_team;

                var individual_team_1 = document.createElement("div");
                individual_team_1.setAttribute('class', 'match_column_1');
                
                body.appendChild(match);

                // Team 1
                let button_blue = document.createElement("button_blue");
                button_blue.innerHTML = '<img src="images/TeamLogos/' + data.upcoming_matches[k].blue_team + '.png" width="100" height="100" />';
                button_blue.id = '' + data.upcoming_matches[k].blue_team + ' ' + data.upcoming_matches[k].red_team;
                button_blue.className = 'upcoming-match-button';

                individual_team_1.appendChild(button_blue);
                match.appendChild(individual_team_1);

                // Date of match
                var upcoming_match_date = document.createElement("div");
                upcoming_match_date.setAttribute('class', 'match_column_2');
                
                var date = data.upcoming_matches[k].game_date.split("T")[0];
                date = date.split("-").reverse().join("-");
                upcoming_match_date.innerHTML = '<p>' + data.upcoming_matches[k].match_day + ' ' + date + ' '  + data.upcoming_matches[k].match_time + '</p>'
                match.appendChild(upcoming_match_date);

                // Team 2
                var individual_team_2 = document.createElement("div");
                individual_team_2.setAttribute('class', 'match_column_3');

                let button_red = document.createElement("button_red");
                button_red.innerHTML = '<img src="images/TeamLogos/' + data.upcoming_matches[k].red_team + '.png" width="100" height="100" />';
                button_red.id = '' + data.upcoming_matches[k].blue_team + ' ' + data.upcoming_matches[k].red_team;
                button_red.className = 'upcoming-match-button';

                individual_team_2.appendChild(button_red);
                match.appendChild(individual_team_2);

                match.onmousedown = function() {
                    var team_names = (this.id).split(" ");
                    change_team_one_select(team_names[0]);
                    change_team_two_select(team_names[1]);
                }
            }    
            k++;
        }
    });

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
    if (document.getElementById("league").innerHTML == "LCS") {
        var league = 1;
    } else if (document.getElementById("league").innerHTML == "LCK") { 
        var league = 2;
    } else if (document.getElementById("league").innerHTML == "LEC") { 
        var league = 3;
    } else if (document.getElementById("league").innerHTML == "OPL") { 
        var league = 4;
    } else if (document.getElementById("league").innerHTML == "LFL") { 
        var league = 5;
    } else if (document.getElementById("league").innerHTML == "LVP") { 
        var league = 6;
    } else if (document.getElementById("league").innerHTML == "PCS") { 
        var league = 7;
    }  else if (document.getElementById("league").innerHTML == "LLA") { 
        var league = 8;
    }  else if (document.getElementById("league").innerHTML == "Ultraliga") { 
        var league = 9;
    }  else if (document.getElementById("league").innerHTML == "NA_Academy_League") { 
        var league = 11;
    }  else if (document.getElementById("league").innerHTML == "LJL") { 
        var league = 13;
    }  else if (document.getElementById("league").innerHTML == "TCL") { 
        var league = 14;
    }  else if (document.getElementById("league").innerHTML == "VCS") { 
        var league = 15;
    }  else if (document.getElementById("league").innerHTML == "CBLOL") { 
        var league = 16;
    }  else {
        var league = 0;
    }

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
    if (document.getElementById("league").innerHTML == "LCS") {
        var league = 1;
    } else if (document.getElementById("league").innerHTML == "LCK") { 
        var league = 2;
    } else if (document.getElementById("league").innerHTML == "LEC") { 
        var league = 3;
    } else if (document.getElementById("league").innerHTML == "OPL") { 
        var league = 4;
    } else if (document.getElementById("league").innerHTML == "LFL") { 
        var league = 5;
    } else if (document.getElementById("league").innerHTML == "LVP") { 
        var league = 6;
    } else if (document.getElementById("league").innerHTML == "PCS") { 
        var league = 7;
    }  else if (document.getElementById("league").innerHTML == "LLA") { 
        var league = 8;
    }  else if (document.getElementById("league").innerHTML == "Ultraliga") { 
        var league = 9;
    }  else if (document.getElementById("league").innerHTML == "NA_Academy_League") { 
        var league = 11;
    }  else if (document.getElementById("league").innerHTML == "LJL") { 
        var league = 13;
    }  else if (document.getElementById("league").innerHTML == "TCL") { 
        var league = 14;
    }  else if (document.getElementById("league").innerHTML == "VCS") { 
        var league = 15;
    }  else if (document.getElementById("league").innerHTML == "CBLOL") { 
        var league = 16;
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
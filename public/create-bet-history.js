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
bets.push(['2019-08-01','DAMWON Gaming vs Afreeca Freecs','DWG First Dragon','$20','$14']); 
bets.push(['2019-08-02','Griffin vs SANDBOX Gaming','GRF First Tower','$20','$15.80']);
bets.push(['2019-08-02','Fnatic vs Schalke 04','FNC First Blood','$2.90','$1.94']); // Says lost? But shows winnings
bets.push(['2019-08-03','G2 vs Fnatic','G2 First Tower','$20','$13']);
bets.push(['2019-08-03','Schalke 04 vs Origen','S04 First Dragon','$20','$16.80']);
bets.push(['2019-08-03','Schalke 04 vs Origen','S04 First Baron','$20','$17.60']);
bets.push(['2019-08-03','CLG vs Optic','CLG First Dragon','$20','$14.80']);
bets.push(['2019-08-03','Clutch Gaming vs 100 Thieves','CG First Tower','$20','$16.80']);
bets.push(['2019-08-04','Hanwha Life Esports vs DAMWON Gaming','HLE First Blood Map 1','$20','$25.20']);
bets.push(['2019-08-04','Hanwha Life Esports vs DAMWON Gaming','HLE First Blood Map 2','$20','$25.20']);
bets.push(['2019-08-04','CLG vs 100 Thieves','CLG First Dragon','$29.80','$20.76']);
bets.push(['2019-08-04','Team Liquid vs Team SoloMid','TL First Dragon','$20','$12.80']);
bets.push(['2019-08-04','Golden Guardians vs Clutch Gaming','CG First Tower','$20','$18.40']);
bets.push(['2019-08-04','Echo Fox vs FlyQuest','EF First Tower','$20','$19.80']);
bets.push(['2019-08-04','CLG vs Cloud9','CLG First Dragon','$30','$0']);
bets.push(['2019-08-09','Afreeca Freecs vs SANDBOX Gaming ','AF First Tower Map 1','$20','$16.80']);
bets.push(['2019-08-09','SANDBOX Gaming vs Afreeca Freecs','SB First Dragon Map 1','$20','$0']);
bets.push(['2019-08-09','Afreeca Freecs vs SANDBOX Gaming ','AF First Tower Map 2','$20','$0']);
bets.push(['2019-08-09','SANDBOX Gaming vs Afreeca Freecs','SB First Dragon Map 2','$20','$16.80']);
bets.push(['2019-08-09','Griffin vs Gen.G','Griffin First Tower Map 1','$20','$15.20']);
bets.push(['2019-08-09','Griffin vs Gen.G','Griffin First Tower Map 2','$20','$15.20']);
bets.push(['2019-08-09','Team Vitality vs SK Gaming','Vitality First Tower','$20','$0']);
bets.push(['2019-08-09','Team Vitality vs SK Gaming','Vitality First Dragon','$20','$13.80']);
bets.push(['2019-08-09','Splyce vs Origen','Splyce First Blood','$20','$0']);
bets.push(['2019-08-09','Splyce vs Origen','Splyce First Tower','$20','$15.20']);
bets.push(['2019-08-09','Splyce vs Origen','Splyce First Dragon','$50','$0']);
bets.push(['2019-08-10','Team Vitality vs Fnatic','VIT First Dragon','$20','$0']);
bets.push(['2019-08-10','Clutch Gaming vs Team SoloMid','CG First Dragon Map 1','$20','$22.80']);
bets.push(['2019-08-10','Clutch Gaming vs Team SoloMid','CG First Dragon Map 2','$20','$20.60']);
bets.push(['2019-08-10','Clutch Gaming vs Team SoloMid','CG First Dragon Map 3','$20','$18.40']);
bets.push(['2019-08-11','Afreeca Freecs vs Gen.G','AF First Blood Map 1','$20','$17.20']);
bets.push(['2019-08-11','Afreeca Freecs vs Gen.G','AF First Tower Map 1','$20','$16.80']);
bets.push(['2019-08-11','Afreeca Freecs vs Gen.G','AF First Dragon Map 1','$20','$16.80']);
bets.push(['2019-08-11','Afreeca Freecs vs Gen.G','AF First Blood Map 2','$20','$0']);
bets.push(['2019-08-11','Afreeca Freecs vs Gen.G','AF First Tower Map 2','$20','$16.80']);
bets.push(['2019-08-11','Afreeca Freecs vs Gen.G','AF First Dragon Map 2','$20','$16.80']);
bets.push(['2019-08-11','Counter Logic Gaming vs Optic','CLG First Dragon Map 1','$20','$0']);
bets.push(['2019-08-11','Counter Logic Gaming vs Optic','CLG First Dragon Map 2','$20','$0']);
bets.push(['2019-08-11','Counter Logic Gaming vs Optic','CLG First Dragon Map 3','$20','$14.00']);
bets.push(['2019-08-15','SKT vs DAMWON Gaming','SKT First Blood Map 1','$20','$14.60']);
bets.push(['2019-08-15','DAMWON Gaming vs SKT','DWG First Dragon Map 1','$20','$0']);
bets.push(['2019-08-15','SKT vs DAMWON Gaming','SKT First Blood Map 2','$20','$0']);
bets.push(['2019-08-15','DAMWON Gaming vs SKT','DWG First Dragon Map 2','$20','$16.60']);
bets.push(['2019-08-15','SKT vs DAMWON Gaming','SKT First Blood Map 3','$20','$0']);
bets.push(['2019-08-15','DAMWON Gaming vs SKT','DWG First Dragon Map 3','$20','$0']);
bets.push(['2019-08-15','KT Rolster vs SANDBOX Gaming','KT First Blood Map 1','$30','$0']);
bets.push(['2019-08-15','KT Rolster vs SANDBOX Gaming','KT First Blood Map 2','$20','$18.40']);
bets.push(['2019-08-15','KT Rolster vs SANDBOX Gaming','KT First Blood Map 3','$20','$0']);
bets.push(['2019-08-16','Hanwha Life Esports vs Afreeca Freecs','HLE First Blood Map 1','$20','$0']);
bets.push(['2019-08-16','Hanwha Life Esports vs Afreeca Freecs','HLE First Blood Map 2','$20','$19.00']);
bets.push(['2019-08-16','Hanwha Life Esports vs Afreeca Freecs','HLE First Blood Map 3','$20','$0']);
bets.push(['2019-08-16','ORDER vs MAMMOTH','ORDER First Blood','$20','$0']);
bets.push(['2019-08-16','ORDER vs Chiefs','ORDER First Blood','$20','$0']);
bets.push(['2019-08-16','Misfits vs Team Vitality','MSF First Blood','$20','$21.60']);
bets.push(['2019-08-16','exceL vs SK Gaming','exceL First Dragon','$20','$0']);
bets.push(['2019-08-16','Splyce vs Fnatic','Splyce First Tower','$20','$18.60']);
bets.push(['2019-08-17','Legacy vs MAMMOTH','LGC First Blood','$7','$0']);
bets.push(['2019-08-17','Bombers vs Chiefs','BMR First Blood','$20','$20.40']);
bets.push(['2019-08-17','AVANT Gaming vs MAMMOTH','AVG First Blood','$20','$0']);
bets.push(['2019-08-17','Team Vitality vs Schalke 04','VIT First Dragon','$20','$18.40']);
bets.push(['2019-08-17','Cloud9 vs Counter Logic Gaming','C9 First Blood Map 1','$20','$16.00']);
bets.push(['2019-08-17','Counter Logic Gaming vs Cloud9','CLG First Dragon Map 1','$20','$0']);
bets.push(['2019-08-17','Cloud9 vs Counter Logic Gaming','C9 First Blood Map 2','$20','$16.00']);
bets.push(['2019-08-17','Counter Logic Gaming vs Cloud9','CLG First Dragon Map 2','$20','$0']);
bets.push(['2019-08-17','Cloud9 vs Counter Logic Gaming','C9 First Blood Map 3','$20','$16.00']);
bets.push(['2019-08-17','Counter Logic Gaming vs Cloud9','CLG First Dragon Map 3','$20','$0']);
bets.push(['2019-08-18','Hanwha Life Esports vs Griffin','HLE First Blood Map 1','$20','$0']);
bets.push(['2019-08-18','Hanwha Life Esports vs Griffin','HLE First Blood Map 2','$20','$0']);
bets.push(['2019-08-19','G2 Heretics vs Origen BCN','G2H Win','$20','$0']);
bets.push(['2019-08-21','Afreeca Freecs vs SKT','AF First Blood Map 1','$20','$17.20']);
bets.push(['2019-08-21','Afreeca Freecs vs SKT','AF First Tower Map 1','$30','$0']);
bets.push(['2019-08-21','Afreeca Freecs vs SKT','AF First Blood Map 2','$20','$17.20']);
bets.push(['2019-08-21','Afreeca Freecs vs SKT','AF First Dragon Map 2','$30','$28.20']);
bets.push(['2019-08-23','SKT vs SANDBOX Gaming','SKT First Dragon Map 1','$18.76','$14.26']);
bets.push(['2019-08-23','Hong Kong Attitude vs MAD Team','HKA Win','$30','$26.10']);
bets.push(['2019-08-23','Splyce vs Rogue','SPY First Blood Map 1','$20','$13.40']);
bets.push(['2019-08-23','Splyce vs Rogue','SPY First Dragon Map 1','$20','$0']);
bets.push(['2019-08-24','Billibilli Gaming vs EDward Gaming','BLG Win','$9.12','$6.29']);
bets.push(['2019-08-24','Team Vitality vs Schalke 04','VIT First Dragon Map 1','$30','$0']);
bets.push(['2019-08-24','Clutch Gaming vs Counter Logic Gaming','CG First Tower Map 1','$20','$16.80']);
bets.push(['2019-08-24','Clutch Gaming vs Counter Logic Gaming','CG First Tower Map 2','$20','$16.80']);
bets.push(['2019-08-24','Clutch Gaming vs Counter Logic Gaming','CG First Tower Map 3','$20','$0']);
bets.push(['2019-08-25','SKT vs DAMWON Gaming','SKT First Blood Map 1','$20','$17.20']);
bets.push(['2019-08-25','SKT vs DAMWON Gaming','SKT First Dragon Map 1','$20','$16.80']);
bets.push(['2019-08-25','Team Liquid vs Cloud9','TL First Dragon Map 1','$20','$13.80']);
bets.push(['2019-08-25','Team Liquid vs Cloud9','TL First Dragon Map 2','$20','$0']);
bets.push(['2019-08-25','Team Liquid vs Cloud9','TL First Dragon Map 3','$20','$0']);
bets.push(['2019-08-30','Chiefs vs MAMMOTH','Chiefs Win','$20','$0']);
bets.push(['2019-08-31','Fnatic vs G2 Esports','FNC First Dragon Map 1','$20','$0']);
bets.push(['2019-08-31','Fnatic vs G2 Esports','FNC First Dragon Map 2','$20','$24.00']);
bets.push(['2019-08-31','Griffin vs SKT','GRF First Dragon Map 1','$40','$33.60']);
bets.push(['2019-08-31','Griffin vs SKT','GRF First Dragon Map 2','$40','$33.60']);
bets.push(['2019-08-31','Griffin vs SKT','GRF First Dragon Map 3','$40','$33.60 ']);
bets.push(['2019-09-01','Vodafone Giants vs Origen BCN','GIA Win','$50','$31.00']);
bets.push(['2019-09-03','Afreeca Freecs vs Kingzone DragonX','AF First Blood Map 1','$20','$0']);
bets.push(['2019-09-03','Afreeca Freecs vs Kingzone DragonX','AF First Blood Map 2','$20','$0']);
bets.push(['2019-09-03','Afreeca Freecs vs Kingzone DragonX','AF First Blood Map 3','$20','$0']);
bets.push(['2019-09-03','Afreeca Freecs vs Kingzone DragonX','AF Win','$30','$0']);
bets.push(['2019-09-06','FlyQuest vs Clutch Gaming','FLY First Blood Map 1','$30','$30.00']);
bets.push(['2019-09-06','Clutch Gaming vs Flyquest','CG First Tower Map 1','$30','$20.70']);
bets.push(['2019-09-06','FlyQuest vs Clutch Gaming','FLY First Blood Map 2','$30','$30.00']);
bets.push(['2019-09-06','Clutch Gaming vs Flyquest','CG First Tower Map 2','$30','$0']);
bets.push(['2019-09-06','FlyQuest vs Clutch Gaming','FLY First Blood Map 3','$30','$30.00']);
bets.push(['2019-09-06','Clutch Gaming vs Flyquest','CG First Tower Map 3','$16','$11.04']);
bets.push(['2019-09-07','Kingzone DragonX vs DAMWON Gaming','KZ First Blood Map 1','$20','$0']);
bets.push(['2019-09-07','Kingzone DragonX vs DAMWON Gaming','KZ First Dragon Map 1','$20','$0']);
bets.push(['2019-09-07','Kingzone DragonX vs DAMWON Gaming','KZ First Blood Map 2','$20','$0']);
bets.push(['2019-09-07','Kingzone DragonX vs DAMWON Gaming','KZ First Dragon Map 2','$20','$0']);
bets.push(['2019-09-07','Kingzone DragonX vs DAMWON Gaming','KZ First Blood Map 3','$20','$0']);
bets.push(['2019-09-07','Kingzone DragonX vs DAMWON Gaming','KZ First Dragon Map 3','$20','$0']);
bets.push(['2019-09-07','Fnatic vs Schalke 04','FNC First Blood Map 1','$30','$21.00']);
bets.push(['2019-09-07','Fnatic vs Schalke 04','FNC First Blood Map 2','$30','$21.00']);
bets.push(['2019-09-07','Fnatic vs Schalke 04','FNC First Blood Map 3','$30','$21.00']);    
bets.push(['2019-09-08','G-Rex vs Hong Kong Attitude','GRX First Blood Map 1','$20','$16.60']);
bets.push(['2019-09-08','G-Rex vs Hong Kong Attitude','GRX First Blood Map 2','$20','$0']);
bets.push(['2019-09-08','Fnatic vs G2 Esports','FNC First Blood Map 1','$20','$14.00']);
bets.push(['2019-09-08','Fnatic vs G2 Esports','FNC First Dragon Map 1','$20','$20.20']);
bets.push(['2019-09-08','Fnatic vs G2 Esports','FNC First Blood Map 2','$20','$0']);
bets.push(['2019-09-08','Fnatic vs G2 Esports','FNC First Dragon Map 2','$20','$0']);
bets.push(['2019-09-08','Fnatic vs G2 Esports','FNC First Blood Map 3','$20','$0']);    
bets.push(['2019-09-08','Fnatic vs G2 Esports','FNC First Dragon Map 3','$20','$0']);
bets.push(['2019-09-09','APK Prince vs Jin Air','APK First Blood Map 1','$20','$17.00']); 
bets.push(['2019-09-09','APK Prince vs Jin Air','APK First Tower Map 1','$20','$0']); 
bets.push(['2019-09-09','APK Prince vs Jin Air','APK First Blood Map 2','$20','$0']); 
bets.push(['2019-09-09','APK Prince vs Jin Air','APK to win','$30','$34.50']); 
bets.push(['2019-09-10','Hanwa Life Esports vs Dynamics','HLE First Blood Map 1','$20','$13.20']);
bets.push(['2019-09-10','Hanwa Life Esports vs Dynamics','HLE First Blood Map 2','$20','$12.20']); 
bets.push(['2019-09-10','Hanwa Life Esports vs Dynamics','HLE First Blood Map 3','$20','$0']);  
bets.push(['2019-09-10','Hanwa Life Esports vs Dynamics','DYN to not win a map','$30','$0']); 
bets.push(['2019-09-11','Hanwa Life Esports vs Jin Air','HLE First Blood Map 1','$20','$15.60']);
bets.push(['2019-09-11','Hanwa Life Esports vs Jin Air','HLE First Tower Map 1','$20','$0']);
bets.push(['2019-09-11','Hanwa Life Esports vs Jin Air','HLE First Blood Map 2','$20','$15.60']); 
bets.push(['2019-09-11','Hanwa Life Esports vs Jin Air','HLE First Tower Map 2','$15.25','$0']); 
bets.push(['2019-09-12','Origen BCN vs Rogue','VIT.B First Blood Map 1','$20','$16.60']);
bets.push(['2019-09-12','Origen BCN vs Rogue','VIT.B First Blood Map 2','$11.20','$0']);
bets.push(['2019-09-12','Vitality Bee vs BIG','VIT.B First Blood Map 1','$20','$16.60']);
bets.push(['2019-09-12','Vitality Bee vs BIG','VIT.B First Blood Map 2','$20','$0']);
bets.push(['2019-09-13','Splyce vs Origen','SPY First Blood Map 1','$20','$0']); 
bets.push(['2019-09-13','Splyce vs Origen','SPY First Tower Map 1','$20','$0']); 
bets.push(['2019-09-13','Splyce vs Origen','SPY First Blood Map 2','$20','$0']); 
bets.push(['2019-09-13','Splyce vs Origen','SPY First Tower Map 2','$20','$13.80']);
bets.push(['2019-09-13','Splyce vs Origen','SPY First Blood Map 3','$20','$0']);    
bets.push(['2019-09-13','Splyce vs Origen','SPY First Tower Map 3','$20','$13.80']);
bets.push(['2019-09-14','Splyce vs Schalke 04','SPY First Blood Map 1','$20','$17.60']); 
bets.push(['2019-09-14','Splyce vs Schalke 04','SPY First Tower Map 1','$20','$0']);
bets.push(['2019-09-14','Schalke 04 vs Splyce','s04 First Dragon Map 1','$20','$0']);  
bets.push(['2019-09-14','Splyce vs Schalke 04','SPY First Blood Map 2','$20','$0']); 
bets.push(['2019-09-14','Splyce vs Schalke 04','SPY First Tower Map 2','$20','$17.20']); 
bets.push(['2019-09-14','Schalke 04 vs Splyce','s04 First Dragon Map 2','$20','$0']);
bets.push(['2019-09-14','Splyce vs Schalke 04','SPY First Blood Map 3','$20','$0']); 
bets.push(['2019-09-15','Fnatic vs Splyce','FNC First Blood Map 1','$30','$0']);
bets.push(['2019-09-15','Fnatic vs Splyce','FNC First Blood Map 2','$20','$15.40']);
bets.push(['2019-09-15','Fnatic vs Splyce','FNC First Blood Map 3','$20','$0']);
bets.push(['2019-10-12','Team Liquid vs ?','TL First Dragon Map 1','$40','$36.00']);
bets.push(['2019-10-13','Invictus Gaming vs DAMWON Gaming','IG First Tower Map 1','$20','$17.20']);
bets.push(['2019-10-13','Invictus Gaming vs DAMWON Gaming','IG First Dragon Map 1','$20','$17.20']);
bets.push(['2019-10-15','Royal Never Give Up vs Fnatic','RNG First Tower Map 1','$20','$17.20']);
bets.push(['2019-10-15','J Team vs Splyce','JT First Tower Map 1','$50','$0']);
bets.push(['2019-10-18','Griffin vs G2 Esports','GRF First Tower Map 1','$50','$17.60']);
bets.push(['2019-10-18','SKT vs Royal Never Give Up','SKT Win Map 1','$30','$18.00']);
bets.push(['2019-10-20','Team Liquid vs DAMWON Gaming','TL First Dragon Map 1','$30','$0']);
bets.push(['2019-10-20','Team Liquid vs Invictus Gaming','TL First Dragon Map 1','$20','$16.60']);
bets.push(['2019-10-26','Team Griffin vs Invictus Gaming','GRF First Tower Map 1','$20','$0']);
bets.push(['2019-10-26','Team Griffin vs Invictus Gaming','GRF First Tower Map 2','$20','$16.80']);
bets.push(['2019-10-26','Team Griffin vs Invictus Gaming','GRF First Tower Map 3','$20','$16.80']);
bets.push(['2019-10-26','FunPlus Phoenix vs Fnatic','FPX First Tower Map 1','$20','$16.80']);
bets.push(['2019-10-26','FunPlus Phoenix vs Fnatic','FPX First Tower Map 2','$20','$16.80']);
bets.push(['2019-10-27','G2 vs DAMWON Gaming','G2 First Tower Map 1','$20','$17.20']);
bets.push(['2019-10-27','DAMWON Gaming vs G2','DWG First Dragon Map 1','$20','$0']);
bets.push(['2019-10-27','G2 vs DAMWON Gaming','G2 First Tower Map 2','$20','$0']);
bets.push(['2019-10-27','DAMWON Gaming vs G2','DWG First Dragon Map 2','$20','$17.20']) ;
bets.push(['2019-10-27','G2 vs DAMWON Gaming','G2 First Tower Map 3','$20','$0']);
bets.push(['2019-10-27','DAMWON Gaming vs G2','DWG First Dragon Map 3','$20','$17.20']);
bets.push(['2019-11-02','FunPlus Phoenix vs Invictus Gaming','FPX First Dragon Map 1','$20','$16.80']);
bets.push(['2019-11-02','FunPlus Phoenix vs Invictus Gaming','FPX First Dragon Map 2','$20','$16.80']);
bets.push(['2019-11-02','FunPlus Phoenix vs Invictus Gaming','FPX First Dragon Map 3','$20','$16.80']);
bets.push(['2019-11-03','SKT vs G2 Esports','SKT First Tower Map 1','$20','$16.80']);
bets.push(['2019-11-03','SKT vs G2 Esports','SKT First Dragon Map 1','$19.60','$0']);
bets.push(['2019-11-03','SKT vs G2 Esports','SKT First Tower Map 2','$20','$16.80']);
bets.push(['2019-11-03','SKT vs G2 Esports','SKT First Tower Map 3','$20','$16.80']);
bets.push(['2019-11-10','FunPlus Phoenix vs G2 Esports','FPX First Tower Map 1','$20','$0']);
bets.push(['2019-11-10','FunPlus Phoenix vs G2 Esports','FPX First Dragon Map 1','$20','$0']);
bets.push(['2019-11-10','FunPlus Phoenix vs G2 Esports','FPX First Tower Map 2','$20','$0']);
bets.push(['2019-11-10','FunPlus Phoenix vs G2 Esports','FPX First Dragon Map 2','$20','$0']);
bets.push(['2019-11-10','FunPlus Phoenix vs G2 Esports','FPX First Tower Map 3','$20','$0']);
bets.push(['2019-11-10','FunPlus Phoenix vs G2 Esports','FPX First Dragon Map 3','$20','$0']);

function create_history() {
    var history_table = '<table id="bet_history_table">';
    history_table = '<thead><tr><th>Date</th><th>Match</th><th>Objective</th><th>Odds</th><th>Bet Amount</th><th>Outcome</th><th>Total</th></tr></thead><tbody>';
    history_table += '<tr><td colspan="7";>';
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
            history_table += '<td colspan="7";>';
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
        if (((+bets[i][3].split("$")[1] + +bets[i][4].split("$")[1])/bets[i][3].split("$")[1]).toFixed(2) == 1.00) {
            history_table += 'N/A';
        } else {
            history_table += ((+bets[i][3].split("$")[1] + +bets[i][4].split("$")[1])/bets[i][3].split("$")[1]).toFixed(2);    
        }    
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
            history_table += total_money = (+total_money + +bets[i][4].split("$")[1]).toFixed(2);
        } else {
            history_table += total_money = (+total_money - +bets[i][3].split("$")[1]).toFixed(2);
        }
        history_table += '</td>';

        history_table += '</tr>';
    }

    history_table+='</tbody></table>';
    $('#historyDiv').html(history_table);   
}

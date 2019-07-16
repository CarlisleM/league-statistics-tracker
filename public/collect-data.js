var pg = require('pg');
var connectionString = "databaselink";

var pgClient = new pg.Client({
    user: 'user',
    host: 'host',
    database: 'database',
    password: 'password',
    port: 5432,
    ssl: true
}); 

function getData(callback) {

    pgClient.connect();
    
    var query = pgClient.query("SELECT game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_data where id = game_id");

    query.on("row", function (row, result) {
        result.addRow(row);
    });

    query.on("end", function (result) {
     // callback(result.rows, null, "    ");
        callback(result.rows, null);
     // callback(JSON.stringify(result.rows, null));
     // console.log(JSON.stringify(result.rows, null, "    "));
    });

    pgClient.end();

}

exports.getData = getData;

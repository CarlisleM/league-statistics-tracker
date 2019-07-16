var pg = require('pg');
var connectionString = "postgres://djpoucmhkewvrh:e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c@ec2-174-129-209-212.compute-1.amazonaws.com:5432/d24ubplectbqas";

var pgClient = new pg.Client({
    user: 'djpoucmhkewvrh',
    host: 'ec2-174-129-209-212.compute-1.amazonaws.com',
    database: 'd24ubplectbqas',
    password: 'e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c',
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

    pgClient.end()

}

exports.getData = getData;

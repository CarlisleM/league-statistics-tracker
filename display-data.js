function getData() {

    var pg = require('pg');

    var connectionString = "postgres://djpoucmhkewvrh:e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c@ec2-174-129-209-212.compute-1.amazonaws.com:5432/d24ubplectbqas";

    console.log("trying to connect");

    var pgClient = new pg.Client(connectionString);

    pgClient.connect();

    console.log(connected);

    var query = pgClient.query("SELECT game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_data where id = game_id");

    query.on("row", function(row,result){
        result.addRow(row);
    });

    console.log(results);

}
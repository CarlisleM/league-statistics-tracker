const express = require('express')
const path = require('path')
const PORT = process.env.PORT || 5000

const { Client } = require('pg')
 
var db = require('./public/collect-data')
 
const app = express()
  app.use(express.static('public'))
  app.use(express.static(path.join(__dirname, 'public')))
  app.set('views', path.join(__dirname, 'views'))
  app.set('view engine', 'ejs') 
  app.get('/', (req, res) => res.render('pages/index'))

// app.get('/games', (req, res) => {
//   db.getData(function(result) {
//      // console.log(result);
//      res.json({ matches: result })
//   });
// })

app.get('/games', async (req, res) => {
  const client = new Client({
    user: 'djpoucmhkewvrh',
    host: 'ec2-174-129-209-212.compute-1.amazonaws.com',
    database: 'd24ubplectbqas',
    password: 'e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c',
    port: 5432,
    ssl: true
  })
  client.connect()

  const result = await client.query('SELECT game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_data where id = game_id')
  await client.end()
  res.json({ matches: result.rows })
})






app.listen(PORT, () => console.log(`Listening on ${ PORT }`))



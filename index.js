const express = require('express')
const path = require('path')
const PORT = process.env.PORT || 5000

const { Client } = require('pg')
  
const app = express()
  app.use(express.static('public'))
  app.use(express.static(path.join(__dirname, 'public')))
  app.set('views', path.join(__dirname, 'views'))
  app.set('view engine', 'ejs') 
  app.get('/', (req, res) => res.render('pages/index'))

// index page 
app.get('/', function(req, res) {
    res.render('pages/index');
});

// about page 
app.get('/about', function(req, res) {
    res.render('pages/about');
});

// faq page 
app.get('/faq', function(req, res) {
  res.render('pages/faq');
});

// bet history page 
app.get('/bets', function(req, res) {
    res.render('pages/bets');
});

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

  const result = await client.query('SELECT * FROM games, match_results where id = game_id')
  await client.end()
  res.json({ matches: result.rows })
})

app.get('/upcoming', async (req, res) => {
  const client = new Client({
    user: 'djpoucmhkewvrh',
    host: 'ec2-174-129-209-212.compute-1.amazonaws.com',
    database: 'd24ubplectbqas',
    password: 'e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c',
    port: 5432,
    ssl: true
  })
  client.connect()

  (TO_TIMESTAMP('04:00','HH24:MI:SS')::TIME < timezone('PDT', NOW())::TIME)

  const result = await client.query("SELECT * FROM upcoming WHERE (game_date = DATE(NOW()) AND (TO_TIMESTAMP(match_time,'HH24:MI:SS')::TIME > timezone('PDT', NOW())::TIME(0))) OR game_date > DATE(NOW());")
  await client.end()
  res.json({ upcoming_matches: result.rows })
})

app.listen(PORT, () => console.log(`Listening on ${ PORT }`))

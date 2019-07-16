const express = require('express')
const path = require('path')
const PORT = process.env.PORT || 5000
 
var db = require('./public/collect-data')
 
const app = express()
  app.use(express.static('public'))
  app.use(express.static(path.join(__dirname, 'public')))
  app.set('views', path.join(__dirname, 'views'))
  app.set('view engine', 'ejs') 
  app.get('/', (req, res) => res.render('pages/index'))

app.get('/games', (req, res) => {
  db.getData(function(result) {
     // console.log(result);
     res.json({ matches: result })
  });
})

app.listen(PORT, () => console.log(`Listening on ${ PORT }`))

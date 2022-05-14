var express = require('express');
const { json } = require('express/lib/response');
var router = express.Router();

const fs = require('fs');

let dbip;
fs.readFile('../ansible/vars/setup.yaml', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  dbip = data.match(/(\d+\.){3}\d+/g)[0];
});

const key = 'AIzaSyDqODW7h13yD9PzJ4wv2y8EJ_pdhy71vp0';

router.get('/', function (req, res, next) {
  res.render('index', {
    dbip: dbip,
    title: 'Yarra Tram Traffic Sentiment Analysis',
    key: key
  });
});

module.exports = router;

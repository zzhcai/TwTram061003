/*
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

*/

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

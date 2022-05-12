var express = require('express');
var router = express.Router();

const key = 'AIzaSyDqODW7h13yD9PzJ4wv2y8EJ_pdhy71vp0';

router.get('/', function (req, res, next) {
  res.redirect('/sa3');
});

router.get('/sa2', function (req, res, next) {
  res.render('index', { title: 'Statistical Area 2', geoJSON: '/jsons/sa2.json', key: key });
});

router.get('/sa3', function (req, res, next) {
  res.render('index', { title: 'Statistical Area 3', geoJSON: '/jsons/sa3.json', key: key });
});

router.get('/sa4', function (req, res, next) {
  res.render('index', { title: 'Statistical Area 4', geoJSON: '/jsons/sa4.json', key: key });
});

module.exports = router;

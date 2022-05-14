var express = require('express');
const { json } = require('express/lib/response');
var router = express.Router();

const key = 'AIzaSyDqODW7h13yD9PzJ4wv2y8EJ_pdhy71vp0';

router.get('/', function (req, res, next) {
  res.render('index', {
    title: 'temp title',
    key: key
  });
});

module.exports = router;

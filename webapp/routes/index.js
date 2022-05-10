var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', { title: 'Assignment', key: "AIzaSyDqODW7h13yD9PzJ4wv2y8EJ_pdhy71vp0" });
});

module.exports = router;

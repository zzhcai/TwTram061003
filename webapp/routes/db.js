/*
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

*/

var express = require('express');
const { json } = require('express/lib/response');
var router = express.Router();
const axios = require('axios');

router.get('/*', async function (req, res, next) {
	let url = req.originalUrl.substring(4);
	let headers = { 'Authorization': 'Basic ' + Buffer.from('admin:admin').toString('base64') };
	let json = await (axios.get(url, { headers: headers })
		.catch(error => {
			console.error(error);
		}));
	res.send(json.data);
});

module.exports = router;

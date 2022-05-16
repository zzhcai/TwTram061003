var express = require('express');
const { json } = require('express/lib/response');
var router = express.Router();
const axios = require('axios');

router.get('/*', async function (req, res, next) {
	let url = req.originalUrl.substring(4);
	let headers = { 'Authorization': 'Basic ' + Buffer.from('admin:admin').toString('base64') };
	let json = await axios.get(url, { headers: headers })
		.catch(error => {
			console.error(error);
		});
	res.send(json);
});

module.exports = router;

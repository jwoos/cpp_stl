'use strict';

const http = require('http');
const express = require('express');
const app = express();

// render
app.engine('html', require('ejs').renderFile);

app.get('/', function(req, res, next) {
	res.render('index.html');
});

app.get('/:date', function(req, res, next) {
	let date = req.params.date;
	
	let toSend = {
		unix: null,
		natural: null
	};
	
	let monthMap = {
		0: 'January',
		1: 'February',
		2: 'March',
		3: 'April',
		4: 'May',
		5: 'June',
		6: 'July',
		7: 'August',
		8: 'September',
		9: 'October',
		10: 'November',
		11: 'December'
	};
	
	if (isNaN(Number(date))) {
		
	} else {
		// make a module
		let dateObj = new Date(date * 1000);
		if (isNaN(dateObj.getFullYear()) || !monthMap[dateObj.getUTCMonth()] || !(date.length == 10)) {
			res.send(toSend);
		} else {
			toSend.unix = dateObj.getTime() / 1000;
			toSend.natural = monthMap[dateObj.getUTCMonth()] + ' ' + dateObj.getUTCDate() + ', ' + dateObj.getUTCFullYear();
			res.send(toSend);
		}
	}
});

// handle 404
app.use(function(req, res, next) {
	res.status(404).send('Sorry can\'t find that!');
});

// error handling
app.use(function(err, req, res, next) {
	if (req.xhr) {
		res.status(500).send({ error: 'Error' });
	} else {
		res.send('Error');
		res.send(err);
	}
});

app.listen(8080);
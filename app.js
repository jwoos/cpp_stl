const http = require('http');
const express = require('express');
const app = express();

// render
app.engine('html', require('ejs').renderFile);

app.get('/', function(req, res, next) {
	res.render('index.html');
});

app.get('/:date', function(req, res, next) {
	res.send(req.params.date);
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
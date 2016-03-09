const http = require('http');
const express = require('express');
const app = express();

// render
app.engine('html', require('ejs').renderFile);

app.get('/', function(req, res, next) {
	res.render('index.html');
});

app.get('/:date', function(req, res, next) {
	res.send('TEST');
});

app.listen(8080);
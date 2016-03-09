const http = require('http');
const express = require('express');
const app = express();

app.get('/', function(req, res, next) {
	res.send('Hello!');
});

app.listen(8080);
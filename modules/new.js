'use strict';

const pg = require('pg');
const http = require('http');

const pgString = 'postgres://psql:123456789@localhost/links';

module.exports = function(url) {
    let toReturn = {};
    
    let validPattern = /^(https|http)?(:\/\/)?(www\.)?\w+\.(\w+)(\.\w+)?(\/\w+)*/;
    if (!validPattern.test(url)) {
        toReturn.error = true;
        return toReturn;
    }
    
    http.get(url, function(res) {
        if (res.statusCode !== 200) {
            toReturn.original_url = url;
            toReturn.short_url = 'Invalid original url';
        } else {
            console.log(res);
        }
    }).on('error', function(e) {
        console.log(e);
        toReturn.error = e;
        return toReturn;
    });
    

    pg.connect(pgString, function(err, client, done) {
        if (err) {
            return console.log('Error fetching client from pool', err);
        }
        
        client.query("INSERT INTO links(url) values('" + url + "')", function(err, result) {
            if (err) {
                toReturn.error = err;
                return toReturn;
            }
            done();
        });
        
        client.query("SELECT * FROM links WHERE url='" + url + "'", function(err, result) {
            if (err) {
                toReturn.error = err;
                return toReturn;
            }
            console.log(result);
        });
    });

    return toReturn;
};
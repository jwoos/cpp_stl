const pg = require('pg');
const http = require('http');

const pgString = 'postgres://postgres:apassword@localhost/links';

module.exports = function(url) {
    let toReturn = {},
        valid = false;
    
    http.get(url, function(res) {
        if (res.statusCode !== 200) {
            toReturn.original_url = url;
            toReturn.short_url = 'Invalid original url';
        } else {
            console.log(res);
            valid = true;
        }
    }).on('error', function(e) {
        console.log(e);
    });
    
    if (valid) {
        pg.connect(pgString, function(err, client, done) {
            if (err) {
                return console.err('Error fetching client from pool', err);
            }
            
            client.query('INSERT INTO links(url) values(' + url + ')', function(err, result) {
                console.err(err);
                done();
            });
        });
    }
    
    return toReturn;
};
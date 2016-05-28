'use strict';

const pg = require('pg');
const pgString = 'postgres://ubuntu:123456789@localhost/links';

pg.connect(pgString, function(err, client, done) {
    if (err) {
        return console.log(err);
    }
    
    let query = client.query(`
        CREATE TABLE links(
            id SERIAL PRIMARY KEY NOT NULL,
            url TEXT NOT NULL
        )
    `);
    
    query.on('error', function(err) {
        console.log(err);
    });
    
    query.on('end', function() {
        done();
    });
});
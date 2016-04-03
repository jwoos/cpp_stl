'use strict';

const pg = require('pg');

const pgString = 'postgres://psql:123456789@localhost/links';

module.exports = function(number) {
    pg.connect(pgString, function(err, client, done) {
        client.query("SELECT * FROM links WHERE id='" + number + "'", function(err, results) {
            if (err) {
                return err;
            } else {
                return results;
            }
        }) ;
    });
};
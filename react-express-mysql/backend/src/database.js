/**
 * @fileoverview This file sets up the database connection using knex.
 */
const knex = require('knex');
const { database } = require('./config');

module.exports = knex({
  client: 'mysql2',
  connection: database,
});

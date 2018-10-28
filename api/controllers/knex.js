const knex = require('knex');

const db = knex({
  client: 'mysql',
  connection: {
    host : "127.0.0.1",
    user : "root",
    password : "Thinkonce",
    database : "freejobalert"
  }
});



module.exports = {
  db
}

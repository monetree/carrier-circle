const express = require('express');
const bodyParser = require('body-parser');
const knex = require('knex');
const app = express();
const cors = require('cors');
app.use(bodyParser.json());
app.use(cors());

const db = knex({
  client: 'mysql',
  connection: {
    host : "127.0.0.1",
    user : "root",
    password : "Thinkonce",
    database : "freejobalert"
  }
});

app.get('/',(req,res) => {
  res.send("Api Root");
})

app.get('/odisha_govt_jobs/', (req, res) => {
    let columns = [
    'scrap_odishagovtjobs.last_date',
    'scrap_odishagovtjobs.start_date',
    'scrap_odishagovtjobs.post_name',
    'scrap_odishagovtjobs.education',
    'scrap_odishagovtjobs.requirement_board',
    'scrap_odishagovtjobs.type',
    'scrap_odishagovtjobs.join_id',
    'details_odishagovtjobdetails.more_info'
  ];
  // db.ref('scrap_odishagovtjobs.last_date').as('last_date')

  db.select(
    (db.raw('group_concat(details_odishagovtjobdetails.more_info) as details')),columns)
    .from('scrap_odishagovtjobs').
     innerJoin('details_odishagovtjobdetails', 'scrap_odishagovtjobs.join_id', 'details_odishagovtjobdetails.join_id')
    .where('scrap_odishagovtjobs.type', 2).groupBy('scrap_odishagovtjobs.post_name')
    // db.raw("select group_concat(details_odishagovtjobdetails.more_info) as more_info,\
    //         scrap_odishagovtjobs.start_date,scrap_odishagovtjobs.last_date,scrap_odishagovtjobs.post_name,\
    //         scrap_odishagovtjobs.education,scrap_odishagovtjobs.requirement_board,scrap_odishagovtjobs.type \
    //         from scrap_odishagovtjobs inner join details_odishagovtjobdetails\
    //         on scrap_odishagovtjobs.join_id=details_odishagovtjobdetails.join_id\
    //          where scrap_odishagovtjobs.type=2 group by scrap_odishagovtjobs.post_name\
    //         ")
    .then(api => {
        res.json(api)
    })
    .catch(err => res.status(400).json('error getting api'))
})

app.listen(3000, ()=> {
  console.log('App is running on port 3000');
})

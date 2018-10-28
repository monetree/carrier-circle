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

let job_type1 = {}
let job_type2 = {}
let job_type3 = {}
let job_api = {}

app.get('/',(req,res) => {
  res.send("Api Root");
})

app.get('/api/statewise-govt-jobs/odisha-govt-jobs/', (req, res) => {
    let job_type2 = [
      db.raw('group_concat(details_odishagovtjobdetails.more_info) as more_info'),
      db.ref('scrap_odishagovtjobs.start_date').as('start_date'),
      db.ref('scrap_odishagovtjobs.last_date').as('last_date'),
      db.ref('scrap_odishagovtjobs.post_name').as('post_name'),
      db.ref('scrap_odishagovtjobs.education').as('education'),
      db.ref('scrap_odishagovtjobs.requirement_board').as('requirement_board'),
      db.ref('scrap_odishagovtjobs.type').as('type'),
      db.ref('scrap_odishagovtjobs.more_info').as('details')
  ];
    let job_type1 = [
      db.ref('scrap_odishagovtjobs.start_date').as('start_date'),
      db.ref('scrap_odishagovtjobs.last_date').as('last_date'),
      db.ref('scrap_odishagovtjobs.post_name').as('post_name'),
      db.ref('scrap_odishagovtjobs.education').as('education'),
      db.ref('scrap_odishagovtjobs.requirement_board').as('requirement_board'),
      db.ref('scrap_odishagovtjobs.type').as('jobs_type'),
      db.ref('scrap_odishagovtjobs.more_info').as('more_info')
    ];

  db.select(job_type2)
    .from('scrap_odishagovtjobs').
     innerJoin('details_odishagovtjobdetails',
               'scrap_odishagovtjobs.join_id',
               'details_odishagovtjobdetails.join_id')
    .where('scrap_odishagovtjobs.type', 2)
    .groupBy('scrap_odishagovtjobs.post_name')
    .then(api => {
        job_type2 = api
        // console.log(job_type2)
    }).then(
      db.select(job_type1)
      .from('scrap_odishagovtjobs')
      .where('scrap_odishagovtjobs.type', 1)
      .then(api => {
          job_type1 = api
          // console.log(job_type1)
        }).then(
            db.select(job_type3)
            .from('scrap_odishagovtjobs')
            .where('scrap_odishagovtjobs.type', 3)
        ).then(api => {
          job_type3 = api
          // console.log(job_type3)
        })
        .then(api => {
          (job_type3 != undefined  && job_type3.length) ?
            job_api = job_type1.concat(job_type2,job_type3) :
          (job_type2 != undefined  && job_type2.length) ?
            job_api =  job_type1.concat(job_type2) :
           job_api = job_type1;
        }).then(api => {
          job_api.map((ja, i) => {
            if (ja["type"] == 2){
              eval('ja["more_info"]='+ja["more_info"]);
              }
            })
          res.json(job_api)
        })
    )
    .catch(err => res.status(400).json('error getting api'))
})

app.listen(3000, ()=> {
  console.log('App is running on port 3000');
})

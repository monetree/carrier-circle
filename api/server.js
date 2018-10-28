const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const cors = require('cors');
app.use(bodyParser.json());
app.use(cors());

// controllers
const knex = require('./controllers/knex');
const common = require('./controllers/common');
const access = require('./controllers/access');


app.get('/',(req,res) => {
  res.send("Api Root");
})


app.get('/api/all_india-govt-jobs/other-all-india-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  let job_type1 = [
    knex.db.ref('scrap_otherallindiajobs.start_date').as('start_date'),
    knex.db.ref('scrap_otherallindiajobs.last_date').as('last_date'),
    knex.db.ref('scrap_otherallindiajobs.post_name').as('post_name'),
    knex.db.ref('scrap_otherallindiajobs.education').as('education'),
    knex.db.ref('scrap_otherallindiajobs.requirement_board').as('requirement_board'),
    knex.db.ref('scrap_otherallindiajobs.type').as('type'),
    knex.db.ref('scrap_otherallindiajobs.more_info').as('more_info')
  ];
  let job_type2 = [
    knex.db.raw('group_concat(details_otherallindiajobdetails.more_info) as more_info'),
    knex.db.ref('scrap_otherallindiajobs.start_date').as('start_date'),
    knex.db.ref('scrap_otherallindiajobs.last_date').as('last_date'),
    knex.db.ref('scrap_otherallindiajobs.post_name').as('post_name'),
    knex.db.ref('scrap_otherallindiajobs.education').as('education'),
    knex.db.ref('scrap_otherallindiajobs.requirement_board').as('requirement_board'),
    knex.db.ref('scrap_otherallindiajobs.type').as('type'),
    knex.db.ref('scrap_otherallindiajobs.more_info').as('details')
];
  let job_type3 = [
    knex.db.ref('scrap_otherallindiajobs.start_date').as('start_date'),
    knex.db.ref('scrap_otherallindiajobs.last_date').as('last_date'),
    knex.db.ref('scrap_otherallindiajobs.post_name').as('post_name'),
    knex.db.ref('scrap_otherallindiajobs.education').as('education'),
    knex.db.ref('scrap_otherallindiajobs.requirement_board').as('requirement_board'),
    knex.db.ref('scrap_otherallindiajobs.type').as('type'),
    knex.db.ref('scrap_otherallindiajobs.more_info').as('more_info')
  ];
  let tables = ["scrap_otherallindiajobs","details_otherallindiajobdetails"]
  let joins  = ["scrap_otherallindiajobs.join_id","details_otherallindiajobdetails.join_id"]
  let where  = {"where1":'scrap_otherallindiajobs.type',"where1_index":1,
               "where2":'scrap_otherallindiajobs.type',"where2_index":2,
               "where3":'scrap_otherallindiajobs.type',"where3_index":3}
  let group  = 'scrap_otherallindiajobs.post_name'
  common.Algo(req, res, knex, job_type1, job_type2, job_type3, tables, joins, where, group);
})

app.get('/api/statewise-govt-jobs/odisha-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  let job_type1 = [
    knex.db.ref('scrap_odishagovtjobs.start_date').as('start_date'),
    knex.db.ref('scrap_odishagovtjobs.last_date').as('last_date'),
    knex.db.ref('scrap_odishagovtjobs.post_name').as('post_name'),
    knex.db.ref('scrap_odishagovtjobs.education').as('education'),
    knex.db.ref('scrap_odishagovtjobs.requirement_board').as('requirement_board'),
    knex.db.ref('scrap_odishagovtjobs.type').as('jobs_type'),
    knex.db.ref('scrap_odishagovtjobs.more_info').as('more_info')
  ];
  let job_type2 = [
    knex.db.raw('group_concat(details_odishagovtjobdetails.more_info) as more_info'),
    knex.db.ref('scrap_odishagovtjobs.start_date').as('start_date'),
    knex.db.ref('scrap_odishagovtjobs.last_date').as('last_date'),
    knex.db.ref('scrap_odishagovtjobs.post_name').as('post_name'),
    knex.db.ref('scrap_odishagovtjobs.education').as('education'),
    knex.db.ref('scrap_odishagovtjobs.requirement_board').as('requirement_board'),
    knex.db.ref('scrap_odishagovtjobs.type').as('type'),
    knex.db.ref('scrap_odishagovtjobs.more_info').as('details')
];
  let tables = ["scrap_odishagovtjobs","details_odishagovtjobdetails"]
  let joins  = ["scrap_odishagovtjobs.join_id","details_odishagovtjobdetails.join_id"]
  let where  = {"where1":'scrap_odishagovtjobs.type',"where1_index":1,
               "where2":'scrap_odishagovtjobs.type',"where2_index":2,
               "where3":'scrap_odishagovtjobs.type',"where3_index":3}
  let group  = 'scrap_odishagovtjobs.post_name'
  common.Algo(req, res, knex, job_type1, job_type2, tables, joins, where, group);
})

app.listen(3000, ()=> {
  console.log('App is running on port 3000');
})

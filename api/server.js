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
  table1 = "scrap_otherallindiajobs"
  table2 = "details_otherallindiajobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/odisha-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_odishagovtjobs"
  table2 = "details_odishagovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.listen(3000, ()=> {
  console.log('App is running on port 3000');
})

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

app.get('/api/statewise-govt-jobs/andaman-nicobar-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_andamannicoborgovtjobs"
  table2 = "details_andamannicoborgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/andhra-pradesh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_andhrapradeshgovtjobs"
  table2 = "details_andhrapradeshgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/arunachal-pradesh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_arunachalpradeshgovernmentjobs"
  table2 = "details_arunachalpradeshgovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/assam-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_assamgovtjobs"
  table2 = "details_assamgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/bihar-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_bihargovtjobs"
  table2 = "details_bihargovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/chandigarh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chandigarhgovtjobs"
  table2 = "details_chandigarhgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/chhattishgarh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chhattisgarhgovtjobs"
  table2 = "details_chhattisgarhgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})


app.listen(3000, ()=> {
  console.log('App is running on port 3000');
})

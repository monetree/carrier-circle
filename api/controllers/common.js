
const express = require('express');
const app = express()
const fetch = require('node-fetch');
let path = require('path');

let python_url = "http://localhost:8000/"
let job_type1 = {}
let job_type2 = {}
let job_type3 = {}
let job_api = {}


const Algo = (req, res, knex, jobType1, jobType2, jobType3, tables, joins, where, groupBy) => {
  let table1 = tables[0]
  let table2 = tables[1]
  let join1 = joins[0]
  let join2 = joins[1]
  let group = groupBy
  knex.db.select(jobType1)
  .from(table1)
  .where(where["where1"], where["where1_index"])
    .then(api => {
        job_type1 = api
    }).then(
      knex.db.select(jobType2)
        .from(table2).
         innerJoin(table1,join1,join2)
        .where(where["where2"], where["where2_index"])
         // .groupBy(group)
      .then(api => {
          job_type2 = api
        }).then(
          knex.db.select(jobType3)
          .from(table1)
          .where(where["where3"], where["where3_index"])
        .then(api => {
          job_type3 = api
        })
        .then(api => {
          if (job_type3 != undefined  && job_type3.length) {
             job_api = job_type1.concat(job_type2,job_type3)
           }else if (job_type2 != undefined  && job_type2.length) {
             job_api =  job_type1.concat(job_type2)
           }else{
             job_api = job_type1;
           }
        }).then(api => {
          job_api.map((ja, i) => {
              if (ja["type"] === 3){
                ja["more_info"] = python_url + ja["more_info"];
              }
              if (ja["type"] === 2){
                str = ja["more_info"]
                replace_quote = str.replace(/'/gi,'"')
                ja["more_info"] = JSON.parse(replace_quote)
                more_info = ja["more_info"]
                more_info.map((mi, i) => {
                  if (mi["Link"].startsWith('media') && mi["Link"].endsWith('pdf')) {
                    mi["Link"] = python_url + mi["Link"]
                  }
                })
              }
            })
            res.json(job_api)
        })
    )
  )
    .catch(err => res.status(400).json('error getting api'))
}

const data = (req,res,knex,table1,table2) => {
  let job_type1 = [
    knex.db.ref(table1 + '.start_date').as('start_date'),
    knex.db.ref(table1 + '.last_date').as('last_date'),
    knex.db.ref(table1 + '.post_name').as('post_name'),
    knex.db.ref(table1 + '.education').as('education'),
    knex.db.ref(table1 + '.requirement_board').as('requirement_board'),
    knex.db.ref(table1 + '.type').as('type'),
    knex.db.ref(table1 + '.more_info').as('more_info')
  ];
  let job_type2 = [
    knex.db.ref(table2 + '.more_info').as('more_info'),
    knex.db.ref(table1 + '.start_date').as('start_date'),
    knex.db.ref(table1 + '.last_date').as('last_date'),
    knex.db.ref(table1 + '.post_name').as('post_name'),
    knex.db.ref(table1 + '.education').as('education'),
    knex.db.ref(table1 + '.requirement_board').as('requirement_board'),
    knex.db.ref(table1 + '.type').as('type'),
];
  let job_type3 = [
    knex.db.ref(table1 + '.start_date').as('start_date'),
    knex.db.ref(table1 + '.last_date').as('last_date'),
    knex.db.ref(table1 + '.post_name').as('post_name'),
    knex.db.ref(table1 + '.education').as('education'),
    knex.db.ref(table1 + '.requirement_board').as('requirement_board'),
    knex.db.ref(table1 + '.type').as('type'),
    knex.db.ref(table1 + '.more_info').as('more_info')
  ];
  let tables = [table1,table2]
  let joins  = [table1 + ".join_id",table2 + ".join_id"]
  let where  = {"where1":table1 + '.type',"where1_index":1,
               "where2":table1 + '.type',"where2_index":2,
               "where3":table1 + '.type',"where3_index":3}
  let group  = table1 + '.post_name'
    Algo(req, res, knex, job_type1, job_type2, job_type3, tables, joins, where, group);
}

module.exports = {
  data
}

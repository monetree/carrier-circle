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
        .from(table1).
         innerJoin(table2,join1,join2)
        .where(where["where2"], where["where2_index"])
        .groupBy(group)
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
          (job_type3 != undefined  && job_type3.length) ?
            job_api = job_type1.concat(job_type2,job_type3) :
          (job_type2 != undefined  && job_type2.length) ?
            job_api =  job_type1.concat(job_type2) :
           job_api = job_type1;
        }).then(api => {
          job_api.map((ja, i) => {
              ja["type"] == 2 ?
                eval('ja["more_info"]='+ja["more_info"]):
              ja["type"] == 3 ?
                ja["more_info"]= python_url + ja["more_info"]:
              ja["more_info"] = ja["more_info"]
            })
          res.json(job_api)
        })
    )
  )
    .catch(err => res.status(400).json('error getting api'))
}


module.exports = {
  Algo
}

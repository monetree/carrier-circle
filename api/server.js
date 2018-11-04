const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const cors = require('cors');
app.use(bodyParser.json());
app.use(cors());
app.set('view engine','pug')

// controllers
const knex = require('./controllers/knex');
const common = require('./controllers/common');
const access = require('./controllers/access');


app.get('/',(req,res) => {
  let context = {title:"api",message:"root"}
  res.render("index", context);
})

// all india govt jobs api

app.get('/api/all_india-govt-jobs/other-all-india-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_otherallindiajobs"
  table2 = "details_otherallindiajobdetails"
  common.data(req,res,knex,table1,table2)
})

// statewise govt jobs api

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

app.get('/api/statewise-govt-jobs/dadra-nagar-haweli-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_dadranagarhaveligovtjobs"
  table2 = "details_dadranagarhaveligovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/chhattishgarh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chhattisgarhgovtjobs"
  table2 = "details_chhattisgarhgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/daman-diu-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_damandiugovtjobs"
  table2 = "details_damandiugovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/delhi-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_delhigovtjobs"
  table2 = "details_goagovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/goa-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_goagovernmentjobs"
  table2 = "details_goajobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/gujurat-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_gujuratgovtjobs"
  table2 = "details_gujuratgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/haryana-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_haryanagovtjobs"
  table2 = "details_haryanagovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/himachal-pradesh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_himachalpradeshgovtjobs"
  table2 = "details_himachalpradeshgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/jammu-kashmir-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_jammukashmirgovtjobs"
  table2 = "details_chhattisgarhgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/jharkhand-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_jharkhandgovtjobs"
  table2 = "details_jharkhandgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/karnataka-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_karnatakagovtjobs"
  table2 = "details_karnatakagovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/kerala-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_keralagovtjobs"
  table2 = "details_keralagovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/lakshadweep-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_lakshadweepgovernmentjobs"
  table2 = "details_lakshadweepgovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/madhya-pradesh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_madhyapradeshgovtjobs"
  table2 = "details_madhyapradeshgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/maharashtra-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_maharashtragovtjobs"
  table2 = "details_maharashtragovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/manipur-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_manipurgovtjobs"
  table2 = "details_manipurgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/meghalaya-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_meghalayagovtjobs"
  table2 = "details_meghalayagovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/mizoram-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_mizoramgovtjobs"
  table2 = "details_mizoramgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/nagaland-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_nagalandgovtjobs"
  table2 = "details_nagalandgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/puduchhery-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_puduchherygovtjobs"
  table2 = "details_puduchherygovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/punjab-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_punjabgovtjobs"
  table2 = "details_punjabgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/rajastan-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_rajasthangovtjobs"
  table2 = "details_rajasthangovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/sikkim-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_sikkimgovtjobs"
  table2 = "details_sikkimgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/tamilnadu-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_tamilgovtjobs"
  table2 = "details_tamilgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/telengana-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_telanganagovtjobs"
  table2 = "details_telanganagovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/tripura-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_tripuragovtjobs"
  table2 = "details_tripuragovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/uttarakhand-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_uttarakhandgovtjobs"
  table2 = "details_uttarakhandgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/uttar-pradesh-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_uttarpradeshgovtjobs"
  table2 = "details_uttarpradeshgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-govt-jobs/west-bengal-govt-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_westbengalgovtjobs"
  table2 = "details_westbengalgovtjobdetails"
  common.data(req,res,knex,table1,table2)
})

// teaching jobs api

app.get('/api/statewise-teaching-jobs/all-india-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_allindiateachingjobs"
  table2 = "details_allindiateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/odisha-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_odishateachingjobs"
  table2 = "details_odishateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/andaman-nicobar-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_andamannicoborteachingjobs"
  table2 = "details_andamannicoborteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/andhra-pradesh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_andhrapradeshteachingjobs"
  table2 = "details_andhrapradeshteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/arunachal-pradesh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_arunachalpradeshteachingjobs"
  table2 = "details_arunachalpradeshteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/assam-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_assamteachingjobs"
  table2 = "details_assamteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/bihar-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_biharteachingjobs"
  table2 = "details_biharteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/chandigarh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chandigarhteachingjobs"
  table2 = "details_chandigarhteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/chhattishgarh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chhattisgarhteachingjobs"
  table2 = "details_chhattisgarhteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/dadra-nagar-haweli-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_dadranagarhaveliteachingjobs"
  table2 = "details_dadranagarhaveliteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})


app.get('/api/statewise-teaching-jobs/daman-diu-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_damandiuteachingjobs"
  table2 = "details_damandiuteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/delhi-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_delhiteachingjobs"
  table2 = "details_goagovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/goa-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_goagovernmentjobs"
  table2 = "details_goajobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/gujurat-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_gujuratteachingjobs"
  table2 = "details_gujuratteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/haryana-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_haryanateachingjobs"
  table2 = "details_haryanateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/himachal-pradesh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_himachalpradeshteachingjobs"
  table2 = "details_himachalpradeshteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/jammu-kashmir-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_jammukashmirteachingjobs"
  table2 = "details_chhattisgarhteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/jharkhand-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_jharkhandteachingjobs"
  table2 = "details_jharkhandteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/karnataka-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_karnatakateachingjobs"
  table2 = "details_karnatakateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/kerala-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_keralateachingjobs"
  table2 = "details_keralateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/lakshadweep-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_lakshadweepgovernmentjobs"
  table2 = "details_lakshadweepgovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/madhya-pradesh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_madhyapradeshteachingjobs"
  table2 = "details_madhyapradeshteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/maharashtra-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_maharashtrateachingjobs"
  table2 = "details_maharashtrateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/manipur-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_manipurteachingjobs"
  table2 = "details_manipurteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/meghalaya-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_meghalayateachingjobs"
  table2 = "details_meghalayateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/mizoram-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_mizoramteachingjobs"
  table2 = "details_mizoramteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/nagaland-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_nagalandteachingjobs"
  table2 = "details_nagalandteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/puduchhery-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_puduchheryteachingjobs"
  table2 = "details_puduchheryteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/punjab-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_punjabteachingjobs"
  table2 = "details_punjabteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/rajastan-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_rajasthanteachingjobs"
  table2 = "details_rajasthanteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/sikkim-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_sikkimteachingjobs"
  table2 = "details_sikkimteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/tamilnadu-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_tamilnaduteachingjobs"
  table2 = "details_tamilnaduteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/telengana-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_telanganateachingjobs"
  table2 = "details_telanganateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/tripura-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_tripurateachingjobs"
  table2 = "details_tripurateachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/uttarakhand-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_uttarakhandteachingjobs"
  table2 = "details_uttarakhandteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/uttar-pradesh-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_uttarpradeshteachingjobs"
  table2 = "details_uttarpradeshteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-teaching-jobs/west-bengal-teaching-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_westbengalteachingjobs"
  table2 = "details_westbengalteachingjobdetails"
  common.data(req,res,knex,table1,table2)
})

// engineering jobs api

app.get('/api/statewise-engg-jobs/all-india-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_allindiaenggjobs"
  table2 = "details_allindiaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/all-india-fellow-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_allindiafellowenggjobs"
  table2 = "details_allindiafellowenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/odisha-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_odishaenggjobs"
  table2 = "details_odishaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/andaman-nicobar-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_andamannicoborenggjobs"
  table2 = "details_andamannicoborenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/andhra-pradesh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_andhrapradeshenggjobs"
  table2 = "details_andhrapradeshenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/arunachal-pradesh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_arunachalpradeshenggjobs"
  table2 = "details_arunachalpradeshenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/assam-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_assamenggjobs"
  table2 = "details_assamenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/bihar-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_biharenggjobs"
  table2 = "details_biharenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/chandigarh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chandigarhenggjobs"
  table2 = "details_chandigarhenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/chhattishgarh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chhattisgarhenggjobs"
  table2 = "details_chhattisgarhenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/dadra-nagar-haweli-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_dadranagarhavelienggjobs"
  table2 = "details_dadranagarhavelienggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/chhattishgarh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_chhattisgarhenggjobs"
  table2 = "details_chhattisgarhenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/daman-diu-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_damandiuenggjobs"
  table2 = "details_damandiuenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/delhi-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_delhienggjobs"
  table2 = "details_goagovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/goa-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_goagovernmentjobs"
  table2 = "details_goajobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/gujurat-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_gujuratenggjobs"
  table2 = "details_gujuratenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/haryana-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_haryanaenggjobs"
  table2 = "details_haryanaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/himachal-pradesh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_himachalpradeshenggjobs"
  table2 = "details_himachalpradeshenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/jammu-kashmir-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_jammukashmirenggjobs"
  table2 = "details_chhattisgarhenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/jharkhand-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_jharkhandenggjobs"
  table2 = "details_jharkhandenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/karnataka-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_karnatakaenggjobs"
  table2 = "details_karnatakaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/kerala-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_keralaenggjobs"
  table2 = "details_keralaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/lakshadweep-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_lakshadweepgovernmentjobs"
  table2 = "details_lakshadweepgovernmentjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/madhya-pradesh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_madhyapradeshenggjobs"
  table2 = "details_madhyapradeshenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/maharashtra-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_maharashtraenggjobs"
  table2 = "details_maharashtraenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/manipur-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_manipurenggjobs"
  table2 = "details_manipurenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/meghalaya-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_meghalayaenggjobs"
  table2 = "details_meghalayaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/mizoram-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_mizoramenggjobs"
  table2 = "details_mizoramenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/nagaland-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_nagalandenggjobs"
  table2 = "details_nagalandenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/puduchhery-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_puduchheryenggjobs"
  table2 = "details_puduchheryenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/punjab-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_punjabenggjobs"
  table2 = "details_punjabenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/rajastan-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_rajasthanenggjobs"
  table2 = "details_rajasthanenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/sikkim-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_sikkimenggjobs"
  table2 = "details_sikkimenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/tamilnadu-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_tamilnaduenggjobs"
  table2 = "details_tamilnaduenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/telengana-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_telanganaenggjobs"
  table2 = "details_telanganaenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/tripura-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_tripuraenggjobs"
  table2 = "details_tripuraenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/uttarakhand-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_uttarakhandenggjobs"
  table2 = "details_uttarakhandenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/uttar-pradesh-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_uttarpradeshenggjobs"
  table2 = "details_uttarpradeshenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/statewise-engg-jobs/west-bengal-engg-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_westbengalenggjobs"
  table2 = "details_westbengalenggjobdetails"
  common.data(req,res,knex,table1,table2)
})

// bank jobs api

app.get('/api/bank-jobs/all-bank-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_allbankjobs"
  table2 = "details_allbankjobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/bank-jobs/other-financial-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_otherfinancialjobs"
  table2 = "details_otherfinancialjobdetails"
  common.data(req,res,knex,table1,table2)
})

// Railway jobs api

app.get('/api/railway-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_railwayjobsmodel"
  table2 = "details_railwayjobdetails"
  common.data(req,res,knex,table1,table2)
})

// Polica jobs api

app.get('/api/police-jobs/all-india-police-defence-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_policeanddefencejobs"
  table2 = "details_policeanddefencejobdetails"
  common.data(req,res,knex,table1,table2)
})

app.get('/api/police-jobs/statewise-police-defence-jobs/', (req, res) => {
  access.Validate(req, res)
  table1 = "scrap_statewisepolicejobs"
  table2 = "details_statewisepolicejobdetails"
  common.data(req,res,knex,table1,table2)
})

app.listen(3000, ()=> {
  console.log('App is running on port 3000');
})

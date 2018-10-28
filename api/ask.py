here is my knex raw sql query.


    knex.raw("select group_concat(details_odishagovtjobdetails.more_info) as more_info,\
            scrap_odishagovtjobs.start_date,scrap_odishagovtjobs.last_date,scrap_odishagovtjobs.post_name,\
            scrap_odishagovtjobs.education,scrap_odishagovtjobs.requirement_board,scrap_odishagovtjobs.type \
            from scrap_odishagovtjobs inner join details_odishagovtjobdetails\
            on scrap_odishagovtjobs.join_id=details_odishagovtjobdetails.join_id\
             where scrap_odishagovtjobs.type=2 group by scrap_odishagovtjobs.post_name\
        ")


knex way:

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

    db.select((db.raw('group_concat(details_odishagovtjobdetails.more_info) as details')),columns).from('scrap_odishagovtjobs').
    innerJoin('details_odishagovtjobdetails', 'scrap_odishagovtjobs.join_id', 'details_odishagovtjobdetails.join_id')
    .where('scrap_odishagovtjobs.type', 2).groupBy('scrap_odishagovtjobs.post_name')


response:

    {
        "0": "24-11-2018",
        "1": "12/10/2018",
        "2": "Assistant Professor  – 107 Posts",
        "3": "M.Ch, MD/ MS, M.Sc, DM",
        "4": "OPSC",
        "5": 2,
        "6": 193457,
        "7": "{'Link': 'http://opsconline.gov.in/', 'Title': ' Apply Online'}",
        "details": "{'Link': 'http://opsconline.gov.in/', 'Title': ' Apply Online'},{'Link': 'http://www.opsc.gov.in/Admin/ContAttach/101819.pdf', 'Title': 'Notification '},{'Link': 'http://www.opsc.gov.in/', 'Title': ' Official Website'}"
    }

here i am writing above query in knex way with express.js but i am getting serial no for each columns instead of
actual column names.

Please have a look into my code.

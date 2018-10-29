json string:


    str = "{'Link': 'https://careers.powergrid.in/CCBaclogVacancy2018/c/default.aspx',
    'Title': 'Apply Online'},{'Link': 'https://careers.powergrid.in/CCBaclogVacancy2018/c/login.aspx',
    'Title': 'Login'},{'Link': 'media/pdf/details/all-india-govt-jobs/other-all-india-govt-jobs/8588011698.pdf',
    'Title': 'Notification '},{'Link': 'http://www.powergridindia.com/', 'Title': 'Official Website'}"


expecting:

    json = {'Link': 'https://careers.powergrid.in/CCBaclogVacancy2018/c/default.aspx',
    'Title': 'Apply Online'},{'Link': 'https://careers.powergrid.in/CCBaclogVacancy2018/c/login.aspx',
    'Title': 'Login'},{'Link': 'media/pdf/details/all-india-govt-jobs/other-all-india-govt-jobs/8588011698.pdf',
    'Title': 'Notification '},{'Link': 'http://www.powergridindia.com/', 'Title': 'Official Website'}


i am trying with JSON.parse(str);
it gives me error:

    VM267:1 Uncaught SyntaxError: Unexpected token ' in JSON at position 1
    at JSON.parse (<anonymous>)
    at <anonymous>:1:6

How can i convert string to pure json.

please have a look into this..

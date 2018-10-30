+++++++++++++++++++++++++++++++++++++++++++ before multiprocessing :++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| {'Title': 'Other Details', 'Link': 'https://apdsc.apcfss.in/'}                                                                                           |
| {'Title': 'News Paper Link', 'Link': 'http://img.fabual.com/blcont/uploads/Latest-Updates-Andhra-Pradesh-Today-7729-teacher-DSC-posts-are-replaced.pdf'} |
| {'Title': 'Official Site', 'Link': 'https://schooledu.ap.gov.in/DSENEW/'}                                                                                |
| {'Title': ' Official Website', 'Link': 'http://apvvp.nic.in/'}                                                                                           |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/80491429.pdf', 'Title': 'Information Bulletin (School Education)'}                  |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/26426598.pdf', 'Title': 'Information Bulletin (Residential Schools)'}               |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/12320694.pdf', 'Title': 'Notification (School Education)'}                          |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/69342324.pdf', 'Title': 'Notification (Residential Schools)'}                       |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/96849037.pdf', 'Title': 'Exam Schedule'}                                            |                                                                                        |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/75530213.pdf', 'Title': 'Abstract'}                                                 |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/35858358.pdf', 'Title': 'Notification '}                                            |
| {'Title': 'Syllabus', 'Link': 'crash'}                                                                                                                   |
| {'Title': 'Eligibility', 'Link': 'crash'}                                                                                                                |
| {'Title': 'Selection Procedure Details', 'Link': 'crash'}                                                                                                |
++++++++++++++++++++++++++++++++++++++++++time 8 min with 3 exceptions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

+++++++++++++++++++++++++++++++++++++++++++ after multiprocessing :+++++++++++++++++++++++++++++++++++++++++++++
| {'Link': 'https://apdsc.apcfss.in/', 'Title': 'Other Details'}                                                                                           |
| {'Link': 'http://img.fabual.com/blcont/uploads/Latest-Updates-Andhra-Pradesh-Today-7729-teacher-DSC-posts-are-replaced.pdf', 'Title': 'News Paper Link'} |
| {'Link': 'https://schooledu.ap.gov.in/DSENEW/', 'Title': 'Official Site'}                                                                                |
| {'Link': 'http://apvvp.nic.in/', 'Title': ' Official Website'}                                                                                           |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/512714815.pdf', 'Title': 'Information Bulletin (School Education)'}                 |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/3682918364.pdf', 'Title': 'Information Bulletin (Residential Schools)'}             |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/9416707350.pdf', 'Title': 'Notification (School Education)'}                        |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/6525134333.pdf', 'Title': 'Notification (Residential Schools)'}                     |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/3883206811.pdf', 'Title': 'Exam Schedule'}                                          |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/4017534319.pdf', 'Title': 'Abstract'}                                               |
| {'Link': 'media/pdf/details/state-govt-jobs/andhra-pradesh-govt-jobs/8891242375.pdf', 'Title': 'Notification '}                                          |
| {'Link': 'crash', 'Title': 'Syllabus'}                                                                                                                   |
| {'Link': 'crash', 'Title': 'Eligibility'}                                                                                                                |
| {'Link': 'crash', 'Title': 'Selection Procedure Details'}                                                                                                |
+++++++++++++++++++++++++++++++++++++++++++++++++4.2 min and no exceptions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Winner is multiprocessing.....




















from .models import *
from scrap.models import *
import pathlib
import re
import requests
from bs4 import BeautifulSoup
from random import randint
import shutil


class Details:
    def get_important_links(scrap_model_name,details_model_name,pdf_dir_name):
        scrap_model   = eval(scrap_model_name)
        details_model = eval(details_model_name)
        pdf_dir       = "media/pdf/details/" + pdf_dir_name
        details_model.objects.all().delete()
        try:
            shutil.rmtree(pdf_dir)
        except FileNotFoundError:
            pass
        try:
            pathlib.Path(pdf_dir).mkdir(parents=True, exist_ok=True)
        except FileNotFoundError:
            pass
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        obj = list(scrap_model.objects.values())
        for o in obj:
            if o["type"] == 2:
                join_id = o["join_id"]
                url = o["more_info"]
                ############ Constant variables #####
                page = requests.get(url)
                c = page.content
                soup = BeautifulSoup(c,"html5lib")
                ########################
                if len(soup.find_all("table",{"style":"width: 500px;"})) != 0:
                    row = soup.find_all("table",{"style":"width: 500px;"})[0].find_all('tr')
                else:
                    row = soup.find_all("table",border="2")[0].find_all('tr')
                dict = {}
                for i in row:
                    for title in i.find_all('span', attrs={'style':'color: #008000;'}):
                        dict["Title"] = title.text
                    for link in i.find_all('a',title=True, href=True):
                        pdf_url = link['href']
                        if pdf_url.split(".")[1] == "freejobalert" and re.search(r'.pdf$',pdf_url):
                            pdf_file_name = pdf_dir+"/"+str(randint(9999, 99999999))+".pdf"
                            get_url = requests.get(pdf_url)
                            with open(pdf_file_name,'wb') as pdf:
                                pdf.write(get_url.content)
                            dict["Link"] = pdf_file_name
                        elif pdf_url.split(".")[1] == "freejobalert" and not (re.search(r'.pdf$',pdf_url)):
                            dict["Link"] = "crash"
                        else:
                            dict["Link"] = pdf_url
                        obj = details_model.objects.create(more_info=dict,join_id=join_id)
                        lst.append(dict.copy())
        return lst

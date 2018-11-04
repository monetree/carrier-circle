from .models import *
from scrap.models import *
import pathlib
import re
import requests
from bs4 import BeautifulSoup
from random import randint
import shutil
from multiprocessing.dummy import Pool as ThreadPool

class Details:
    def important_links(url,join_id,pdf_dir,details_model):

        lst=[]
        lst2=[]
        dict={}
        dict2={}
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
                dict['Title'] = title.text.strip().replace("\xa0"," ")
            for link in i.find_all('a',title=True, href=True):
                pdf_url = link['href']
                if pdf_url.split(".")[1] == "freejobalert" and re.search(r'.pdf$',pdf_url):
                    pdf_file_name = pdf_dir+"/"+str(randint(99999, 9999999999))+".pdf"
                    get_url = requests.get(pdf_url)
                    with open(pdf_file_name,'wb') as pdf:
                        pdf.write(get_url.content)
                    dict['Link'] = pdf_file_name
                elif pdf_url.split(".")[1] == "freejobalert" and not (re.search(r'.pdf$',pdf_url)):
                    dict["Link"] = "crash"
                else:
                    dict['Link'] = pdf_url
                # obj = details_model.objects.create(more_info=dict,join_id=join_id)
                lst.append(dict.copy())
        print(len(lst))
        obj = details_model.objects.create(more_info=lst,join_id=join_id)
        return lst
    def get_important_links(scrap_model_name,details_model_name,pdf_dir_name):
        pool = ThreadPool(4)
        urls=[]
        join_ids = []
        scrap_model   = eval(scrap_model_name)
        details_model = eval(details_model_name)
        pdf_dir       = ["media/pdf/details/" + pdf_dir_name]

        try:
            shutil.rmtree(''.join(pdf_dir))
        except FileNotFoundError:
            pass
        try:
            pathlib.Path(''.join(pdf_dir)).mkdir(parents=True, exist_ok=True)
        except FileNotFoundError:
            pass

        details_model.objects.all().delete()
        obj = scrap_model.objects.filter(type=2).values('more_info','join_id')
        for i in obj:
            urls.append(i["more_info"])
            join_ids.append(i["join_id"])
        pdf_dir = pdf_dir * len(urls)
        details_model = [details_model] * len(urls)
        results = pool.starmap(
            Details.important_links,
            zip(urls,join_ids,pdf_dir,details_model)
        )
        return results

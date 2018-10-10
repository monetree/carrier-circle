from .models import *
from scrap.models import *
import pathlib
import re
import requests
from bs4 import BeautifulSoup
from random import randint

class Details:
    def get_important_links(scrap_model_name,details_model_name,pdf_dir_name):
        scrap_model   = eval(scrap_model_name)
        details_model = eval(details_model_name)
        pdf_dir       = "media/pdf/" + pdf_dir_name
        details_model.objects.all().delete()
        try:
            shutil.rmtree(pdf_dir)
        except:
            pathlib.Path(pdf_dir).mkdir(parents=True, exist_ok=True)
        try:
            pathlib.Path(pdf_dir).mkdir(parents=True, exist_ok=True)
        except:
            shutil.rmtree(pdf_dir)
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
                row = soup.find_all("table",{"style":"width: 500px;"})[0].find_all('tr')
                dict = {}
                for i in row:
                    for title in i.find_all('span', attrs={'style':'color: #008000;'}):
                        dict['Title'] = title.text
                    for link in i.find_all('a',title=True, href=True):
                        pdf_url = link['href']
                        pdf_file_name = pdf_dir+"/"+str(randint(99999, 9999999999))+".pdf"
                        get_url = requests.get(pdf_url)
                        with open(pdf_file_name,'wb') as pdf:
                            pdf.write(get_url.content)
                        dict['Link'] = pdf_file_name
                        obj = details_model.objects.create(more_info=dict,join_id=join_id)
                        lst.append(dict.copy())

        return lst

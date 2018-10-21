# import requests
# from bs4 import BeautifulSoup
#
# def display(url):
#   page = requests.get(url)
#   c = page.content
#   soup = BeautifulSoup(c,"html5lib")
#   row = soup.find_all("table",{"style":"width: 500px;"})[0].find_all('tr')
#   dict = {}
#   for i in row:
#       for title in i.find_all('span', attrs={
#       'style':'color: #008000;'}):
#           dict['Title'] = title.text
#       for link in i.find_all('a',attrs={'title':'UPSC'}, href=True):
#           dict['Link'] = link['href']
#           print(dict)
#
# def perform():
#     from multiprocessing.dummy import Pool as ThreadPool
#     pool = ThreadPool(4)
#     results = pool.map(display,
#      ['http://www.freejobalert.com/upsc-advt-no-18/33742/',
#      'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019'])
#
# perform()
#
#
#


import requests
from bs4 import BeautifulSoup
from random import randint


def display(url,pdf_name):
  page = requests.get(url)
  pdf_name = "media/other/"+str(randint(99999, 9999999999))+".pdf"
  c = page.content
  soup = BeautifulSoup(c,"html5lib")
  row = soup.find_all("table",{"style":"width: 500px;"})[0].find_all('tr')
  dict = {}
  for i in row:
      for title in i.find_all('span', attrs={
      'style':'color: #008000;'}):
          dict['Title'] = title.text
      for link in i.find_all('a',attrs={'title':'UPSC'}, href=True):
          dict['Link'] = link['href']
          l = dict["Link"].split(".")
          if "pdf" in l:
              get_url = requests.get(dict['Link'])
              with open(pdf_name,'wb') as pdf:
                  pdf.write(get_url.content)
          else:
              pass
          print(dict)

def perform():
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(4)
    urls=['http://www.freejobalert.com/upsc-advt-no-18/33742/',
    'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019',
    'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019',
    'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019',
    'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019',
    'http://www.freejobalert.com/upsc-advt-no-18/33742/',
    'http://www.freejobalert.com/upsc-advt-no-18/33742/']
    pdf_name = ["media/other/"+str(randint(99999, 9999999999))+".pdf"]
    pdf_name = pdf_name * len(urls)

    results = pool.starmap(
         display,zip(urls,pdf_name)

     )

perform()







"""

import requests
from bs4 import BeautifulSoup
from random import randint


def display(url,ids,pdf_name):
  page = requests.get(url)
  c = page.content
  soup = BeautifulSoup(c,"html5lib")
  print(pdf_name)

  row = soup.find_all("table",{"style":"width: 500px;"})[0].find_all('tr')
  dict = {}
  for i in row:
      for title in i.find_all('span', attrs={
      'style':'color: #008000;'}):
          dict['Title'] = title.text
      for link in i.find_all('a',attrs={'title':'UPSC'}, href=True):
          dict['Link'] = link['href']
          l = dict["Link"].split(".")
          if "pdf" in l:
              get_url = requests.get(dict['Link'])
              with open(pdf_name,'wb') as pdf:
                  pdf.write(get_url.content)
          else:
              pass
          print(dict)

def perform():
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(4)
    pdf_name = ["media/other/"+str(randint(99999, 9999999999))+".pdf"]
    results = pool.starmap(
        display,
        zip(['http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/','http://www.freejobalert.com/upsc-advt-no-18/33742/','http://www.freejobalert.com/upsc-advt-no-18/33742/',
         'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019'],
        [1,2,3,3,345,78,96,78],pdf_name)
     )

perform()

"""

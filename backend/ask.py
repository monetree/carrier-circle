# Function based Thread..
"""
from threading import *
def display(arg):
    print('hello, i am running!')
    print(arg)
t = Thread(target=display,args=(20,))
t.start()
"""

#Class based Thread..
"""
from threading import *
class myclass(Thread):
    def run(self):
        print('i am running')
t = myclass()
t.start()
"""

#Class Based independent thread
"""
from threading import *
class myclass:
    def display(self):
        print('hello m runnning!')
obj=myclass()
t=Thread(target=obj.display)
t.start()
"""

# single tasking -> executing onetask at a time
# preparation of tea
"""
from threading import *
from time import *
class myclass:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print('boil milk + tea powder for 5 min')
        sleep(5)
    def task2(self):
        print('add sugar and boil for another 2 min')
        sleep(2)
    def task3(self):
        print('filter and serve it')
obj = myclass()
if __name__ == "__main__":
    t = Thread(target=obj.prepareTea)
    t.start()
"""

# multithreading
"""
from threading import *
from time import *
class Theater:
    def __init__(self,str):
        self.str = str
    def movietickets(self):
        for i in range(1,11):
            print(self.str,'for ticket no: ',i)
            sleep(1.5)
obj1 = Theater('cut ticket')
obj2 = Theater('show chair')
t1 = Thread(target=obj1.movietickets)
t2 = Thread(target=obj2.movietickets)
t1.start()
t2.start()
"""











# import requests
# import time
# from bs4 import BeautifulSoup
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
#
#
# from multiprocessing.dummy import Pool as ThreadPool
# pool = ThreadPool(4)
# results = pool.map(display, ['http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019','http://www.freejobalert.com/upsc-advt-no-18/33742/',
# 'http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019'])

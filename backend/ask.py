


















# import requests
# from bs4 import BeautifulSoup
# page = requests.get('http://www.freejobalert.com/odisha-govt-jobs/130634/')
# c = page.content
# soup = BeautifulSoup(c,"html.parser")
# row = soup.find_all('table',border="2")[0].find_all('tr')
# dict = {}
# for i in row:
#     for title in i.find_all('span', attrs={'style':'color: #008000;'}):
#         dict["title"] = title
#     for link in i.find_all('a',title=True, href=True):
#         dict["link"] = link["href"]
#         print(dict)
#


# import threading
# import os
# from time import sleep
# from queue import Queue
#
# def task1(a,queue):
#     print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 1: {}".format(os.getpid()))
#     queue.put(a)
#     sleep(0.5)
#
# def task2(b,queue):
#     print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 2: {}".format(os.getpid()))
#     queue.put(b)
#
#
# def get():
#     q1 = Queue()
#     q2 = Queue()
#     t1 = threading.Thread(target=task1, name='t1',args=[10, q1])
#     t1.join()
#     t1.join()
#     t2 = threading.Thread(target=task2, name='t2',args=[20, q2])
#     d1=q1.get()
#     t2.join()
#     t2.join()
#     d2=q2.get()
#
# get()

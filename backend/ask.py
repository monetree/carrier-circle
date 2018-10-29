here is my views.py


    def handler_404(request):
        return render(request, '404.html', status=404)

    def handler_500(request):
        return render(request, '500.html', status=404)


here is my urls.py

    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static
    from finish.views import handler_404,handler_500
    from django.conf.urls import (
                    handler400,
                    handler403,
                    handler404,
                    handler500
                )


    urlpatterns = [
        path('', include("scrap.urls")),
        path('', include("details.urls")),
        path('', include("finalize.urls")),
        path('', include("finish.urls")),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    handler404 = handler_404
    handler500 = handler_500


when i am typing some url in which is not exist
it is coming "Server Error(500)" instead of coming "page not found(404)" error.

Please have a look into this....






















views.py:

    from threading import Thread

    class PoliceJobs:
        def call_police_defence_jobs(request):
            job         = PoliceDefenceJobs.police_jobs(request)
            sleep(0.5)
            job_details = PoliceDefenceJobDetails.police_defence_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)

        def call_statewise_police_jobs(request):
            job         = PoliceDefenceJobs.statewise_police_jobs(request)
            sleep(0.5)
            job_details = PoliceDefenceJobDetails.statewise_police_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)

    def police_jobs(request):
        try:
            t1 = Thread(target=PoliceJobs.call_police_defence_jobs,args=[request])
            t2 = Thread(target=PoliceJobs.call_statewise_police_jobs,args=[request])
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            return HttpResponse("success")
        except:
            return HttpResponse("error")


urls.py

    from django.urls import path
    from .views import police_jobs

    urlpatterns = [
        path('finish_police_jobs/', police_jobs),
    ]



error in shell:

    Traceback (most recent call last):
      File "/usr/lib/python3.5/threading.py", line 914, in _bootstrap_inner
        self.run()
      File "/usr/lib/python3.5/threading.py", line 862, in run
        self._target(*self._args, **self._kwargs)
      File "/home/soubhagya/Desktop/carrier-circle/backend/finalize/views.py", line 840, in call_police_defence_jobs
        job         = PoliceDefenceJobs.police_jobs(request)
    AttributeError: type object 'PoliceDefenceJobs' has no attribute 'police_jobs'


in PoliceJobs class i changed the function name to PoliceDefenceJobs.police_jobs which is not exist to make error.


Here i am making error and handling it by adding except block but
it is still showing error in console but not in browser.
in browser it is showing success wheather there is an exception.


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

from django.shortcuts import render
from details.views import *
from scrap.views import *
from django.http import HttpResponse
from queue import Queue
import threading
from time import sleep

def call_all(job,job_details):
    try:
        if job.status_code and job_details.status_code == 200:
            return "success"
        elif job_details["code"] or job["code"] == 402:
            if job_details["code"] == 402:
                return job_details["traceback"]
            if job["code"]         == 402:
                return job["traceback"]
        else:
            return "Unknown error happened"
    except AttributeError:
        try:
            return job_details["traceback"]
        except KeyError:
            return job["traceback"]

class AllIndiaGovernmentJobs:

    def call_all_india_govt_jobs(request):
        job         = AllIndiaGovtJobs.get_other_all_india(request)
        sleep(0.5)
        job_details = AllIndiaGovtJobDetails.other_all_india_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

class StatewiseGovtJobs:

    def call_andaman_govt_jobs(request):
        job         = StateGovtJobs.andaman_nicobor_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.andaman_nicobar_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_odisha_govt_jobs(request):
        job         = StateGovtJobs.odisha_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.odisha_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

class BankingJobs:
    
    def call_all_bank_jobs(request):
        job         = BankJobs.all_bank_jobs(request)
        sleep(0.5)
        job_details = BankJobDetails.all_bank_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)
    
    def call_other_financial_jobs(request):
        job         = BankJobs.other_financial_jobs(request)
        sleep(0.5)
        job_details = BankJobDetails.other_financial_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)
    
class StatewiseTeachingJobs:
class StatewiseEngineeringJobs:
    
class RailwayJobs:
    
    def call_railway_jobs(request):
    job         = RailwayJobs.railway_jobs(request)
    sleep(0.5)
    job_details = RailwayJobDetails.railway_job_details(request)
    message = call_all(job,job_details)
    return HttpResponse(message)
    
class PoliceJobs:
    def call_police_defence_jobs(request):
        job         = PoliceDefenceJobs.police_defence_jobs(request)
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

from django.shortcuts import render
from details.views import *
from scrap.views import *
from django.http import HttpResponse

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
        job_details = AllIndiaGovtJobDetails.other_all_india_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

class StatewiseGovtJobs:

    def call_andaman_govt_jobs(request):
        job         = StateGovtJobs.andaman_nicobor_govt_jobs(request)
        job_details = StateGovtJobDetails.andaman_nicobar_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_odisha_govt_jobs(request):
        job         = StateGovtJobs.odisha_govt_jobs(request)
        job_details = StateGovtJobDetails.odisha_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

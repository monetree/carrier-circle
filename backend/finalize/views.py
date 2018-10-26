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

    def call_andhra_govt_jobs(request):
        job         = StateGovtJobs.andhra_pradesh_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.andhra_pradesh_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_arunachal_pradesh_govt_jobs(request):
        job         = StateGovtJobs.arunachal_pradesh_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.arunachal_pradesh_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_assam_govt_jobs(request):
        job         = StateGovtJobs.assam_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.assam_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_bihar_govt_jobs(request):
        job         = StateGovtJobs.bihar_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.bihar_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)


    def call_chandigarh_govt_jobs(request):
        job         = StateGovtJobs.chandigarh_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.chandigarh_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_chhattisgarh_govt_jobs(request):
        job         = StateGovtJobs.chhattisgarh_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.chhattisgarh_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_dadra_nagar_govt_jobs(request):
        job         = StateGovtJobs.dadra_nagar_haveli_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.dadra_nagar_haveli_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_daman_diu_govt_jobs(request):
        job         = StateGovtJobs.daman_diu_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.daman_diu_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_delhi_govt_jobs(request):
        job         = StateGovtJobs.delhi_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.delhi_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)

    def call_odisha_govt_jobs(request):
        job         = StateGovtJobs.odisha_govt_jobs(request)
        sleep(0.5)
        job_details = StateGovtJobDetails.odisha_govt_job_details(request)
        message = call_all(job,job_details)
        return HttpResponse(message)


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


from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from scrap.models import *
"""
Scrapping imports
"""
import re
import requests
from bs4 import BeautifulSoup
from random import randint
import urllib.request as urllib
from urllib.request import Request, urlopen, URLError
from lxml import html
from lxml import etree
import shutil # to remove directory
import pathlib # to create directory
from .main import Details
import sys, os
import traceback
from finalize.utils import HandleError
"""
++++++++++++++++
"""

class AllIndiaGovtJobDetails:

    """
    @ Api for UPSC data...
    """
    def upsc_details(request):
        try:
            upsc = list(UpscJobs.objects.values("upsc_id","join_id","more_info"))
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            for u in upsc:
                upsc_id = u["upsc_id"]
                join_id = u["join_id"]
                url     = u["more_info"]

            page = requests.get("http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019")
            c = page.content
            soup=BeautifulSoup(c,"html5lib")
            table=soup.find_all("table")[1]
            trs = table.find_all("tr")
            tds = trs[1].find_all("td")[0].find("span").find("strong").text
            payment = trs[1].find_all("ul")
            if len(payment) != 0:
                li = payment[0].find_all("li")
                for l in li:
                    dict["payment"] = l.text
                    lst.append(dict.copy())
                dict2["payment_details"] = lst
                lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    """
    @ Api for SSC data...
    """
    def ssc_details(request):
        try:
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            ssc_jobs = list(SscJobs.objects.values("ssc_id","type","join_id","more_info"))
            for ssc in ssc_jobs:
                if ssc["type"] == 2:
                    url = ssc["more_info"]
                    r=requests.get("http://www.freejobalert.com/government-JobDetails/")
                    c=r.content
                    soup=BeautifulSoup(c,"html.parser")
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

        """
        @ Api for other All india JobDetails...
        """
    def other_all_india_details(request):
        try:
            api = Details.get_important_links(
             "OtherAllIndiaJobs",
             "OtherAllIndiaJobDetails",
             "all-india-govt-jobs/other-all-india-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    """
    @ Api for STATE GOVT. data...
    """
class StateGovtJobDetails:
    def andaman_nicobar_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "AndamanNicoborGovtJobs",
             "AndamanNicoborGovtJobDetails",
             "state-govt-jobs/andaman-nicobar-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andhra_pradesh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "AndhraPradeshGovtJobs",
             "AndhraPradeshGovtJobDetails",
             "state-govt-jobs/andhra-pradesh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def arunachal_pradesh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "ArunachalPradeshGovernmentjobs",
             "ArunachalPradeshGovernmentJobDetails",
             "state-govt-jobs/arunachal-pradesh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def assam_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "AssamGovtJobs",
             "AssamGovtJobDetails",
             "state-govt-jobs/assam-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def bihar_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "BiharGovtJobs",
             "BiharGovtJobDetails",
             "state-govt-jobs/bihar-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chandigarh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "ChandigarhGovtJobs",
             "ChandigarhGovtJobDetails",
             "state-govt-jobs/chandigarh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chhattisgarh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "ChhattisgarhGovtJobs",
             "ChhattisgarhGovtJobDetails",
             "state-govt-jobs/chandigarh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def dadra_nagar_haveli_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "DadraNagarHaveliGovtJobs",
             "DadraNagarHaveliGovtJobDetails",
             "state-govt-jobs/dadra-nagar-haveli-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def daman_diu_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "DamanDiuGovtJobs",
             "DamanDiuGovtJobDetails",
             "state-govt-jobs/daman-diu-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def delhi_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "DelhiGovtJobs",
             "DelhiGovtJobDetails",
             "state-govt-jobs/delhi-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def goa_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "GoaGovernmentjobs",
             "GoaGovernmentJobDetails",
             "state-govt-jobs/goa-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def gujurat_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "GujuratGovtJobs",
             "GujuratGovtJobDetails",
             "state-govt-jobs/gujurat-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def haryana_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "HaryanaGovtJobs",
             "HaryanaGovtJobDetails",
             "state-govt-jobs/haryana-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def himachal_pradesh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "HimachalPradeshGovtJobs",
             "HimachalPradeshGovtJobDetails",
             "state-govt-jobs/himachal-pradesh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jammu_kashmir_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "JammuKashmirGovtJobs",
             "JammuKashmirGovtJobDetails",
             "state-govt-jobs/jammu-kashmir-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jharkhand_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "JharkhandGovtJobs",
             "JharkhandGovtJobDetails",
             "state-govt-jobs/jharkhand-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def karnataka_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "KarnatakaGovtJobs",
             "KarnatakaGovtJobDetails",
             "state-govt-jobs/karnataka-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def kerala_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "KeralaGovtJobs",
             "KeralaGovtJobDetails",
             "state-govt-jobs/kerala-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def lakshadweep_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "LakshadweepGovernmentjobs",
             "LakshadweepGovernmentJobDetails",
             "state-govt-jobs/lakshadweep-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def madhya_pradesh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "MadhyaPradeshGovtJobs",
             "MadhyaPradeshGovtJobDetails",
             "state-govt-jobs/madhya-pradesh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def maharashtra_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "MaharashtraGovtJobs",
             "MaharashtraGovtJobDetails",
             "state-govt-jobs/maharashtra-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def manipur_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "ManipurGovtJobs",
             "ManipurGovtJobDetails",
             "state-govt-jobs/manipur-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def meghalaya_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "MeghalayaGovtJobs",
             "MeghalayaGovtJobDetails",
             "state-govt-jobs/meghalaya-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def mizoram_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "MizoramGovtJobs",
             "MizoramGovtJobDetails",
             "state-govt-jobs/mizoram-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def nagaland_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "NagalandGovtJobs",
             "NagalandGovtJobDetails",
             "state-govt-jobs/nagaland-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def odisha_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "OdishaGovtJobs",
             "OdishaGovtJobDetails",
             "state-govt-jobs/odisha-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def puduchhery_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "PuduchheryGovtJobs",
             "PuduchheryGovtJobDetails",
             "state-govt-jobs/puduchhery-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def punjab_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "PunjabGovernmentjobs",
             "PunjabGovernmentJobDetails",
             "state-govt-jobs/punjab-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def rajasthan_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "RajasthanGovtJobs",
             "RajasthanGovtJobDetails",
             "state-govt-jobs/rajasthan-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def sikkim_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "SikkimGovtJobs",
             "SikkimGovtJobDetails",
             "state-govt-jobs/sikkim-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tamil_nadu_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "TamilGovtJobs",
             "TamilGovtJobDetails",
             "state-govt-jobs/tamilnadu-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def telangana_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "TelanganaGovtJobs",
             "TelanganaGovtJobDetails",
             "state-govt-jobs/telangana-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tripura_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "TripuraGovtJobs",
             "TripuraGovtJobDetails",
             "state-govt-jobs/tripura-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttarakhand_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "UttarakhandGovtJobs",
             "UttarakhandGovtJobDetails",
             "state-govt-jobs/uttarakhand-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttar_pradesh_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "UttarPradeshGovtJobs",
             "UttarPradeshGovtJobDetails",
             "state-govt-jobs/uttar-pradesh-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def west_bengal_govt_job_details(request):
        try:
            api = Details.get_important_links(
             "WestBengalGovtJobs",
             "WestBengalGovtJobDetails",
             "state-govt-jobs/west-bengal-govt-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    """
    @ Api for BANK GOVT. data...
    """

class BankJobDetails:
    def all_bank_job_details(request):
        try:
            api = Details.get_important_links(
             "AllBankJobs",
             "AllBankJobDetails",
             "all-bank-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def other_financial_job_details(request):
        try:
            api = Details.get_important_links(
             "OtherFinancialJobs",
             "OtherFinancialJobDetails",
             "other-financial-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    """
    @ Api for TEACHING JobDetails...
    """


class TeachingJobDetails:

    def all_india_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "AllIndiaTeachingJobs",
             "AllIndiaTeachingJobDetails",
             "teaching-jobs/all-india-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andaman_nicobar_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "AndamanNicoborTeachingJobs",
             "AndamanNicoborTeachingJobDetails",
             "teaching-jobs/andaman-nicobar-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andhra_pradesh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "AndhraPradeshTeachingJobs",
             "AndhraPradeshTeachingJobDetails",
             "teaching-jobs/andhra-pradesh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def arunachal_pradesh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "ArunachalPradeshTeachingJobs",
             "ArunachalPradeshTeachingJobDetails",
             "teaching-jobs/arunachal-pradesh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def assam_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "AssamTeachingJobs",
             "AssamTeachingJobDetails",
             "assam-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def bihar_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "BiharTeachingJobs",
             "BiharTeachingJobDetails",
             "teaching-jobs/bihar-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chandigarh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "ChandigarhTeachingJobs",
             "ChandigarhTeachingJobDetails",
             "teaching-jobs/chandigarh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chhattisgarh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "ChhattisgarhTeachingJobs",
             "ChhattisgarhTeachingJobDetails",
             "teaching-jobs/chandigarh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def dadra_nagar_haveli_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "DadraNagarHaveliTeachingJobs",
             "DadraNagarHaveliTeachingJobDetails",
             "teaching-jobs/dadra-nagar-haveli-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def daman_diu_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "DamanDiuTeachingJobs",
             "DamanDiuTeachingJobDetails",
             "teaching-jobs/daman-diu-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def delhi_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "DelhiTeachingJobs",
             "DelhiTeachingJobDetails",
             "teaching-jobs/delhi-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def goa_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "GoaTeachingJobs",
             "GoaTeachingJobDetails",
             "teaching-jobs/goa-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def gujurat_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "GujuratTeachingJobs",
             "GujuratTeachingJobDetails",
             "teaching-jobs/gujurat-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def haryana_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "HaryanaTeachingJobs",
             "HaryanaTeachingJobDetails",
             "teaching-jobs/haryana-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def himachal_pradesh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "HimachalPradeshTeachingJobs",
             "HimachalPradeshTeachingJobDetails",
             "teaching-jobs/himachal-pradesh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jammu_kashmir_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "JammuKashmirTeachingJobs",
             "JammuKashmirTeachingJobDetails",
             "teaching-jobs/jammu-kashmir-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jharkhand_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "JharkhandTeachingJobs",
             "JharkhandTeachingJobDetails",
             "teaching-jobs/jharkhand-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def karnataka_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "KarnatakaTeachingJobs",
             "KarnatakaTeachingJobDetails",
             "teaching-jobs/karnataka-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def kerala_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "KeralaTeachingJobs",
             "KeralaTeachingJobDetails",
             "teaching-jobs/kerala-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def lakshadweep_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "LakshadweepTeachingJobs",
             "LakshadweepTeachingJobDetails",
             "teaching-jobs/lakshadweep-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def madhya_pradesh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "MadhyaPradeshTeachingJobs",
             "MadhyaPradeshTeachingJobDetails",
             "teaching-jobs/madhya-pradesh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def maharashtra_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "MaharashtraTeachingJobs",
             "MaharashtraTeachingJobDetails",
             "teaching-jobs/maharashtra-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def manipur_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "ManipurTeachingJobs",
             "ManipurTeachingJobDetails",
             "teaching-jobs/manipur-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def meghalaya_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "MeghalayaTeachingJobs",
             "MeghalayaTeachingJobDetails",
             "teaching-jobs/meghalaya-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def mizoram_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "MizoramTeachingJobs",
             "MizoramTeachingJobDetails",
             "teaching-jobs/mizoram-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def nagaland_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "NagalandTeachingJobs",
             "NagalandTeachingJobDetails",
             "teaching-jobs/nagaland-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def odisha_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "OdishaTeachingJobs",
             "OdishaTeachingJobDetails",
             "teaching-jobs/odisha-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def puduchhery_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "PuduchheryTeachingJobs",
             "PuduchheryTeachingJobDetails",
             "teaching-jobs/puduchhery-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def punjab_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "PunjabTeachingJobs",
             "PunjabTeachingJobDetails",
             "teaching-jobs/punjab-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def rajasthan_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "RajasthanTeachingJobs",
             "RajasthanTeachingJobDetails",
             "teaching-jobs/rajasthan-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def sikkim_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "SikkimTeachingJobs",
             "SikkimTeachingJobDetails",
             "teaching-jobs/sikkim-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tamil_nadu_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "TamilNaduTeachingJobs",
             "TamilNaduTeachingJobDetails",
             "teaching-jobs/tamilnadu-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def telangana_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "TelanganaTeachingJobs",
             "TelanganaTeachingJobDetails",
             "teaching-jobs/telangana-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tripura_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "TripuraTeachingJobs",
             "TripuraTeachingJobDetails",
             "teaching-jobs/tripura-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttarakhand_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "UttarakhandTeachingJobs",
             "UttarakhandTeachingJobDetails",
             "teaching-jobs/uttarakhand-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttar_pradesh_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "UttarPradeshTeachingJobs",
             "UttarPradeshTeachingJobDetails",
             "teaching-jobs/uttar-pradesh-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def west_bengal_teaching_job_details(request):
        try:
            api = Details.get_important_links(
             "WestBengalTeachingJobs",
             "WestBengalTeachingJobDetails",
             "teaching-jobs/west-bengal-teaching-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

"""
@ Api for ENGG JobDetails...
"""


class EnggJobDetails:
    def all_india_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "AllIndiaEnggJobs",
             "AllIndiaEnggJobDetails",
             "Engg-jobs/all-india-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def all_india_fellow_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "AllIndiaFellowEnggJobs",
             "AllIndiaFellowEnggJobDetails",
             "Engg-jobs/all-india-fellow-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andaman_nicobar_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "AndamanNicoborEnggJobs",
             "AndamanNicoborEnggJobDetails",
             "Engg-jobs/andaman-nicobar-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andhra_pradesh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "AndhraPradeshEnggJobs",
             "AndhraPradeshEnggJobDetails",
             "Engg-jobs/andhra-pradesh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def arunachal_pradesh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "ArunachalPradeshEnggJobs",
             "ArunachalPradeshEnggJobDetails",
             "Engg-jobs/arunachal-pradesh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def assam_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "AssamEnggJobs",
             "AssamEnggJobDetails",
             "assam-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def bihar_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "BiharEnggJobs",
             "BiharEnggJobDetails",
             "Engg-jobs/bihar-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chandigarh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "ChandigarhEnggJobs",
             "ChandigarhEnggJobDetails",
             "Engg-jobs/chandigarh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chhattisgarh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "ChhattisgarhEnggJobs",
             "ChhattisgarhEnggJobDetails",
             "Engg-jobs/chandigarh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def dadra_nagar_haveli_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "DadraNagarHaveliEnggJobs",
             "DadraNagarHaveliEnggJobDetails",
             "Engg-jobs/dadra-nagar-haveli-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def daman_diu_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "DamanDiuEnggJobs",
             "DamanDiuEnggJobDetails",
             "Engg-jobs/daman-diu-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def delhi_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "DelhiEnggJobs",
             "DelhiEnggJobDetails",
             "Engg-jobs/delhi-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def goa_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "GoaEnggJobs",
             "GoaEnggJobDetails",
             "Engg-jobs/goa-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def gujurat_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "GujuratEnggJobs",
             "GujuratEnggJobDetails",
             "Engg-jobs/gujurat-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def haryana_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "HaryanaEnggJobs",
             "HaryanaEnggJobDetails",
             "Engg-jobs/haryana-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def himachal_pradesh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "HimachalPradeshEnggJobs",
             "HimachalPradeshEnggJobDetails",
             "Engg-jobs/himachal-pradesh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jammu_kashmir_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "JammuKashmirEnggJobs",
             "JammuKashmirEnggJobDetails",
             "Engg-jobs/jammu-kashmir-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jharkhand_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "JharkhandEnggJobs",
             "JharkhandEnggJobDetails",
             "Engg-jobs/jharkhand-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def karnataka_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "KarnatakaEnggJobs",
             "KarnatakaEnggJobDetails",
             "Engg-jobs/karnataka-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def kerala_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "KeralaEnggJobs",
             "KeralaEnggJobDetails",
             "Engg-jobs/kerala-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def lakshadweep_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "LakshadweepEnggJobs",
             "LakshadweepEnggJobDetails",
             "Engg-jobs/lakshadweep-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def madhya_pradesh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "MadhyaPradeshEnggJobs",
             "MadhyaPradeshEnggJobDetails",
             "Engg-jobs/madhya-pradesh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def maharashtra_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "MaharashtraEnggJobs",
             "MaharashtraEnggJobDetails",
             "Engg-jobs/maharashtra-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def manipur_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "ManipurEnggJobs",
             "ManipurEnggJobDetails",
             "Engg-jobs/manipur-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def meghalaya_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "MeghalayaEnggJobs",
             "MeghalayaEnggJobDetails",
             "Engg-jobs/meghalaya-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def mizoram_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "MizoramEnggJobs",
             "MizoramEnggJobDetails",
             "Engg-jobs/mizoram-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def nagaland_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "NagalandEnggJobs",
             "NagalandEnggJobDetails",
             "Engg-jobs/nagaland-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def odisha_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "OdishaEnggJobs",
             "OdishaEnggJobDetails",
             "Engg-jobs/odisha-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def puduchhery_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "PuduchheryEnggJobs",
             "PuduchheryEnggJobDetails",
             "Engg-jobs/puduchhery-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def punjab_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "PunjabEnggJobs",
             "PunjabEnggJobDetails",
             "Engg-jobs/punjab-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def rajasthan_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "RajasthanEnggJobs",
             "RajasthanEnggJobDetails",
             "Engg-jobs/rajasthan-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def sikkim_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "SikkimEnggJobs",
             "SikkimEnggJobDetails",
             "Engg-jobs/sikkim-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tamil_nadu_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "TamilNaduEnggJobs",
             "TamilNaduEnggJobDetails",
             "Engg-jobs/tamilnadu-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def telangana_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "TelanganaEnggJobs",
             "TelanganaEnggJobDetails",
             "Engg-jobs/telangana-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tripura_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "TripuraEnggJobs",
             "TripuraEnggJobDetails",
             "Engg-jobs/tripura-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttarakhand_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "UttarakhandEnggJobs",
             "UttarakhandEnggJobDetails",
             "Engg-jobs/uttarakhand-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttar_pradesh_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "UttarPradeshEnggJobs",
             "UttarPradeshEnggJobDetails",
             "Engg-jobs/uttar-pradesh-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def west_bengal_engg_job_details(request):
        try:
            api = Details.get_important_links(
             "WestBengalEnggJobs",
             "WestBengalEnggJobDetails",
             "Engg-jobs/west-bengal-engg-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

"""
@ Api for RAILWAY JobDetails...
"""

class RailwayJobDetails:
    def railway_job_details(request):
        try:
            api = Details.get_important_links(
             "RailwayJobsModel",
             "RailwayJobDetails",
             "railway-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class PoliceDefenceJobDetails:
    def police_defence_job_details(request):
        try:
            api = Details.get_important_links(
             "PoliceAndDefenceJobs",
             "PoliceAndDefenceJobDetails",
             "police-and-defence-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def statewise_police_job_details(request):
        try:
            api = Details.get_important_links(
             "StatewisePoliceJobs",
             "StatewisePoliceJobDetails",
             "statewise-police-and-defence-jobs"
             )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

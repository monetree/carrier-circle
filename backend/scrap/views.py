
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import (
            #all india govt jobs model
            UpscJobs,SscJobs,OtherAllIndiaJobs,
            #statewise govt jobs model
            OdishaGovtJobs,AndamanNicoborGovtJobs,AndhraPradeshGovtJobs,
            ArunachalPradeshGovernmentjobs,AssamGovtJobs,
            BiharGovtJobs,ChandigarhGovtJobs,ChhattisgarhGovtJobs,
            DadraNagarHaveliGovtJobs,DamanDiuGovtJobs,
            DelhiGovtJobs,GoaGovernmentjobs,GujuratGovtJobs,
            HaryanaGovtJobs,HimachalPradeshGovtJobs,
            JammuKashmirGovtJobs,JharkhandGovtJobs,KarnatakaGovtJobs,
            KeralaGovtJobs,LakshadweepGovernmentjobs,MadhyaPradeshGovtJobs,
            MaharashtraGovtJobs,ManipurGovtJobs,MeghalayaGovtJobs,
            MizoramGovtJobs,NagalandGovtJobs,PuduchheryGovtJobs,
            PunjabGovernmentjobs,RajasthanGovtJobs,SikkimGovtJobs,
            TamilGovtJobs,TelanganaGovtJobs,TripuraGovtJobs,
            UttarakhandGovtJobs,UttarPradeshGovtJobs,WestBengalGovtJobs,
            #bank jobs model
            AllBankJobs,OtherFinancialJobs,
            #all india teaching jobs model
            AllIndiaTeachingJobs,
            OdishaTeachingJobs,AndamanNicoborTeachingJobs,AndhraPradeshTeachingJobs,
            ArunachalPradeshTeachingJobs,AssamTeachingJobs,
            BiharTeachingJobs,ChandigarhTeachingJobs,ChhattisgarhTeachingJobs,
            DadraNagarHaveliTeachingJobs,DamanDiuTeachingJobs,
            DelhiTeachingJobs,GoaTeachingJobs,GujuratTeachingJobs,
            HaryanaTeachingJobs,HimachalPradeshTeachingJobs,
            JammuKashmirTeachingJobs,JharkhandTeachingJobs,KarnatakaTeachingJobs,
            KeralaTeachingJobs,LakshadweepTeachingJobs,MadhyaPradeshTeachingJobs,
            MaharashtraTeachingJobs,ManipurTeachingJobs,MeghalayaTeachingJobs,
            MizoramTeachingJobs,NagalandTeachingJobs,PuduchheryTeachingJobs,
            PunjabTeachingJobs,RajasthanTeachingJobs,SikkimTeachingJobs,
            TamilNaduTeachingJobs,TelanganaTeachingJobs,TripuraTeachingJobs,
            UttarakhandTeachingJobs,UttarPradeshTeachingJobs,WestBengalTeachingJobs,
            #all india engineering jobs model
            AllIndiaEnggJobs,AllIndiaFellowEnggJobs,
            OdishaEnggJobs,AndamanNicoborEnggJobs,AndhraPradeshEnggJobs,
            ArunachalPradeshEnggJobs,AssamEnggJobs,
            BiharEnggJobs,ChandigarhEnggJobs,ChhattisgarhEnggJobs,
            DadraNagarHaveliEnggJobs,DamanDiuEnggJobs,
            DelhiEnggJobs,GoaEnggJobs,GujuratEnggJobs,
            HaryanaEnggJobs,HimachalPradeshEnggJobs,
            JammuKashmirEnggJobs,JharkhandEnggJobs,KarnatakaEnggJobs,
            KeralaEnggJobs,LakshadweepEnggJobs,MadhyaPradeshEnggJobs,
            MaharashtraEnggJobs,ManipurEnggJobs,MeghalayaEnggJobs,
            MizoramEnggJobs,NagalandEnggJobs,PuduchheryEnggJobs,
            PunjabEnggJobs,RajasthanEnggJobs,SikkimEnggJobs,
            TamilNaduEnggJobs,TelanganaEnggJobs,TripuraEnggJobs,
            UttarakhandEnggJobs,UttarPradeshEnggJobs,WestBengalEnggJobs,
            #railway jobs model
            RailwayJobsModel,
            #police & defence jobs model,
            StatewisePoliceJobs,PoliceAndDefenceJobs,
            )

"""
Scrapping imports
"""
import re
import requests
from bs4 import BeautifulSoup
from random import randint
import pathlib
from .main import create_delete_pdf_dir, download_pdf
import sys, os
import traceback
from finalize.utils import HandleError
"""
++++++++++++++++
"""

class AllIndiaGovtJobs:

    """
    @ Api for UPSC data...
    """

    def get_upsc(request):
        try:
            #empty model
            UpscJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/upsc_jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/government-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[0].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["post_name"] = d[1].text
                dict["education"] = d[2].text
                dict["last_date"] = d[4].text
                l=d[5].text
                if l != "":
                    link = d[5].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[5].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[5].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = UpscJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=UpscJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["education"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=join_id
                    )
                lst.append(dict.copy())
            dict2["upsc"] = lst
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
    def get_ssc(request):
        try:
            #empty model
            SscJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/ssc_jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/government-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[1].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["post_name"] = d[1].text
                dict["qualification"] = d[2].text
                dict["last_date"] = d[4].text
                l=d[5].text
                if l != "":
                    link = d[5].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[5].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[5].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = SscJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=SscJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["qualification"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=join_id
                    )
                lst.append(dict.copy())
            dict2["ssc"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

        """
        @ Api for other All india jobs...
        """
    def get_other_all_india(request):
        try:
            #empty model
            OtherAllIndiaJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/all_india_govt_jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/government-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[2].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["requirement_board"] = d[1].text
                dict["post_name"] = d[2].text
                dict["qualification"] = d[3].text
                dict["last_date"] = d[5].text
                l=d[6].text
                if l != "":
                    link = d[6].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    # check the existing of join_id
                    count_join_id = OtherAllIndiaJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    # insert into mysql database
                    obj=OtherAllIndiaJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["qualification"],
                        more_info=dict["more_info"],type=dict["type"],
                        requirement_board=dict["requirement_board"],
                        job_id=dict["job_id"],join_id=join_id
                    )
                lst.append(dict.copy())
            dict2["other_all_india"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors


    """
    @ Api for STATE GOVT. data...
    """
class StateGovtJobs:
    def get_all_state(url,keyword,model_name,pdf_file):
        #empty model
        model = eval(model_name)
        model.objects.all().delete()
        pdf_dir = "media/pdf/scrap/statewise_govt_jobs/" + pdf_file
        create_delete_pdf_dir(pdf_dir)
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get(url)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
        data=all[0].find_all("tr",{"style":"border: 1px solid #000000;"})
        for i in data:
            d = i.find_all("td")
            dict["start_date"] = d[0].text
            dict["requirement_board"] = d[1].text
            dict["post_name"] = d[2].text
            dict["qualification"] = d[3].text
            dict["last_date"] = d[5].text
            l=d[6].text
            if l != "":
                link = d[6].find("strong").find("a")['href']
                if link.split(".")[1] == "freejobalert":
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 2
                    link_remove_slash = link.split("/")
                    link_to_string = (''.join(link_remove_slash))
                    job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                    if len(job_id) == 5:
                        dict["job_id"] = int(job_id)
                    elif len(job_id) == 7:
                        dict["job_id"] = int(job_id[2::])
                    else:
                        dict["job_id"] = None
                else:
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 1
                    dict["job_id"] = None
                join_id = randint(99999, 999999)
                #check the existing of join_id
                count_join_id = model.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                        pdf_url = link
                        pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                        download_pdf(pdf_url,pdf_file_name)
                        dict["more_info"] = pdf_file_name
                #insert into mysql database
                obj = model.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["qualification"],
                    more_info=dict["more_info"],type=dict["type"],
                    requirement_board=dict["requirement_board"],
                    job_id=dict["job_id"],join_id=join_id
                )

            lst.append(dict.copy())
        dict2[keyword] = lst
        lst2.append(dict2)
        return lst2

    def odisha_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/odisha-government-jobs/",
                "odisha_govt_jobs",
                "OdishaGovtJobs",
                "odisha_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andaman_nicobor_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/an-government-jobs/",
                "andaman_nicobor_govt_jobs",
                "AndamanNicoborGovtJobs",
                "andaman_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andhra_prtadesh_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/ap-government-jobs/",
                "andhra_prtadesh_govt_jobs",
                "AndhraPradeshGovtJobs",
                "andhra_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def arunachal_pradesh_government_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/arunachal-pradesh-government-jobs/",
                "arunachal_pradesh_government_jobs",
                "ArunachalPradeshGovernmentjobs",
                "arunachal_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def assam_govt_jobs(request):
        api = StateGovtJobs.get_all_state(
            "http://www.freejobalert.com/assam-government-jobs/",
            "assam_govt_jobs",
            "AssamGovtJobs",
            "assam_govt_jobs/"
        )
        return JsonResponse(api,safe=False)

    def bihar_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/bihar-government-jobs/",
                "bihar_govt_jobs",
                "BiharGovtJobs",
                "bihar_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chandigarh_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/chandigarh-government-jobs/",
                "chandigarh_govt_jobs",
                "ChandigarhGovtJobs",
                "chandigarh_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chhattisgarh_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/chhattisgarh-government-jobs/",
                "chhattisgarh_govt_jobs",
                "ChhattisgarhGovtJobs",
                "chandigarh_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def dadra_nagar_haveli_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/dadra-nagar-haveli-government-jobs/",
                "dadra_nagar_haveli_govt_jobs",
                "DadraNagarHaveliGovtJobs",
                "dadra_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def daman_diu_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/daman-diu-government-jobs/",
                "daman_diu_govt_jobs",
                "DamanDiuGovtJobs",
                "daman_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def delhi_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/delhi-government-jobs/",
                "delhi_govt_jobs",
                "DelhiGovtJobs",
                "delhi_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def goa_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/goa-government-jobs/",
                "goa_govt_jobs",
                "GoaGovernmentjobs",
                "goa_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def gujurat_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/gujarat-government-jobs/",
                "gujurat_govt_jobs",
                "GujuratGovtJobs",
                "gujurat_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def haryana_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/haryana-government-jobs/",
                "haryana_govt_jobs",
                "HaryanaGovtJobs",
                "haryana_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def himachal_pradesh_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/hp-government-jobs/",
                "himachal_pradesh_govt_jobs",
                "HimachalPradeshGovtJobs",
                "himachal_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jammu_kashmir_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/jk-government-jobs/",
                "jammu_kashmir_govt_jobs",
                "JammuKashmirGovtJobs",
                "jammu_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jharkhand_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/jharkhand-government-jobs/",
                "jharkhand_govt_jobs",
                "JharkhandGovtJobs",
                "jharkhand_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def karnataka_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/karnataka-government-jobs/",
                "karnataka_govt_jobs",
                "KarnatakaGovtJobs",
                "karnataka_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def kerala_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/kerala-government-jobs/",
                "kerala_govt_jobs",
                "KeralaGovtJobs",
                "kerala_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def lakshadweep_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/lakshadweep-government-jobs/",
                "lakshadweep_govt_jobs",
                "LakshadweepGovernmentjobs",
                "lakshadweep_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def madhya_pradesh_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/mp-government-jobs/",
                "madhya_pradesh_govt_jobs",
                "MadhyaPradeshGovtJobs",
                "madhya_pradesh_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def maharashtra_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/maharashtra-government-jobs/",
                "maharashtra_govt_jobs",
                "MaharashtraGovtJobs",
                "maharashtra_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def manipur_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/manipur-government-jobs/",
                "manipur_govt_jobs",
                "ManipurGovtJobs",
                "maniput_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def meghalaya_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/meghalaya-government-jobs/",
                "meghalaya_govt_jobs",
                "MeghalayaGovtJobs",
                "meghalaya-govbt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def mizoram_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/mizoram-government-jobs/",
                "mizoram_govt_jobs",
                "MizoramGovtJobs",
                "mizoram_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def nagaland_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/nagaland-government-jobs/",
                "nagaland_govt_jobs",
                "NagalandGovtJobs",
                "nagaland_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def puduchhery_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/puduchhery-government-jobs/",
                "puduchhery_govt_jobs",
                "PuduchheryGovtJobs",
                "puduchhery_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def punjab_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/punjab-government-jobs/",
                "punjab_govt_jobs",
                "PunjabGovernmentjobs",
                "punjab_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def rajasthan_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/rajasthan-government-jobs/",
                "rajasthan_govt_jobs",
                "RajasthanGovtJobs",
                "rajasthan_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def sikkim_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/sikkim-government-jobs/",
                "sikkim_govt_jobs",
                "SikkimGovtJobs",
                "sikkim_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tamil_nadu_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/tn-government-jobs/",
                "tamil_nadu_govt_jobs",
                "TamilGovtJobs",
                "tamil_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def telangana_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/telangana-government-jobs/",
                "telangana_govt_jobs",
                "TelanganaGovtJobs",
                "telengana_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tripura_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/tripura-government-jobs/",
                "tripura_govt_jobs",
                "TripuraGovtJobs",
                "tripura_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttarakhand_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/uttarakhand-government-jobs/",
                "uttarakhand_govt_jobs",
                "UttarakhandGovtJobs",
                "uttarakhand_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttar_pradesh_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/up-government-jobs/",
                "uttar_pradesh_govt_jobs",
                "UttarPradeshGovtJobs",
                "uttarpradesh_govt_jobs/"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def west_bengal_govt_jobs(request):
        try:
            api = StateGovtJobs.get_all_state(
                "http://www.freejobalert.com/wb-government-jobs/",
                "west_bengal_govt_jobs",
                "WestBengalGovtJobs",
                "west_bengal_govt_jobs/"
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

class BankJobs:
    def all_bank_jobs(request):
        try:
            #empty model
            AllBankJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/all_bank_jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/bank-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[0].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["bank_name"]  = d[1].text
                dict["post_name"]  = d[2].text
                dict["education"] = d[3].text
                dict["last_date"] = d[5].text
                l=d[6].text
                if l != "":
                    link = d[6].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = AllBankJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=AllBankJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["education"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=randint(99999, 999999)
                    )
                lst.append(dict.copy())
            dict2["all_bank_jobs"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def other_financial_jobs(request):
        try:
            #empty model
            OtherFinancialJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/other_financial_jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/bank-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[1].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["requirement_board"] = d[1].text
                dict["post_name"] = d[2].text
                dict["education"] = d[3].text
                dict["last_date"] = d[5].text
                l=d[6].text
                if l != "":
                    link = d[6].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = OtherFinancialJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=OtherFinancialJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["education"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=randint(99999, 999999)
                    )
                lst.append(dict.copy())
            dict2["other_financial_jobs"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    """
    @ Api for TEACHING jobs...
    """
class TeachingJobs:
    def common_teaching_jobs(index,keyword,model_name):
        model = eval(model_name)
        #empty model
        model.objects.all().delete()
        pdf_dir = "media/pdf/scrap/teaching_jobs/" + re.sub("_","-",keyword) + "/"
        create_delete_pdf_dir(pdf_dir)
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/teaching-faculty-jobs/")
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
        data=all[index].find_all("tr",{"style":"border: 1px solid #000000;"})
        for i in data:
            d = i.find_all("td")
            dict["start_date"] = d[0].text
            dict["requirement_board"] = d[1].text
            dict["post_name"] = d[2].text
            dict["education"] = d[3].text
            dict["last_date"] = d[5].text
            l=d[6].text
            if l != "":
                link = d[6].find("strong").find("a")['href']
                if link.split(".")[1] == "freejobalert":
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 2
                    link_remove_slash = link.split("/")
                    link_to_string = (''.join(link_remove_slash))
                    job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                    if len(job_id) == 5:
                        dict["job_id"] = int(job_id)
                    elif len(job_id) == 7:
                        dict["job_id"] = int(job_id[2::])
                    else:
                        dict["job_id"] = None
                else:
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 1
                    dict["job_id"] = None
                join_id = randint(99999, 999999)
                #check the existing of join_id
                count_join_id = model.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                        pdf_url = link
                        pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                        download_pdf(pdf_url,pdf_file_name)
                        dict["more_info"] = pdf_file_name
                #insert into mysql database
                obj=model.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["education"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2[keyword] = lst
        lst2.append(dict2)
        return lst2

    def all_india_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                0,
                "all_india_teaching_jobs",
                "AllIndiaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andaman_nicobar_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                1,
                "andaman_nicobar_teaching_jobs",
                "AndamanNicoborTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andhra_pradesh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                2,
                "andhra_pradesh_teaching_jobs",
                "AndhraPradeshTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def arunachal_pradesh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                3,
                "arunachal_pradesh_teaching_jobs",
                "ArunachalPradeshTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def assam_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                4,
                "assam_teaching_jobs",
                "AssamTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def bihar_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                5,
                "bihar_teaching_jobs",
                "BiharTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chandigarh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                6,
                "chandigarh_teaching_jobs",
                "ChandigarhTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chhattisgarh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                7,
                "chhattisgarh_teaching_jobs",
                "ChhattisgarhTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def dadra_nagar_haveli_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                8,
                "dadra_nagar_haveli_teaching_jobs",
                "DadraNagarHaveliTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def daman_diu_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                9,
                "daman_diu_teaching_jobs",
                "DamanDiuTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def delhi_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                10,
                "delhi_teaching_jobs",
                "DelhiTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def goa_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                11,
                "goa_teaching_jobs",
                "GoaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def gujurat_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                12,
                "gujurat_teaching_jobs",
                "GujuratTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def haryana_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                13,
                "haryana_teaching_jobs",
                "HaryanaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors
    def himachal_pradesh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                14,
                "himachal_pradesh_teaching_jobs",
                "HimachalPradeshTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jammu_kashmir_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                15,
                "jammu_kashmir_teaching_jobs",
                "JammuKashmirTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jharkhand_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                16,
                "jharkhand_teaching_jobs",
                "JharkhandTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def karnataka_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                17,
                "karnataka_teaching_jobs",
                "KarnatakaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def kerala_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                18,
                "kerala_teaching_jobs",
                "KeralaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def lakshadweep_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                19,
                "lakshadweep_teaching_jobs",
                "LakshadweepTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def madhya_pradesh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                20,
                "madhya_pradesh_teaching_jobs",
                "MadhyaPradeshTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def maharashtra_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                21,
                "maharashtra_teaching_jobs",
                "MaharashtraTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def manipur_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                22,
                "manipur_teaching_jobs",
                "ManipurTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def meghalaya_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                23,
                "meghalaya_teaching_jobs",
                "MeghalayaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def mizoram_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                24,
                "mizoram_teaching_jobs",
                "MizoramTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def nagaland_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                25,
                "nagaland_teaching_jobs",
                "NagalandTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def odisha_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                26,
                "odisha_teaching_jobs",
                "OdishaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def puduchhery_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                27,
                "puduchhery_teaching_jobs",
                "PuduchheryTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def punjab_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                28,
                "punjab_teaching_jobs",
                "PunjabTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def rajasthan_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                29,
                "rajasthan_teaching_jobs",
                "RajasthanTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def sikkim_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                30,
                "sikkim_teaching_jobs",
                "SikkimTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tamil_nadu_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                31,
                "tamil_nadu_teaching_jobs",
                "TamilNaduTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def telangana_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                32,
                "telangana_teaching_jobs",
                "TelanganaTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tripura_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                33,
                "tripura_teaching_jobs",
                "TripuraTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttarakhand_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                34,
                "uttarakhand_teaching_jobs",
                "UttarakhandTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttar_pradesh_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                35,
                "uttar_pradesh_teaching_jobs",
                "UttarPradeshTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def west_bengal_teaching_jobs(request):
        try:
            api = TeachingJobs.common_teaching_jobs(
                36,
                "west_bengal_teaching_jobs",
                "WestBengalTeachingJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

"""
@ Api for ENGG jobs...
"""


class EnggJobs:
    def common_engg_jobs(index,keyword,model_name):
        model = eval(model_name)
        #empty model
        model.objects.all().delete()
        pdf_dir = "media/pdf/scrap/engineering-jobs/" + re.sub("_","-",keyword) + "/"
        create_delete_pdf_dir(pdf_dir)
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/engineering-jobs/")
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
        data=all[index].find_all("tr",{"style":"border: 1px solid #000000;"})
        for i in data:
            d = i.find_all("td")
            dict["start_date"] = d[0].text
            dict["requirement_board"] = d[1].text
            dict["post_name"] = d[2].text
            dict["education"] = d[3].text
            dict["last_date"] = d[5].text
            l=d[6].text
            if l != "":
                link = d[6].find("strong").find("a")['href']
                if link.split(".")[1] == "freejobalert":
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 2
                    link_remove_slash = link.split("/")
                    link_to_string = (''.join(link_remove_slash))
                    job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                    if len(job_id) == 5:
                        dict["job_id"] = int(job_id)
                    elif len(job_id) == 7:
                        dict["job_id"] = int(job_id[2::])
                    else:
                        dict["job_id"] = None
                else:
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 1
                    dict["job_id"] = None
                join_id = randint(99999, 999999)
                #check the existing of join_id
                count_join_id = model.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                        pdf_url = link
                        pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                        download_pdf(pdf_url,pdf_file_name)
                        dict["more_info"] = pdf_file_name
                #insert into mysql database
                obj=model.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["education"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2[keyword] = lst
        lst2.append(dict2)
        return lst2

    def all_india_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                0,
                "all_india_engg_jobs",
                "AllIndiaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def all_india_fellow_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                1,
                "all_india_engg_jobs",
                "AllIndiaFellowEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andaman_nicobar_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                2,
                "andaman_nicobar_engg_jobs",
                "AndamanNicoborEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def andhra_pradesh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                3,
                "andhra_pradesh_engg_jobs",
                "AndhraPradeshEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def arunachal_pradesh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                4,
                "arunachal_pradesh_engg_jobs",
                "ArunachalPradeshEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def assam_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                5,
                "assam_engg_jobs",
                "AssamEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def bihar_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                6,
                "bihar_engg_jobs",
                "BiharEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chandigarh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                7,
                "chandigarh_engg_jobs",
                "ChandigarhEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def chhattisgarh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                8,
                "chhattisgarh_engg_jobs",
                "ChhattisgarhEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def dadra_nagar_haveli_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                9,
                "dadra_nagar_haveli_engg_jobs",
                "DadraNagarHaveliEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def daman_diu_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                10,
                "daman_diu_engg_jobs",
                "DamanDiuEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def delhi_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                11,
                "delhi_engg_jobs",
                "DelhiEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def goa_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                12,
                "goa_engg_jobs",
                "GoaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def gujurat_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                13,
                "gujurat_engg_jobs",
                "GujuratEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def haryana_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                14,
                "haryana_engg_jobs",
                "HaryanaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def himachal_pradesh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                15,
                "himachal_pradesh_engg_jobs",
                "HimachalPradeshEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jammu_kashmir_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                16,
                "jammu_kashmir_engg_jobs",
                "JammuKashmirEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def jharkhand_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                17,
                "jharkhand_engg_jobs",
                "JharkhandEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def karnataka_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                18,
                "karnataka_engg_jobs",
                "KarnatakaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def kerala_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                19,
                "kerala_engg_jobs",
                "KeralaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def lakshadweep_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                20,
                "lakshadweep_engg_jobs",
                "LakshadweepEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def madhya_pradesh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                21,
                "madhya_pradesh_engg_jobs",
                "MadhyaPradeshEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def maharashtra_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                22,
                "maharashtra_engg_jobs",
                "MaharashtraEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def manipur_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                23,
                "manipur_engg_jobs",
                "ManipurEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def meghalaya_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                24,
                "meghalaya_engg_jobs",
                "MeghalayaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def mizoram_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                25,
                "mizoram_engg_jobs",
                "MizoramEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def nagaland_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                26,
                "nagaland_engg_jobs",
                "NagalandEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def odisha_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                27,
                "odisha_engg_jobs",
                "OdishaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def puduchhery_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                28,
                "puduchhery_engg_jobs",
                "PuduchheryEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def punjab_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                29,
                "punjab_engg_jobs",
                "PunjabEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def rajasthan_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                30,
                "rajasthan_engg_jobs",
                "RajasthanEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def sikkim_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                31,
                "sikkim_engg_jobs",
                "SikkimEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tamil_nadu_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                32,
                "tamil_nadu_engg_jobs",
                "TamilNaduEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def telangana_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                33,
                "telangana_engg_jobs",
                "TelanganaEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def tripura_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                34,
                "tripura_engg_jobs",
                "TripuraEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttarakhand_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                35,
                "uttarakhand_engg_jobs",
                "UttarakhandEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def uttar_pradesh_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                36,
                "uttar_pradesh_engg_jobs",
                "UttarPradeshEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def west_bengal_engg_jobs(request):
        try:
            api = EnggJobs.common_engg_jobs(
                37,
                "west_bengal_engg_jobs",
                "WestBengalEnggJobs"
            )
            return JsonResponse(api,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

"""
@ Api for RAILWAY jobs...
"""

class RailwayJob:
    def railway_jobs(request):
        try:
            RailwayJobsModel.objects.all().delete()
            pdf_dir = "media/pdf/scrap/railway-jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/railway-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[0].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["requirement_board"] = d[1].text
                dict["post_name"] = d[2].text
                dict["qualification"] = d[3].text
                dict["last_date"] = d[5].text
                l=d[6].text
                if l != "":
                    link = d[6].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = RailwayJobsModel.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=RailwayJobsModel.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["qualification"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=randint(99999, 999999)
                    )
                lst.append(dict.copy())
            dict2["railway_jobs"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class PoliceDefenceJobs:
    def police_defence_jobs(request):
        try:
            PoliceAndDefenceJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/police-defence-jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/police-defence-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[0].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["requirement_board"] = d[1].text
                dict["post_name"] = d[2].text
                dict["qualification"] = d[3].text
                dict["last_date"] = d[5].text
                l=d[6].text
                if l != "":
                    link = d[6].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = PoliceAndDefenceJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=PoliceAndDefenceJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["qualification"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=randint(99999, 999999)
                    )
                lst.append(dict.copy())
            dict2["police_defence_jobs"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def statewise_police_jobs(request):
        try:
            StatewisePoliceJobs.objects.all().delete()
            pdf_dir = "media/pdf/scrap/statewise-police-defence-jobs/"
            create_delete_pdf_dir(pdf_dir)
            lst=[]
            lst2=[]
            dict={}
            dict2={}
            r=requests.get("http://www.freejobalert.com/police-defence-jobs/")
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
            data=all[0].find_all("tr",{"style":"border: 1px solid #000000;"})
            for i in data:
                d = i.find_all("td")
                dict["start_date"] = d[0].text
                dict["requirement_board"] = d[1].text
                dict["post_name"] = d[2].text
                dict["qualification"] = d[3].text
                dict["last_date"] = d[5].text
                l=d[6].text
                if l != "":
                    link = d[6].find("strong").find("a")['href']
                    if link.split(".")[1] == "freejobalert":
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 2
                        link_remove_slash = link.split("/")
                        link_to_string = (''.join(link_remove_slash))
                        job_id = (''.join(re.findall(r'\d{7}|\d{5}',link_to_string)))
                        if len(job_id) == 5:
                            dict["job_id"] = int(job_id)
                        elif len(job_id) == 7:
                            dict["job_id"] = int(job_id[2::])
                        else:
                            dict["job_id"] = None
                    else:
                        dict["more_info"] = d[6].find("strong").find("a")['href']
                        dict["type"] = 1
                        dict["job_id"] = None
                    join_id = randint(99999, 999999)
                    #check the existing of join_id
                    count_join_id = StatewisePoliceJobs.objects.filter(join_id=join_id).count()
                    if count_join_id is not 0:
                        join_id = join_id + 1
                    pdf_link = re.search(r'.pdf$',link)
                    if pdf_link:
                        pdf_link_lst=link.split(".")
                        if "freejobalert" in pdf_link_lst:
                            dict["type"] = 3
                            pdf_url = link
                            pdf_file_name = pdf_dir + str(randint(99999, 9999999999))+".pdf"
                            download_pdf(pdf_url,pdf_file_name)
                            dict["more_info"] = pdf_file_name
                    #insert into mysql database
                    obj=StatewisePoliceJobs.objects.create(
                        start_date=dict["start_date"],last_date=dict["last_date"],
                        post_name=dict["post_name"],education=dict["qualification"],
                        more_info=dict["more_info"],type=dict["type"],
                        job_id=dict["job_id"],join_id=randint(99999, 999999)
                    )
                lst.append(dict.copy())
            dict2["police_defence_jobs"] = lst
            lst2.append(dict2)
            return JsonResponse(lst2,safe=False)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

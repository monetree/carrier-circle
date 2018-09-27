
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import (
            UpscJobs,SscJobs,OtherAllIndiaJobs,
            OdishGovtJobs,AndamanNicoborGovtJobs,AndhraPradeshGovtJobs,
            ArunachalPradeshGovernmentjobs,AssamGovtJobs,
            BiharGovtJobs,ChandigarhGovtJobs,ChhattisgarhGovtJobs
                    )

"""
Scrapping imports
"""
import re
import requests
from bs4 import BeautifulSoup
from random import randint
"""
++++++++++++++++
"""

class AllIndiaGovtJobs:

    """
    @ Api for UPSC data...
    """

    def get_upsc(request):
        #empty model
        UpscJobs.objects.all().delete()
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

    """
    @ Api for SSC data...
    """
    def get_ssc(request):
        #empty model
        SscJobs.objects.all().delete()
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

        """
        @ Api for other All india jobs...
        """
    def get_other_all_india(request):
        #empty model
        OtherAllIndiaJobs.objects.all().delete()
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

    """
    @ Api for STATE GOVT. data...
    """
class StateGovtJobs:
    def get_all_state(url,keyword,model_name):
        #empty model
        model = eval(model_name)
        model.objects.all().delete()
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
                        print("Error on job id-- FIX IT ..")
                else:
                    dict["more_info"] = d[6].find("strong").find("a")['href']
                    dict["type"] = 1
                    dict["job_id"] = None
                lst.append(dict.copy())
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
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/odisha-government-jobs/","odisha_govt_jobs","OdishGovtJobs")
        request.session["job_id"] = 5
        return JsonResponse(api,safe=False)

    def andaman_nicobor_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/an-government-jobs/","andaman_nicobor_govt_jobs","AndamanNicoborGovtJobs")
        return JsonResponse(api,safe=False)

    def andhra_prtadesh_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/ap-government-jobs/","andhra_prtadesh_govt_jobs","AndhraPradeshGovtJobs")
        return JsonResponse(api,safe=False)

    def arunachal_pradesh_government_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/arunachal-pradesh-government-jobs/","arunachal_pradesh_government_jobs","ArunachalPradeshGovernmentjobs")
        return JsonResponse(api,safe=False)

    def assam_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/assam-government-jobs/","assam_govt_jobs","AssamGovtJobs")
        return JsonResponse(api,safe=False)

    def bihar_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/bihar-government-jobs/","bihar_govt_jobs","BiharGovtJobs")
        return JsonResponse(api,safe=False)

    def chandigarh_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/chandigarh-government-jobs/","chandigarh_govt_jobs","ChandigarhGovtJobs")
        return JsonResponse(api,safe=False)

    def chhattisgarh_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/chhattisgarh-government-jobs/","chhattisgarh_govt_jobs","ChhattisgarhGovtJobs")
        return JsonResponse(api,safe=False)

    def dadra_nagar_haveli_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/dadra-nagar-haveli-government-jobs/","dadra_nagar_haveli_govt_jobs","DadraNagarHaveliGovtJobs")
        return JsonResponse(api,safe=False)

    def daman_diu_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/daman-diu-government-jobs/","daman_diu_govt_jobs","DamanDiuGovtJobs")
        return JsonResponse(api,safe=False)

    def delhi_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/delhi-government-jobs/","delhi_govt_jobs","DelhiGovtJobs")
        return JsonResponse(api,safe=False)

    def goa_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/goa-government-jobs/","goa_govt_jobs","GoaGovtJobs")
        return JsonResponse(api,safe=False)

    def gujurat_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/gujarat-government-jobs/","gujurat_govt_jobs","GujuratGovtJobs")
        return JsonResponse(api,safe=False)

    def haryana_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/haryana-government-jobs/","haryana_govt_jobs","HaryanaGovtJobs")
        return JsonResponse(api,safe=False)

    def himachal_pradesh_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/hp-government-jobs/","himachal_pradesh_govt_jobs","HimachalPradeshGovtJobs")
        return JsonResponse(api,safe=False)

    def jammu_kashmir_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/jk-government-jobs/","jammu_kashmir_govt_jobs","JammuKashmirGovtJobs")
        return JsonResponse(api,safe=False)

    def jharkhand_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/jharkhand-government-jobs/","jharkhand_govt_jobs","JharkhandGovtJobs")
        return JsonResponse(api,safe=False)

    def karnataka_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/karnataka-government-jobs/","karnataka_govt_jobs")
        return JsonResponse(api,safe=False)

    def kerala_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/kerala-government-jobs/","kerala_govt_jobs")
        return JsonResponse(api,safe=False)

    def lakshadweep_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/lakshadweep-government-jobs/","lakshadweep_govt_jobs")
        return JsonResponse(api,safe=False)

    def madhya_pradesh_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/mp-government-jobs/","madhya_pradesh_govt_jobs")
        return JsonResponse(api,safe=False)

    def maharashtra_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/maharashtra-government-jobs/","maharashtra_govt_jobs")
        return JsonResponse(api,safe=False)

    def manipur_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/manipur-government-jobs/","manipur_govt_jobs")
        return JsonResponse(api,safe=False)

    def meghalaya_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/meghalaya-government-jobs/","meghalaya_govt_jobs")
        return JsonResponse(api,safe=False)

    def mizoram_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/mizoram-government-jobs/","mizoram_govt_jobs")
        return JsonResponse(api,safe=False)

    def nagaland_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/nagaland-government-jobs/","nagaland_govt_jobs")
        return JsonResponse(api,safe=False)

    def puduchhery_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/puduchhery-government-jobs/","puduchhery_govt_jobs")
        return JsonResponse(api,safe=False)

    def punjab_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/punjab-government-jobs/","punjab_govt_jobs")
        return JsonResponse(api,safe=False)

    def rajasthan_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/rajasthan-government-jobs/","rajasthan_govt_jobs")
        return JsonResponse(api,safe=False)

    def sikkim_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/sikkim-government-jobs/","sikkim_govt_jobs")
        return JsonResponse(api,safe=False)

    def tamil_nadu_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/tn-government-jobs/","tamil_nadu_govt_jobs")
        return JsonResponse(api,safe=False)

    def telangana_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/telangana-government-jobs/","telangana_govt_jobs")
        return JsonResponse(api,safe=False)

    def tripura_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/tripura-government-jobs/","tripura_govt_jobs")
        return JsonResponse(api,safe=False)

    def uttarakhand_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/uttarakhand-government-jobs/","uttarakhand_govt_jobs")
        return JsonResponse(api,safe=False)

    def uttar_pradesh_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/up-government-jobs/","uttar_pradesh_govt_jobs")
        return JsonResponse(api,safe=False)

    def west_bengal_govt_jobs(request):
        api = StateGovtJobs.get_all_state("http://www.freejobalert.com/wb-government-jobs/","west_bengal_govt_jobs")
        return JsonResponse(api,safe=False)

    """
    @ Api for BANK GOVT. data...
    """

class BankJobs:
    def all_bank_jobs(request):
        #empty model
        AllBankJobs.objects.all().delete()
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
            dict["requirement_board"] = d[1].text
            dict["post_name"] = d[2].text
            dict["qualification"] = d[3].text
            dict["last_date"] = d[5].text
            l=d[6].text
            link = d[6].find("strong").find("a")['href']
            if l != "":
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
                    dict["more_info"] = d[5].find("strong").find("a")['href']
                    dict["type"] = 1
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


    def other_financial_jobs(request):
        #empty model
        OtherFinancialJobs.objects.all().delete()
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
            dict["qualification"] = d[3].text
            dict["last_date"] = d[5].text
            l=d[6].text
            link = d[6].find("strong").find("a")['href']
            if l != "":
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
                    dict["more_info"] = d[5].find("strong").find("a")['href']
                    dict["type"] = 1
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

    """
    @ Api for TEACHING jobs...
    """
class TeachingJobs:
    def common_teaching_jobs(index,keyword,model_name):
        model = eval(model_name)
        #empty model
        model.objects.all().delete()
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
            dict["qualification"] = d[3].text
            dict["last_date"] = d[5].text
            l=d[6].text
            link = d[6].find("strong").find("a")['href']
            if l != "":
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
                    dict["more_info"] = d[5].find("strong").find("a")['href']
                    dict["type"] = 1
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
        api = TeachingJobs.common_teaching_jobs(0, "all_india_teaching_jobs","AllIndiaTeachingJobs")
        return JsonResponse(api,safe=False)

    def andaman_nicobar_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(1, "andaman_nicobar_teaching_jobs","AndamanNicoborTeachingJobs")
        return JsonResponse(api,safe=False)

    def andhra_pradesh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(2, "andhra_pradesh_teaching_jobs","AndhraPradeshTeachingJobs")
        return JsonResponse(api,safe=False)

    def arunachal_pradesh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(3, "arunachal_pradesh_teaching_jobs","ArunachalPradeshTeachingjobs")
        return JsonResponse(api,safe=False)

    def assam_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(4, "assam_teaching_jobs","AssamTeachingJobs")
        return JsonResponse(api,safe=False)

    def bihar_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(5, "bihar_teaching_jobs","BiharTeachingJobs")
        return JsonResponse(api,safe=False)

    def chandigarh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(6, "chandigarh_teaching_jobs","ChandigarhTeachingJobs")
        return JsonResponse(api,safe=False)

    def chhattisgarh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(7, "chhattisgarh_teaching_jobs","ChhattisgarhTeachingJobs")
        return JsonResponse(api,safe=False)

    def dadra_nagar_haveli_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(8, "dadra_nagar_haveli_teaching_jobs","DadraNagarHaveliTeachingJobs")
        return JsonResponse(api,safe=False)

    def daman_diu_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(9, "daman_diu_teaching_jobs","DamanDiuTeachingJobs")
        return JsonResponse(api,safe=False)

    def delhi_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(10, "delhi_teaching_jobs","DelhiTeachingJobs")
        return JsonResponse(api,safe=False)

    def goa_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(11, "goa_teaching_jobs","GoaTeachingJobs")
        return JsonResponse(api,safe=False)

    def gujurat_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(12, "gujurat_teaching_jobs","GujuratTeachingJobs")
        return JsonResponse(api,safe=False)

    def haryana_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(13, "haryana_teaching_jobs","HaryanaTeachingJobs")
        return JsonResponse(api,safe=False)

    def himachal_pradesh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(14, "himachal_pradesh_teaching_jobs","HimachalPradeshTeachingJobs")
        return JsonResponse(api,safe=False)

    def jammu_kashmir_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(15, "jammu_kashmir_teaching_jobs","JammuKashmirTeachingJobs")
        return JsonResponse(api,safe=False)

    def jharkhand_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(16, "jharkhand_teaching_jobs","JharkhandTeachingJobs")
        return JsonResponse(api,safe=False)

    def karnataka_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(17, "karnataka_teaching_jobs","KarntakaTeachingJobs")
        return JsonResponse(api,safe=False)

    def kerala_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(18, "kerala_teaching_jobs","KeralaTeachingJobs")
        return JsonResponse(api,safe=False)

    def lakshadweep_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(19, "lakshadweep_teaching_jobs","LakshadweepTeachingJobs")
        return JsonResponse(api,safe=False)

    def madhya_pradesh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(20, "madhya_pradesh_teaching_jobs","MadhyaPradeshTeachingJobs")
        return JsonResponse(api,safe=False)

    def maharashtra_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(21, "maharashtra_teaching_jobs","MaharashtraTeachingJobs")
        return JsonResponse(api,safe=False)

    def manipur_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(22, "manipur_teaching_jobs","ManipurTeachingJobs")
        return JsonResponse(api,safe=False)

    def meghalaya_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(23, "meghalaya_teaching_jobs","MeghalayaTeachingJobs")
        return JsonResponse(api,safe=False)

    def mizoram_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(24, "mizoram_teaching_jobs","MizoramTeachingJobs")
        return JsonResponse(api,safe=False)

    def nagaland_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(25, "nagaland_teaching_jobs","NagalandTeachingJobs")
        return JsonResponse(api,safe=False)

    def odisha_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(26, "odisha_teaching_jobs","OdishaTeachingJobs")
        return JsonResponse(api,safe=False)

    def puduchhery_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(27, "puduchhery_teaching_jobs","PuduchheryTeachingJobs")
        return JsonResponse(api,safe=False)

    def punjab_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(28, "punjab_teaching_jobs","PunjabTeachingJobs")
        return JsonResponse(api,safe=False)

    def rajasthan_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(29, "rajasthan_teaching_jobs","RajasthanTeachingJobs")
        return JsonResponse(api,safe=False)

    def sikkim_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(30, "sikkim_teaching_jobs","SikkimTeachingJobs")
        return JsonResponse(api,safe=False)

    def tamil_nadu_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(31, "tamil_nadu_teaching_jobs","TamilNaduTeachingJobs")
        return JsonResponse(api,safe=False)

    def telangana_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(32, "telangana_teaching_jobs","TelanganaTeachingJobs")
        return JsonResponse(api,safe=False)

    def tripura_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(33, "tripura_teaching_jobs","TripuraTeachingJobs")
        return JsonResponse(api,safe=False)

    def uttarakhand_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(34, "uttarakhand_teaching_jobs","UttarakhandTeachingJobs")
        return JsonResponse(api,safe=False)

    def uttar_pradesh_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(35, "uttar_pradesh_teaching_jobs","UttarPradeshTeachingJobs")
        return JsonResponse(api,safe=False)

    def west_bengal_teaching_jobs(request):
        api = TeachingJobs.common_teaching_jobs(36, "west_bengal_teaching_jobs","WestBengalTeachingJobs")
        return JsonResponse(api,safe=False)

    """
    @ Api for ENGG jobs...
    """

class EngineeringJobs:
    def common_engg_jobs(index,keyword):
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
            dict["qualification"] = d[3].text
            dict["last_date"] = d[5].text
            lst.append(dict.copy())
        dict2[keyword] = lst
        lst2.append(dict2)
        return lst2


    def all_india_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(0, "all_india_engg_jobs")
        return JsonResponse(api,safe=False)

    def all_india_fellow_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(1, "all_india_fellow_engg_jobs")
        return JsonResponse(api,safe=False)

    def andaman_nicobar_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(2, "andaman_nicobar_engg_jobs")
        return JsonResponse(api,safe=False)

    def andhra_pradesh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(3, "andhra_pradesh_engg_jobs")
        return JsonResponse(api,safe=False)

    def arunachal_pradesh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(4, "arunachal_pradesh_engg_jobs")
        return JsonResponse(api,safe=False)

    def assam_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(5, "assam_engg_jobs")
        return JsonResponse(api,safe=False)

    def bihar_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(6, "bihar_engg_jobs")
        return JsonResponse(api,safe=False)

    def chandigarh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(7, "chandigarh_engg_jobs")
        return JsonResponse(api,safe=False)

    def chhattisgarh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(8, "chhattisgarh_engg_jobs")
        return JsonResponse(api,safe=False)

    def dadra_nagar_haveli_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(9, "dadra_nagar_haveli_engg_jobs")
        return JsonResponse(api,safe=False)

    def daman_diu_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(10, "daman_diu_engg_jobs")
        return JsonResponse(api,safe=False)

    def delhi_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(11, "delhi_engg_jobs")
        return JsonResponse(api,safe=False)

    def goa_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(12, "goa_engg_jobs")
        return JsonResponse(api,safe=False)

    def gujurat_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(13, "gujurat_engg_jobs")
        return JsonResponse(api,safe=False)

    def haryana_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(14, "haryana_engg_jobs")
        return JsonResponse(api,safe=False)

    def himachal_pradesh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(15, "himachal_pradesh_engg_jobs")
        return JsonResponse(api,safe=False)

    def jammu_kashmir_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(16, "jammu_kashmir_engg_jobs")
        return JsonResponse(api,safe=False)

    def jharkhand_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(17, "jharkhand_engg_jobs")
        return JsonResponse(api,safe=False)

    def karnataka_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(18, "karnataka_engg_jobs")
        return JsonResponse(api,safe=False)

    def kerala_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(19, "kerala_engg_jobs")
        return JsonResponse(api,safe=False)

    def lakshadweep_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(20, "lakshadweep_engg_jobs")
        return JsonResponse(api,safe=False)

    def madhya_pradesh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(21, "madhya_pradesh_engg_jobs")
        return JsonResponse(api,safe=False)

    def maharashtra_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(22, "maharashtra_engg_jobs")
        return JsonResponse(api,safe=False)

    def manipur_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(23, "manipur_engg_jobs")
        return JsonResponse(api,safe=False)

    def meghalaya_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(24, "meghalaya_engg_jobs")
        return JsonResponse(api,safe=False)

    def mizoram_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(25, "mizoram_engg_jobs")
        return JsonResponse(api,safe=False)

    def nagaland_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(26, "nagaland_engg_jobs")
        return JsonResponse(api,safe=False)

    def odisha_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(27, "odisha_engg_jobs")
        return JsonResponse(api,safe=False)

    def puduchhery_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(28, "puduchhery_engg_jobs")
        return JsonResponse(api,safe=False)

    def punjab_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(29, "punjab_engg_jobs")
        return JsonResponse(api,safe=False)

    def rajasthan_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(30, "rajasthan_engg_jobs")
        return JsonResponse(api,safe=False)

    def sikkim_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(31, "sikkim_engg_jobs")
        return JsonResponse(api,safe=False)

    def tamil_nadu_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(32, "tamil_nadu_engg_jobs")
        return JsonResponse(api,safe=False)

    def telangana_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(33, "telangana_engg_jobs")
        return JsonResponse(api,safe=False)

    def tripura_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(34, "tripura_engg_jobs")
        return JsonResponse(api,safe=False)

    def uttarakhand_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(35, "uttarakhand_engg_jobs")
        return JsonResponse(api,safe=False)

    def uttar_pradesh_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(36, "uttar_pradesh_engg_jobs")
        return JsonResponse(api,safe=False)

    def west_bengal_engg_jobs(request):
        api = EngineeringJobs.common_engg_jobs(37, "west_bengal_engg_jobs")
        return JsonResponse(api,safe=False)


class RailwayJobs:
    def railway_jobs(request):
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
            link = d[6].find("strong").find("a")['href']
            if link.split(".")[1] == "freejobalert":
                dict["more_info"] = "pending"
            else:
                dict["more_info"] = d[6].find("strong").find("a")['href']
            lst.append(dict.copy())
        dict2["railway_jobs"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

class PoliceDefenceJobs:
    def police_defence_jobs(request):
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
            link = d[6].find("strong").find("a")['href']
            if link.split(".")[1] == "freejobalert":
                dict["details"] = "pending"
                dict["type"] = 2
            else:
                dict["details"] = d[6].find("strong").find("a")['href']
                dict["type"] = 1
            lst.append(dict.copy())
        dict2["police_defence_jobs"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

    def statewise_police_jobs(request):
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/police-defence-jobs/")
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all=soup.find_all("table",{"style":"color:#000000; border: 2px solid #006699;border-collapse: collapse; max-width:790px;"})
        data=all[1].find_all("tr",{"style":"border: 1px solid #000000;"})
        for i in data:
            d = i.find_all("td")
            dict["start_date"] = d[0].text
            dict["requirement_board"] = d[1].text
            dict["post_name"] = d[2].text
            dict["qualification"] = d[3].text
            dict["last_date"] = d[5].text
            link = d[6].find("strong").find("a")['href']
            if link.split(".")[1] == "freejobalert":
                dict["more_info"] = "pending"
            else:
                dict["more_info"] = d[6].find("strong").find("a")['href']
            lst.append(dict.copy())
        dict2["statewise_police_jobs"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

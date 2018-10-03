
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

"""
++++++++++++++++
"""

class AllIndiaGovtJobDetails:

    """
    @ Api for UPSC data...
    """

    def cleanhtml(raw_html):
      cleantext = re.sub(r'<.*?>', '', raw_html)
      return cleantext

    def upsc_details(request):
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
        # important_dates = trs[2].find_all("ul")
        # if len(important_dates) != 0:
        #     li = important_dates[0].find_all("li")
        #     for l in li:
        #         dict["dates"] = l.text
        #         lst.append(dict.copy())
        #     dict2["important_dates"] = lst
        #     lst2.append(dict2)




        return JsonResponse(lst2,safe=False)


            # from lxml import html
            # from lxml import etree
            # import requests
            # page = requests.get('http://www.freejobalert.com/upsc-recruitment/16960/#Engg-Services2019')
            # tree = html.fromstring(page.content)
            # tables = tree.xpath('//table[@style="width: 500px;"]')
            # for t in tables:
            #     ts = etree.tostring(t)
            #     lst.append(ts)



    """
    @ Api for SSC data...
    """
    def ssc_details(request):
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

        """
        @ Api for other All india JobDetails...
        """
    def other_all_india_details(request):
        #empty model
        OtherAllIndiaJobDetails.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/government-JobDetails/")
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
                count_join_id = OtherAllIndiaJobDetails.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                # insert into mysql database
                obj=OtherAllIndiaJobDetails.objects.create(
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
class StateGovtJobDetails:
    def get_all_state(url,keyword,model_name):
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        model = eval(model_name)
        obj = list(AndhraPradeshGovtJobs.objects.values())
        for o in obj:
            if o["type"] == 2:
                url = o["more_info"]
                r=requests.get(url)
                c=r.content
                soup=BeautifulSoup(c,"html.parser")
                table=soup.find_all("table",{"style":"width: 500px;"})[0]
                tr = table.find_all("tr")[-2::]
                print(tr)



        return lst2

    def odisha_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/odisha-government-JobDetails/","odisha_govt_job_details","OdishaGovtJobDetails")
        request.session["job_id"] = 5
        return JsonResponse(api,safe=False)

    def andaman_nicobor_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/an-government-JobDetails/","andaman_nicobor_govt_job_details","AndamanNicoborGovtJobDetails")
        return JsonResponse(api,safe=False)

    def andhra_prtadesh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/ap-government-JobDetails/","andhra_prtadesh_govt_job_details","AndhraPradeshGovtJobDetails")
        return JsonResponse(api,safe=False)

    def arunachal_pradesh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/arunachal-pradesh-government-JobDetails/","arunachal_pradesh_govt_job_details","ArunachalPradeshGovernmentJobDetails")
        return JsonResponse(api,safe=False)

    def assam_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/assam-government-JobDetails/","assam_govt_job_details","AssamGovtJobDetails")
        return JsonResponse(api,safe=False)

    def bihar_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/bihar-government-JobDetails/","bihar_govt_job_details","BiharGovtJobDetails")
        return JsonResponse(api,safe=False)

    def chandigarh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/chandigarh-government-JobDetails/","chandigarh_govt_job_details","ChandigarhGovtJobDetails")
        return JsonResponse(api,safe=False)

    def chhattisgarh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/chhattisgarh-government-JobDetails/","chhattisgarh_govt_job_details","ChhattisgarhGovtJobDetails")
        return JsonResponse(api,safe=False)

    def dadra_nagar_haveli_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/dadra-nagar-haveli-government-JobDetails/","dadra_nagar_haveli_govt_job_details","DadraNagarHaveliGovtJobDetails")
        return JsonResponse(api,safe=False)

    def daman_diu_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/daman-diu-government-JobDetails/","daman_diu_govt_job_details","DamanDiuGovtJobDetails")
        return JsonResponse(api,safe=False)

    def delhi_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/delhi-government-JobDetails/","delhi_govt_job_details","DelhiGovtJobDetails")
        return JsonResponse(api,safe=False)

    def goa_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/goa-government-JobDetails/","goa_govt_job_details","GoaGovtJobDetails")
        return JsonResponse(api,safe=False)

    def gujurat_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/gujarat-government-JobDetails/","gujurat_govt_job_details","GujuratGovtJobDetails")
        return JsonResponse(api,safe=False)

    def haryana_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/haryana-government-JobDetails/","haryana_govt_job_details","HaryanaGovtJobDetails")
        return JsonResponse(api,safe=False)

    def himachal_pradesh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/hp-government-JobDetails/","himachal_pradesh_govt_job_details","HimachalPradeshGovtJobDetails")
        return JsonResponse(api,safe=False)

    def jammu_kashmir_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/jk-government-JobDetails/","jammu_kashmir_govt_job_details","JammuKashmirGovtJobDetails")
        return JsonResponse(api,safe=False)

    def jharkhand_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/jharkhand-government-JobDetails/","jharkhand_govt_job_details","JharkhandGovtJobDetails")
        return JsonResponse(api,safe=False)

    def karnataka_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/karnataka-government-JobDetails/","karnataka_govt_job_details")
        return JsonResponse(api,safe=False)

    def kerala_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/kerala-government-JobDetails/","kerala_govt_job_details")
        return JsonResponse(api,safe=False)

    def lakshadweep_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/lakshadweep-government-JobDetails/","lakshadweep_govt_job_details")
        return JsonResponse(api,safe=False)

    def madhya_pradesh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/mp-government-JobDetails/","madhya_pradesh_govt_job_details")
        return JsonResponse(api,safe=False)

    def maharashtra_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/maharashtra-government-JobDetails/","maharashtra_govt_job_details")
        return JsonResponse(api,safe=False)

    def manipur_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/manipur-government-JobDetails/","manipur_govt_job_details")
        return JsonResponse(api,safe=False)

    def meghalaya_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/meghalaya-government-JobDetails/","meghalaya_govt_job_details")
        return JsonResponse(api,safe=False)

    def mizoram_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/mizoram-government-JobDetails/","mizoram_govt_job_details")
        return JsonResponse(api,safe=False)

    def nagaland_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/nagaland-government-JobDetails/","nagaland_govt_job_details")
        return JsonResponse(api,safe=False)

    def puduchhery_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/puduchhery-government-JobDetails/","puduchhery_govt_job_details")
        return JsonResponse(api,safe=False)

    def punjab_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/punjab-government-JobDetails/","punjab_govt_job_details")
        return JsonResponse(api,safe=False)

    def rajasthan_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/rajasthan-government-JobDetails/","rajasthan_govt_job_details")
        return JsonResponse(api,safe=False)

    def sikkim_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/sikkim-government-JobDetails/","sikkim_govt_job_details")
        return JsonResponse(api,safe=False)

    def tamil_nadu_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/tn-government-JobDetails/","tamil_nadu_govt_job_details")
        return JsonResponse(api,safe=False)

    def telangana_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/telangana-government-JobDetails/","telangana_govt_job_details")
        return JsonResponse(api,safe=False)

    def tripura_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/tripura-government-JobDetails/","tripura_govt_job_details")
        return JsonResponse(api,safe=False)

    def uttarakhand_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/uttarakhand-government-JobDetails/","uttarakhand_govt_job_details")
        return JsonResponse(api,safe=False)

    def uttar_pradesh_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/up-government-JobDetails/","uttar_pradesh_govt_job_details")
        return JsonResponse(api,safe=False)

    def west_bengal_govt_job_details(request):
        api = StateGovtJobDetails.get_all_state("http://www.freejobalert.com/wb-government-JobDetails/","west_bengal_govt_job_details")
        return JsonResponse(api,safe=False)

    """
    @ Api for BANK GOVT. data...
    """

class BankJobDetails:
    def all_bank_job_details(request):
        #empty model
        AllBankJobDetails.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/bank-JobDetails/")
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
                count_join_id = AllBankJobDetails.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                #insert into mysql database
                obj=AllBankJobDetails.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["education"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2["all_bank_JobDetails"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)


    def other_financial_job_details(request):
        #empty model
        OtherFinancialJobDetails.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/bank-JobDetails/")
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
                count_join_id = OtherFinancialJobDetails.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                #insert into mysql database
                obj=OtherFinancialJobDetails.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["education"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2["other_financial_JobDetails"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

    """
    @ Api for TEACHING JobDetails...
    """
class TeachingJobDetails:
    def common_teaching_job_details(index,keyword,model_name):
        model = eval(model_name)
        #empty model
        model.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/teaching-faculty-JobDetails/")
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

    def all_india_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(0, "all_india_teaching_job_details","AllIndiaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def andaman_nicobar_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(1, "andaman_nicobar_teaching_job_details","AndamanNicoborTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def andhra_pradesh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(2, "andhra_pradesh_teaching_job_details","AndhraPradeshTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def arunachal_pradesh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(3, "arunachal_pradesh_teaching_job_details","ArunachalPradeshTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def assam_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(4, "assam_teaching_job_details","AssamTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def bihar_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(5, "bihar_teaching_job_details","BiharTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def chandigarh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(6, "chandigarh_teaching_job_details","ChandigarhTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def chhattisgarh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(7, "chhattisgarh_teaching_job_details","ChhattisgarhTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def dadra_nagar_haveli_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(8, "dadra_nagar_haveli_teaching_job_details","DadraNagarHaveliTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def daman_diu_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(9, "daman_diu_teaching_job_details","DamanDiuTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def delhi_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(10, "delhi_teaching_job_details","DelhiTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def goa_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(11, "goa_teaching_job_details","GoaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def gujurat_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(12, "gujurat_teaching_job_details","GujuratTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def haryana_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(13, "haryana_teaching_job_details","HaryanaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def himachal_pradesh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(14, "himachal_pradesh_teaching_job_details","HimachalPradeshTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def jammu_kashmir_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(15, "jammu_kashmir_teaching_job_details","JammuKashmirTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def jharkhand_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(16, "jharkhand_teaching_job_details","JharkhandTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def karnataka_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(17, "karnataka_teaching_job_details","KarnatakaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def kerala_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(18, "kerala_teaching_job_details","KeralaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def lakshadweep_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(19, "lakshadweep_teaching_job_details","LakshadweepTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def madhya_pradesh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(20, "madhya_pradesh_teaching_job_details","MadhyaPradeshTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def maharashtra_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(21, "maharashtra_teaching_job_details","MaharashtraTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def manipur_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(22, "manipur_teaching_job_details","ManipurTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def meghalaya_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(23, "meghalaya_teaching_job_details","MeghalayaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def mizoram_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(24, "mizoram_teaching_job_details","MizoramTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def nagaland_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(25, "nagaland_teaching_job_details","NagalandTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def odisha_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(26, "odisha_teaching_job_details","OdishaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def puduchhery_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(27, "puduchhery_teaching_job_details","PuduchheryTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def punjab_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(28, "punjab_teaching_job_details","PunjabTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def rajasthan_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(29, "rajasthan_teaching_job_details","RajasthanTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def sikkim_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(30, "sikkim_teaching_job_details","SikkimTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def tamil_nadu_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(31, "tamil_nadu_teaching_job_details","TamilNaduTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def telangana_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(32, "telangana_teaching_job_details","TelanganaTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def tripura_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(33, "tripura_teaching_job_details","TripuraTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def uttarakhand_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(34, "uttarakhand_teaching_job_details","UttarakhandTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def uttar_pradesh_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(35, "uttar_pradesh_teaching_job_details","UttarPradeshTeachingJobDetails")
        return JsonResponse(api,safe=False)

    def west_bengal_teaching_job_details(request):
        api = TeachingJobDetails.common_teaching_job_details(36, "west_bengal_teaching_job_details","WestBengalTeachingJobDetails")
        return JsonResponse(api,safe=False)

"""
@ Api for ENGG JobDetails...
"""


class EnggJobDetails:
    def common_engg_job_details(index,keyword,model_name):
        model = eval(model_name)
        #empty model
        model.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/engineering-JobDetails/")
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

    def all_india_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(0, "all_india_engg_job_details","AllIndiaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def all_india_fellow_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(1, "all_india_engg_job_details","AllIndiaFellowEnggJobDetails")
        return JsonResponse(api,safe=False)

    def andaman_nicobar_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(2, "andaman_nicobar_engg_job_details","AndamanNicoborEnggJobDetails")
        return JsonResponse(api,safe=False)

    def andhra_pradesh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(3, "andhra_pradesh_engg_job_details","AndhraPradeshEnggJobDetails")
        return JsonResponse(api,safe=False)

    def arunachal_pradesh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(4, "arunachal_pradesh_engg_job_details","ArunachalPradeshEnggJobDetails")
        return JsonResponse(api,safe=False)

    def assam_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(5, "assam_engg_job_details","AssamEnggJobDetails")
        return JsonResponse(api,safe=False)

    def bihar_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(6, "bihar_engg_job_details","BiharEnggJobDetails")
        return JsonResponse(api,safe=False)

    def chandigarh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(7, "chandigarh_engg_job_details","ChandigarhEnggJobDetails")
        return JsonResponse(api,safe=False)

    def chhattisgarh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(8, "chhattisgarh_engg_job_details","ChhattisgarhEnggJobDetails")
        return JsonResponse(api,safe=False)

    def dadra_nagar_haveli_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(9, "dadra_nagar_haveli_engg_job_details","DadraNagarHaveliEnggJobDetails")
        return JsonResponse(api,safe=False)

    def daman_diu_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(10, "daman_diu_engg_job_details","DamanDiuEnggJobDetails")
        return JsonResponse(api,safe=False)

    def delhi_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(11, "delhi_engg_job_details","DelhiEnggJobDetails")
        return JsonResponse(api,safe=False)

    def goa_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(12, "goa_engg_job_details","GoaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def gujurat_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(13, "gujurat_engg_job_details","GujuratEnggJobDetails")
        return JsonResponse(api,safe=False)

    def haryana_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(14, "haryana_engg_job_details","HaryanaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def himachal_pradesh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(15, "himachal_pradesh_engg_job_details","HimachalPradeshEnggJobDetails")
        return JsonResponse(api,safe=False)

    def jammu_kashmir_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(16, "jammu_kashmir_engg_job_details","JammuKashmirEnggJobDetails")
        return JsonResponse(api,safe=False)

    def jharkhand_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(17, "jharkhand_engg_job_details","JharkhandEnggJobDetails")
        return JsonResponse(api,safe=False)

    def karnataka_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(18, "karnataka_engg_job_details","KarnatakaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def kerala_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(19, "kerala_engg_job_details","KeralaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def lakshadweep_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(20, "lakshadweep_engg_job_details","LakshadweepEnggJobDetails")
        return JsonResponse(api,safe=False)

    def madhya_pradesh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(21, "madhya_pradesh_engg_job_details","MadhyaPradeshEnggJobDetails")
        return JsonResponse(api,safe=False)

    def maharashtra_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(22, "maharashtra_engg_job_details","MaharashtraEnggJobDetails")
        return JsonResponse(api,safe=False)

    def manipur_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(23, "manipur_engg_job_details","ManipurEnggJobDetails")
        return JsonResponse(api,safe=False)

    def meghalaya_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(24, "meghalaya_engg_job_details","MeghalayaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def mizoram_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(25, "mizoram_engg_job_details","MizoramEnggJobDetails")
        return JsonResponse(api,safe=False)

    def nagaland_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(26, "nagaland_engg_job_details","NagalandEnggJobDetails")
        return JsonResponse(api,safe=False)

    def odisha_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(27, "odisha_engg_job_details","OdishaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def puduchhery_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(28, "puduchhery_engg_job_details","PuduchheryEnggJobDetails")
        return JsonResponse(api,safe=False)

    def punjab_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(29, "punjab_engg_job_details","PunjabEnggJobDetails")
        return JsonResponse(api,safe=False)

    def rajasthan_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(30, "rajasthan_engg_job_details","RajasthanEnggJobDetails")
        return JsonResponse(api,safe=False)

    def sikkim_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(31, "sikkim_engg_job_details","SikkimEnggJobDetails")
        return JsonResponse(api,safe=False)

    def tamil_nadu_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(32, "tamil_nadu_engg_job_details","TamilNaduEnggJobDetails")
        return JsonResponse(api,safe=False)

    def telangana_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(33, "telangana_engg_job_details","TelanganaEnggJobDetails")
        return JsonResponse(api,safe=False)

    def tripura_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(34, "tripura_engg_job_details","TripuraEnggJobDetails")
        return JsonResponse(api,safe=False)

    def uttarakhand_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(35, "uttarakhand_engg_job_details","UttarakhandEnggJobDetails")
        return JsonResponse(api,safe=False)

    def uttar_pradesh_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(36, "uttar_pradesh_engg_job_details","UttarPradeshEnggJobDetails")
        return JsonResponse(api,safe=False)

    def west_bengal_engg_job_details(request):
        api = EnggJobDetails.common_engg_job_details(37, "west_bengal_engg_job_details","WestBengalEnggJobDetails")
        return JsonResponse(api,safe=False)


"""
@ Api for RAILWAY JobDetails...
"""

class RailwayJobDetails:
    def railway_job_details(request):
        RailwayJob.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/railway-JobDetails/")
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
                count_join_id = RailwayJob.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                #insert into mysql database
                obj=RailwayJob.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["qualification"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2["railway_JobDetails"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

class PoliceDefenceJobDetails:
    def police_defence_job_details(request):
        PoliceAndDefenceJobDetails.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/police-defence-JobDetails/")
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
                count_join_id = PoliceAndDefenceJobDetails.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                #insert into mysql database
                obj=PoliceAndDefenceJobDetails.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["qualification"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2["police_defence_JobDetails"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

    def statewise_police_job_details(request):
        StatewisePoliceJobDetails.objects.all().delete()
        lst=[]
        lst2=[]
        dict={}
        dict2={}
        r=requests.get("http://www.freejobalert.com/police-defence-JobDetails/")
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
                count_join_id = StatewisePoliceJobDetails.objects.filter(join_id=join_id).count()
                if count_join_id is not 0:
                    join_id = join_id + 1
                pdf_link = re.search(r'.pdf$',link)
                if pdf_link:
                    pdf_link_lst=link.split(".")
                    if "freejobalert" in pdf_link_lst:
                        dict["type"] = 3
                #insert into mysql database
                obj=StatewisePoliceJobDetails.objects.create(
                    start_date=dict["start_date"],last_date=dict["last_date"],
                    post_name=dict["post_name"],education=dict["education"],
                    more_info=dict["more_info"],type=dict["type"],
                    job_id=dict["job_id"],join_id=randint(99999, 999999)
                )
            lst.append(dict.copy())
        dict2["statewise_police_JobDetails"] = lst
        lst2.append(dict2)
        return JsonResponse(lst2,safe=False)

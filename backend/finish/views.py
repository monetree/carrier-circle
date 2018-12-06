from threading import Thread
import json
from django.http import JsonResponse
from time import sleep
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from scrap.models import *
from details.models import *

from finalize.views import (
            AllIndiaGovernmentJobs,
            StatewiseGovtJobs,
            StatewiseTeachingJobs,
            StatewiseEngineeringJobs,
            RailwayJobs,
            BankingJobs,
            PoliceJobs
        )


class FinishAll:
    def all_india_govt_jobs(request):
        res = AllIndiaGovernmentJobs.call_all_india_govt_jobs(request)
        return HttpResponse("success")

    def state_govt_jobs(request):
        t1 = Thread(target=StatewiseGovtJobs.call_andaman_govt_jobs,args=[request])
        t2 = Thread(target=StatewiseGovtJobs.call_odisha_govt_jobs,args=[request])
        t3 = Thread(target=StatewiseGovtJobs.call_andhra_govt_jobs,args=[request])
        t4 = Thread(target=StatewiseGovtJobs.call_arunachal_pradesh_govt_jobs,args=[request])
        t5 = Thread(target=StatewiseGovtJobs.call_assam_govt_jobs,args=[request])
        t6 = Thread(target=StatewiseGovtJobs.call_bihar_govt_jobs,args=[request])
        t7 = Thread(target=StatewiseGovtJobs.call_chandigarh_govt_jobs,args=[request])
        t8 = Thread(target=StatewiseGovtJobs.call_chhattisgarh_govt_jobs,args=[request])
        t9 = Thread(target=StatewiseGovtJobs.call_dadra_nagar_govt_jobs,args=[request])
        t10 = Thread(target=StatewiseGovtJobs.call_daman_diu_govt_jobs,args=[request])
        t11 = Thread(target=StatewiseGovtJobs.call_delhi_govt_jobs,args=[request])
        t12 = Thread(target=StatewiseGovtJobs.call_goa_govt_jobs,args=[request])
        t13 = Thread(target=StatewiseGovtJobs.call_gujurat_govt_jobs,args=[request])
        t14 = Thread(target=StatewiseGovtJobs.call_haryana_govt_jobs,args=[request])
        t15 = Thread(target=StatewiseGovtJobs.call_himachal_pradesh_govt_jobs,args=[request])
        t16 = Thread(target=StatewiseGovtJobs.call_jammu_kashmir_govt_jobs,args=[request])
        t17 = Thread(target=StatewiseGovtJobs.call_jharkhand_govt_jobs,args=[request])
        t18 = Thread(target=StatewiseGovtJobs.call_karnataka_govt_jobs,args=[request])
        t19 = Thread(target=StatewiseGovtJobs.call_kerala_govt_jobs,args=[request])
        t20 = Thread(target=StatewiseGovtJobs.call_lakshadweep_govt_jobs,args=[request])
        t21 = Thread(target=StatewiseGovtJobs.call_madhya_pradesh_govt_jobs,args=[request])
        t22 = Thread(target=StatewiseGovtJobs.call_maharashtra_govt_jobs,args=[request])
        t23 = Thread(target=StatewiseGovtJobs.call_manipur_govt_jobs,args=[request])
        t24 = Thread(target=StatewiseGovtJobs.call_meghalaya_govt_jobs,args=[request])
        t25 = Thread(target=StatewiseGovtJobs.call_mizoram_govt_jobs,args=[request])
        t26 = Thread(target=StatewiseGovtJobs.call_nagaland_govt_jobs,args=[request])
        t27 = Thread(target=StatewiseGovtJobs.call_puduchhery_govt_jobs,args=[request])
        t28 = Thread(target=StatewiseGovtJobs.call_punjab_govt_jobs,args=[request])
        t29 = Thread(target=StatewiseGovtJobs.call_rajastan_govt_jobs,args=[request])
        t30 = Thread(target=StatewiseGovtJobs.call_sikkim_govt_jobs,args=[request])
        t31 = Thread(target=StatewiseGovtJobs.call_tamil_nadu_govt_jobs,args=[request])
        t32 = Thread(target=StatewiseGovtJobs.call_telengana_govt_jobs,args=[request])
        t33 = Thread(target=StatewiseGovtJobs.call_tripura_govt_jobs,args=[request])
        t34 = Thread(target=StatewiseGovtJobs.call_uttarakhand_govt_jobs,args=[request])
        t35 = Thread(target=StatewiseGovtJobs.call_uttar_pradesh_govt_jobs,args=[request])
        t36 = Thread(target=StatewiseGovtJobs.call_west_bengal_govt_jobs,args=[request])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()
        t26.start()
        t27.start()
        t28.start()
        t29.start()
        t30.start()
        t31.start()
        t32.start()
        t33.start()
        t34.start()
        t35.start()
        t36.start()


        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()
        t26.join()
        t27.join()
        t28.join()
        t29.join()
        t30.join()
        t31.join()
        t32.join()
        t33.join()
        t34.join()
        t35.join()
        t36.join()

        return HttpResponse("success")

    def teaching_jobs(request):
        t1 = Thread(target=StatewiseTeachingJobs.call_andaman_teaching_jobs,args=[request])
        t2 = Thread(target=StatewiseTeachingJobs.call_odisha_teaching_jobs,args=[request])
        t3 = Thread(target=StatewiseTeachingJobs.call_andhra_teaching_jobs,args=[request])
        t4 = Thread(target=StatewiseTeachingJobs.call_arunachal_pradesh_teaching_jobs,args=[request])
        t5 = Thread(target=StatewiseTeachingJobs.call_assam_teaching_jobs,args=[request])
        t6 = Thread(target=StatewiseTeachingJobs.call_bihar_teaching_jobs,args=[request])
        t7 = Thread(target=StatewiseTeachingJobs.call_chandigarh_teaching_jobs,args=[request])
        t8 = Thread(target=StatewiseTeachingJobs.call_chhattisgarh_teaching_jobs,args=[request])
        t9 = Thread(target=StatewiseTeachingJobs.call_dadra_nagar_teaching_jobs,args=[request])
        t10 = Thread(target=StatewiseTeachingJobs.call_daman_diu_teaching_jobs,args=[request])
        t11 = Thread(target=StatewiseTeachingJobs.call_delhi_teaching_jobs,args=[request])
        t12 = Thread(target=StatewiseTeachingJobs.call_goa_teaching_jobs,args=[request])
        t13 = Thread(target=StatewiseTeachingJobs.call_gujurat_teaching_jobs,args=[request])
        t14 = Thread(target=StatewiseTeachingJobs.call_haryana_teaching_jobs,args=[request])
        t15 = Thread(target=StatewiseTeachingJobs.call_himachal_pradesh_teaching_jobs,args=[request])
        t16 = Thread(target=StatewiseTeachingJobs.call_jammu_kashmir_teaching_jobs,args=[request])
        t17 = Thread(target=StatewiseTeachingJobs.call_jharkhand_teaching_jobs,args=[request])
        t18 = Thread(target=StatewiseTeachingJobs.call_karnataka_teaching_jobs,args=[request])
        t19 = Thread(target=StatewiseTeachingJobs.call_kerala_teaching_jobs,args=[request])
        t20 = Thread(target=StatewiseTeachingJobs.call_lakshadweep_teaching_jobs,args=[request])
        t21 = Thread(target=StatewiseTeachingJobs.call_madhya_pradesh_teaching_jobs,args=[request])
        t22 = Thread(target=StatewiseTeachingJobs.call_maharashtra_teaching_jobs,args=[request])
        t23 = Thread(target=StatewiseTeachingJobs.call_manipur_teaching_jobs,args=[request])
        t24 = Thread(target=StatewiseTeachingJobs.call_meghalaya_teaching_jobs,args=[request])
        t25 = Thread(target=StatewiseTeachingJobs.call_mizoram_teaching_jobs,args=[request])
        t26 = Thread(target=StatewiseTeachingJobs.call_nagaland_teaching_jobs,args=[request])
        t27 = Thread(target=StatewiseTeachingJobs.call_puduchhery_teaching_jobs,args=[request])
        t28 = Thread(target=StatewiseTeachingJobs.call_punjab_teaching_jobs,args=[request])
        t29 = Thread(target=StatewiseTeachingJobs.call_rajastan_teaching_jobs,args=[request])
        t30 = Thread(target=StatewiseTeachingJobs.call_sikkim_teaching_jobs,args=[request])
        t31 = Thread(target=StatewiseTeachingJobs.call_tamil_nadu_teaching_jobs,args=[request])
        t32 = Thread(target=StatewiseTeachingJobs.call_telengana_teaching_jobs,args=[request])
        t33 = Thread(target=StatewiseTeachingJobs.call_tripura_teaching_jobs,args=[request])
        t34 = Thread(target=StatewiseTeachingJobs.call_uttarakhand_teaching_jobs,args=[request])
        t35 = Thread(target=StatewiseTeachingJobs.call_uttar_pradesh_teaching_jobs,args=[request])
        t36 = Thread(target=StatewiseTeachingJobs.call_west_bengal_teaching_jobs,args=[request])
        t37 = Thread(target=StatewiseTeachingJobs.call_all_india_teaching_jobs,args=[request])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()
        t26.start()
        t27.start()
        t28.start()
        t29.start()
        t30.start()
        t31.start()
        t32.start()
        t33.start()
        t34.start()
        t35.start()
        t36.start()
        t37.start()


        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()
        t26.join()
        t27.join()
        t28.join()
        t29.join()
        t30.join()
        t31.join()
        t32.join()
        t33.join()
        t34.join()
        t35.join()
        t36.join()
        t37.join()

        return HttpResponse("success")

    def engineering_jobs(request):
        t1 = Thread(target=StatewiseEngineeringJobs.call_andaman_engg_jobs,args=[request])
        t2 = Thread(target=StatewiseEngineeringJobs.call_odisha_engg_jobs,args=[request])
        t3 = Thread(target=StatewiseEngineeringJobs.call_andhra_engg_jobs,args=[request])
        t4 = Thread(target=StatewiseEngineeringJobs.call_arunachal_pradesh_engg_jobs,args=[request])
        t5 = Thread(target=StatewiseEngineeringJobs.call_assam_engg_jobs,args=[request])
        t6 = Thread(target=StatewiseEngineeringJobs.call_bihar_engg_jobs,args=[request])
        t7 = Thread(target=StatewiseEngineeringJobs.call_chandigarh_engg_jobs,args=[request])
        t8 = Thread(target=StatewiseEngineeringJobs.call_chhattisgarh_engg_jobs,args=[request])
        t9 = Thread(target=StatewiseEngineeringJobs.call_dadra_nagar_engg_jobs,args=[request])
        t10 = Thread(target=StatewiseEngineeringJobs.call_daman_diu_engg_jobs,args=[request])
        t11 = Thread(target=StatewiseEngineeringJobs.call_delhi_engg_jobs,args=[request])
        t12 = Thread(target=StatewiseEngineeringJobs.call_goa_engg_jobs,args=[request])
        t13 = Thread(target=StatewiseEngineeringJobs.call_gujurat_engg_jobs,args=[request])
        t14 = Thread(target=StatewiseEngineeringJobs.call_haryana_engg_jobs,args=[request])
        t15 = Thread(target=StatewiseEngineeringJobs.call_himachal_pradesh_engg_jobs,args=[request])
        t16 = Thread(target=StatewiseEngineeringJobs.call_jammu_kashmir_engg_jobs,args=[request])
        t17 = Thread(target=StatewiseEngineeringJobs.call_jharkhand_engg_jobs,args=[request])
        t18 = Thread(target=StatewiseEngineeringJobs.call_karnataka_engg_jobs,args=[request])
        t19 = Thread(target=StatewiseEngineeringJobs.call_kerala_engg_jobs,args=[request])
        t20 = Thread(target=StatewiseEngineeringJobs.call_lakshadweep_engg_jobs,args=[request])
        t21 = Thread(target=StatewiseEngineeringJobs.call_madhya_pradesh_engg_jobs,args=[request])
        t22 = Thread(target=StatewiseEngineeringJobs.call_maharashtra_engg_jobs,args=[request])
        t23 = Thread(target=StatewiseEngineeringJobs.call_manipur_engg_jobs,args=[request])
        t24 = Thread(target=StatewiseEngineeringJobs.call_meghalaya_engg_jobs,args=[request])
        t25 = Thread(target=StatewiseEngineeringJobs.call_mizoram_engg_jobs,args=[request])
        t26 = Thread(target=StatewiseEngineeringJobs.call_nagaland_engg_jobs,args=[request])
        t27 = Thread(target=StatewiseEngineeringJobs.call_puduchhery_engg_jobs,args=[request])
        t28 = Thread(target=StatewiseEngineeringJobs.call_punjab_engg_jobs,args=[request])
        t29 = Thread(target=StatewiseEngineeringJobs.call_rajastan_engg_jobs,args=[request])
        t30 = Thread(target=StatewiseEngineeringJobs.call_sikkim_engg_jobs,args=[request])
        t31 = Thread(target=StatewiseEngineeringJobs.call_tamil_nadu_engg_jobs,args=[request])
        t32 = Thread(target=StatewiseEngineeringJobs.call_telengana_engg_jobs,args=[request])
        t33 = Thread(target=StatewiseEngineeringJobs.call_tripura_engg_jobs,args=[request])
        t34 = Thread(target=StatewiseEngineeringJobs.call_uttarakhand_engg_jobs,args=[request])
        t35 = Thread(target=StatewiseEngineeringJobs.call_uttar_pradesh_engg_jobs,args=[request])
        t36 = Thread(target=StatewiseEngineeringJobs.call_west_bengal_engg_jobs,args=[request])
        t37 = Thread(target=StatewiseEngineeringJobs.call_all_india_engg_jobs,args=[request])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()
        t26.start()
        t27.start()
        t28.start()
        t29.start()
        t30.start()
        t31.start()
        t32.start()
        t33.start()
        t34.start()
        t35.start()
        t36.start()
        t37.start()


        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()
        t26.join()
        t27.join()
        t28.join()
        t29.join()
        t30.join()
        t31.join()
        t32.join()
        t33.join()
        t34.join()
        t35.join()
        t36.join()
        t37.join()

        return HttpResponse("success")

    def banking_jobs(request):
        t1 = Thread(target=BankingJobs.call_all_bank_jobs,args=[request])
        t2 = Thread(target=BankingJobs.call_other_financial_jobs,args=[request])

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        return HttpResponse("success")

    def railway_jobs(request):
        res = RailwayJobs.call_railway_jobs(request)
        return HttpResponse("success")

    def police_jobs(request):
        t1 = Thread(target=PoliceJobs.call_police_defence_jobs,args=[request])
        t2 = Thread(target=PoliceJobs.call_statewise_police_jobs,args=[request])
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return HttpResponse("success")




class EngineeringJobs:
    def common(model1,model2,model3,model4):
        import json
        import ast
        all_india_engg_job_type2=[]
        dict={}
        job_model = model1
        job_details_model = model2
        job_table = model3
        job_details_table = model4
        all_india_engg_job_type1 = list(job_model.objects.filter(type=1).values())
        all_india_engg_job_type3 = list(job_model.objects.filter(type=3).values())
        all_india_engg_job_type2_raw = job_details_model.objects.raw("""
                                                            select """ + job_details_table + """.more_info as more_info,
                                                            """ + job_details_table + """.id,""" + job_table + """.id,
                                                            """ + job_table + """.start_date as start_date,
                                                            """ + job_table + """.last_date as last_date,
                                                            """ + job_table + """.post_name as post_name,
                                                            """ + job_table + """.education as education,
                                                            """ + job_table + """.requirement_board as requirement_board,
                                                            """ + job_table + """.type as type from
                                                            """ + job_table + """ inner join """ + job_details_table + """ on
                                                            """ + job_details_table + """.join_id=""" + job_table + """.join_id
                                                            where """ + job_table + """.type=2 order by """ + job_table + """.start_date
                                                            """)

        for i in all_india_engg_job_type2_raw:
            dict.update({"start_date":i.start_date,"last_date":i.last_date,
                        "post_name":i.post_name,"education":i.education,
                        "requirement_board":i.requirement_board,"type":i.type,"more_info":ast.literal_eval("" + i.more_info + "")})
            all_india_engg_job_type2.append(dict.copy())
        all_india_engg_jobs = all_india_engg_job_type1 + all_india_engg_job_type2 + all_india_engg_job_type3
        return all_india_engg_jobs

    def make_engineer_bundle():
        EnggJobs.objects.all().delete()
        all_india_engg_jobs         = EngineeringJobs.common(AllIndiaEnggJobs, AllIndiaEnggJobDetails,"scrap_allindiaenggjobs","details_allindiaenggjobdetails")
        all_india_fellow_engg_jobs  = EngineeringJobs.common(AllIndiaFellowEnggJobs, AllIndiaFellowEnggJobDetails,"scrap_allindiafellowenggjobs","details_allindiafellowenggjobdetails")
        andaman_engg_jobs           = EngineeringJobs.common(AndamanNicoborEnggJobs, AndamanNicoborEnggJobDetails,"scrap_andamannicoborenggjobs","details_andamannicoborenggjobdetails")
        andhra_engg_jobs            = EngineeringJobs.common(AndhraPradeshEnggJobs, AndhraPradeshEnggJobDetails,"scrap_andhrapradeshenggjobs","details_andhrapradeshenggjobdetails")
        arunachal_pradesh_engg_jobs = EngineeringJobs.common(ArunachalPradeshEnggJobs, ArunachalPradeshEnggJobDetails,"scrap_arunachalpradeshenggjobs","details_arunachalpradeshenggjobdetails")
        assam_engg_jobs             = EngineeringJobs.common(AssamEnggJobs, AssamEnggJobDetails,"scrap_assamenggjobs","details_assamenggjobdetails")
        bihar_engg_jobs             = EngineeringJobs.common(BiharEnggJobs, BiharEnggJobDetails,"scrap_biharenggjobs","details_biharenggjobdetails")
        chandigarh_engg_jobs        = EngineeringJobs.common(ChandigarhEnggJobs, ChandigarhEnggJobDetails,"scrap_chandigarhenggjobs","details_chandigarhenggjobdetails")
        chattisgarh_engg_jobs       = EngineeringJobs.common(ChhattisgarhEnggJobs, ChhattisgarhEnggJobDetails,"scrap_chhattisgarhenggjobs","details_chhattisgarhenggjobdetails")
        dadra_nagar_engg_jobs       = EngineeringJobs.common(DadraNagarHaveliEnggJobs, DadraNagarHaveliEnggJobDetails,"scrap_dadranagarhavelienggjobs","details_dadranagarhavelienggjobdetails")
        daman_diu_engg_jobs         = EngineeringJobs.common(DamanDiuEnggJobs, DamanDiuEnggJobDetails,"scrap_damandiuenggjobs","details_damandiuenggjobdetails")
        delhi_engg_jobs             = EngineeringJobs.common(DelhiEnggJobs, DelhiEnggJobDetails,"scrap_delhienggjobs","details_delhienggjobdetails")
        goa_engg_jobs               = EngineeringJobs.common(GoaEnggJobs, GoaEnggJobDetails,"scrap_goaenggjobs","details_goaenggjobdetails")
        gujurat_engg_jobs           = EngineeringJobs.common(GujuratEnggJobs, GujuratEnggJobDetails,"scrap_gujuratenggjobs","details_gujuratenggjobdetails")
        haryana_engg_jobs           = EngineeringJobs.common(HaryanaEnggJobs, HaryanaEnggJobDetails,"scrap_haryanaenggjobs","details_haryanaenggjobdetails")
        himachal_pradesh_engg_jobs  = EngineeringJobs.common(HimachalPradeshEnggJobs, HimachalPradeshEnggJobDetails,"scrap_himachalpradeshenggjobs","details_himachalpradeshenggjobdetails")
        jammu_kashmir_engg_jobs     = EngineeringJobs.common(JammuKashmirEnggJobs, JammuKashmirEnggJobDetails,"scrap_jammukashmirenggjobs","details_chhattisgarhenggjobdetails")
        jharkhand_engg_jobs         = EngineeringJobs.common(JharkhandEnggJobs, JharkhandEnggJobDetails,"scrap_jharkhandenggjobs","details_jharkhandenggjobdetails")
        karnataka_engg_jobs         = EngineeringJobs.common(KarnatakaEnggJobs, KarnatakaEnggJobDetails,"scrap_karnatakaenggjobs","details_karnatakaenggjobdetails")
        kerala_engg_jobs            = EngineeringJobs.common(KeralaEnggJobs, KeralaEnggJobDetails,"scrap_keralaenggjobs","details_keralaenggjobdetails")
        lakshadweep_engg_jobs       = EngineeringJobs.common(LakshadweepEnggJobs, LakshadweepEnggJobDetails,"scrap_lakshadweepenggjobs","details_lakshadweepenggjobdetails")
        madhya_pradesh_engg_jobs    = EngineeringJobs.common(MadhyaPradeshEnggJobs, MadhyaPradeshEnggJobDetails,"scrap_madhyapradeshenggjobs","details_madhyapradeshenggjobdetails")
        maharastra_engg_jobs        = EngineeringJobs.common(MaharashtraEnggJobs, MaharashtraEnggJobDetails,"scrap_maharashtraenggjobs","details_maharashtraenggjobdetails")
        manipur_engg_jobs           = EngineeringJobs.common(ManipurEnggJobs, ManipurEnggJobDetails,"scrap_manipurenggjobs","details_manipurenggjobdetails")
        meghalaya_engg_jobs         = EngineeringJobs.common(MeghalayaEnggJobs, MeghalayaEnggJobDetails,"scrap_meghalayaenggjobs","details_meghalayaenggjobdetails")
        mizoram_engg_jobs           = EngineeringJobs.common(MizoramEnggJobs, MizoramEnggJobDetails,"scrap_mizoramenggjobs","details_mizoramenggjobdetails")
        nagaland_engg_jobs          = EngineeringJobs.common(NagalandEnggJobs, NagalandEnggJobDetails,"scrap_nagalandenggjobs","details_nagalandenggjobdetails")
        odisha_engg_jobs            = EngineeringJobs.common(OdishaEnggJobs, OdishaEnggJobDetails,"scrap_odishaenggjobs","details_odishaenggjobdetails")
        pudduchhery_engg_jobs       = EngineeringJobs.common(PuduchheryEnggJobs, PuduchheryEnggJobDetails,"scrap_puduchheryenggjobs","details_puduchheryenggjobdetails")
        punjab_engg_jobs            = EngineeringJobs.common(PunjabEnggJobs, PunjabEnggJobDetails,"scrap_punjabenggjobs","details_punjabenggjobdetails")
        rajastan_engg_jobs          = EngineeringJobs.common(RajasthanEnggJobs, RajasthanEnggJobDetails,"scrap_rajasthanenggjobs","details_rajasthanenggjobdetails")
        sikkim_engg_jobs            = EngineeringJobs.common(SikkimEnggJobs, SikkimEnggJobDetails,"scrap_sikkimenggjobs","details_sikkimenggjobdetails")
        tamilnadu_engg_jobs         = EngineeringJobs.common(TamilNaduEnggJobs, TamilNaduEnggJobDetails,"scrap_tamilnaduenggjobs","details_tamilnaduenggjobdetails")
        telengana_engg_jobs         = EngineeringJobs.common(TelanganaEnggJobs, TelanganaEnggJobDetails,"scrap_telanganaenggjobs","details_telanganaenggjobdetails")
        tripura_engg_jobs           = EngineeringJobs.common(TripuraEnggJobs, TripuraEnggJobDetails,"scrap_tripuraenggjobs","details_tripuraenggjobdetails")
        uttarakhand_engg_jobs       = EngineeringJobs.common(UttarakhandEnggJobs, UttarakhandEnggJobDetails,"scrap_uttarakhandenggjobs","details_uttarakhandenggjobdetails")
        uttarpradesh_engg_jobs      = EngineeringJobs.common(UttarPradeshEnggJobs, UttarPradeshEnggJobDetails,"scrap_uttarpradeshenggjobs","details_uttarpradeshenggjobdetails")
        west_bengal_engg_jobs       = EngineeringJobs.common(WestBengalEnggJobs, WestBengalEnggJobDetails,"scrap_westbengalenggjobs","details_westbengalenggjobdetails")

        engg_jobs = (all_india_engg_jobs + all_india_fellow_engg_jobs + andaman_engg_jobs + andhra_engg_jobs + arunachal_pradesh_engg_jobs +
        assam_engg_jobs + bihar_engg_jobs + chandigarh_engg_jobs + chattisgarh_engg_jobs + dadra_nagar_engg_jobs + daman_diu_engg_jobs +
        delhi_engg_jobs + goa_engg_jobs + gujurat_engg_jobs + haryana_engg_jobs + himachal_pradesh_engg_jobs + jammu_kashmir_engg_jobs +
        jharkhand_engg_jobs + karnataka_engg_jobs + kerala_engg_jobs + lakshadweep_engg_jobs + madhya_pradesh_engg_jobs + maharastra_engg_jobs +
        manipur_engg_jobs + meghalaya_engg_jobs + mizoram_engg_jobs + nagaland_engg_jobs + odisha_engg_jobs + pudduchhery_engg_jobs + punjab_engg_jobs +
        rajastan_engg_jobs + sikkim_engg_jobs + tamilnadu_engg_jobs + telengana_engg_jobs + tripura_engg_jobs + uttarakhand_engg_jobs + uttarpradesh_engg_jobs +
        west_bengal_engg_jobs)

        obj = EnggJobs.objects.create(engg_jobs = engg_jobs)
        if obj:
            return True
        else:
            return False


class Work:
    def perform(request):
        password = request.GET.get("password", None)
        if password == "Thinkonce":
            t1 = Thread(target=FinishAll.all_india_govt_jobs,args=[request])
            t2 = Thread(target=FinishAll.state_govt_jobs,args=[request])
            t3 = Thread(target=FinishAll.teaching_jobs,args=[request])
            t4 = Thread(target=FinishAll.engineering_jobs,args=[request])
            t5 = Thread(target=FinishAll.banking_jobs,args=[request])
            t6 = Thread(target=FinishAll.railway_jobs,args=[request])
            t7 = Thread(target=FinishAll.police_jobs,args=[request])
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
            print("Done")
            engg_jobs = EngineeringJobs.make_engineer_bundle()
            return HttpResponse("success")
        else:
            return render(request, '401.html', status=401)

def handler_404(request):
    return render(request, '404.html', status=404)

def handler_500(request):
    return render(request, '500.html', status=404)

def handler_403(request):
    return render(request, '403.html', status=404)

def handler_400(request):
    return render(request, '400.html', status=404)

import ast
def make_json(request):
    lst=[]
    data    = request.body
    convert = data.decode("utf-8")
    ds      = json.loads(convert)
    s = ds["api"]
    dict = ast.literal_eval("[" + s + "]")
    return JsonResponse(dict,safe=False)

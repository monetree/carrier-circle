from django.urls import path
from .views import FinishAll,Work,make_json


urlpatterns = [
    #finalize all india
    path('finish_all_india_govt_jobs/', FinishAll.all_india_govt_jobs),
    path('finish_state_govt_jobs/', FinishAll.state_govt_jobs),
    path('finish_teaching_jobs/', FinishAll.teaching_jobs),
    path('finish_engineering_jobs/', FinishAll.engineering_jobs),
    path('finish_banking_jobs/', FinishAll.banking_jobs),
    path('finish_railway_jobs/', FinishAll.railway_jobs),
    path('finish_police_jobs/', FinishAll.police_jobs),
    path('finish_police_jobs/', FinishAll.police_jobs),
    path('', Work.perform),
    path('make_json/', make_json),
]

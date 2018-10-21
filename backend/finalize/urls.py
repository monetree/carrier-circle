from django.urls import path
from .views import *

urlpatterns = [
    path('call_all_india_govt_jobs/', AllIndiaGovernmentJobs.call_all_india_govt_jobs),
    path('call_andaman_govt_jobs/', StatewiseGovtJobs.call_andaman_govt_jobs),
    path('call_odisha_govt_jobs/', StatewiseGovtJobs.call_odisha_govt_jobs),

]

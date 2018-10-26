from django.urls import path
from .views import FinishAll

urlpatterns = [
    #finalize all india
    path('finish_all_india_govt_jobs/', FinishAll.all_india_govt_jobs),
    path('finish_state_govt_jobs/', FinishAll.state_govt_jobs),

]

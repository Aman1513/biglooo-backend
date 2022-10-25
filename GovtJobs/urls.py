from django.urls import  re_path, include
from rest_framework import routers
from .views import GovtJobsList

app_name = 'GovtJobs'

router = routers.DefaultRouter()

router.register(r'api', GovtJobsList, basename='GovtJobs')

urlpatterns = [
    re_path("^",include(router.urls))
]
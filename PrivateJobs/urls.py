from django.urls import  re_path, include
from rest_framework import routers
from .views import PrivateJobsList

app_name = 'PrivateJobs'

router = routers.DefaultRouter()

router.register(r'api', PrivateJobsList, basename='PrivateJobs')

urlpatterns = [
    re_path("^",include(router.urls))
]
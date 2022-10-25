from django.urls import  re_path, include
from rest_framework import routers
from .views import LoginDetailList

app_name = 'LoginDetail'

router = routers.DefaultRouter()

router.register(r'api', LoginDetailList, basename='LoginDetail')

urlpatterns = [
    re_path("^",include(router.urls))
]
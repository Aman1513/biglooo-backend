from django.urls import  re_path, include
from rest_framework import routers
from .views import BlogList

app_name = 'Blog'

router = routers.DefaultRouter()

router.register(r'api', BlogList, basename='Blog')

urlpatterns = [
    re_path("^",include(router.urls))
]
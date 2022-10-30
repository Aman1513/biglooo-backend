from .models import LoginDetail
from rest_framework.viewsets import ModelViewSet
from .serializer import LoginDetailSerializers
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class LoginDetailList(ModelViewSet):
    queryset = LoginDetail.objects.all()
    serializer_class = LoginDetailSerializers 
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['name', 'email']
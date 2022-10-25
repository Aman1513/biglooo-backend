from .models import Blog
from rest_framework.viewsets import ModelViewSet
from .serializer import BlogSerializers
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BlogList(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers 
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['heading']
from .models import GovtJobs
from datetime import datetime
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import GovtJobsSerializers
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

# Create your views here.

class GovtJobsList(ReadOnlyModelViewSet):
    queryset = GovtJobs.objects.all()
    serializer_class = GovtJobsSerializers 
    filter_backends = [SearchFilter]
    search_fields = ['search', 'qualification', 'department_name', 'job_title','id']
    DeleteJobs = GovtJobs.objects.filter( last_date__lt = datetime.now())
    for i in DeleteJobs:
        i.delete() 
from .models import PrivateJobs
from datetime import datetime
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import PrivateJobsSerializers
from rest_framework.filters import SearchFilter
# Create your views here.

class PrivateJobsList(ReadOnlyModelViewSet):
    queryset = PrivateJobs.objects.all()
    serializer_class = PrivateJobsSerializers 
    filter_backends = [SearchFilter]
    search_fields = ['company_name', 'job_title', 'salary', 'search', 'qualification', 'location', 'experience','id']
    DeleteJobs = PrivateJobs.objects.filter( last_date__lt = datetime.now())
    for i in DeleteJobs:
        i.delete() 
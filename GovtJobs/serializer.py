from .models import *
from rest_framework import serializers

class GovtJobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GovtJobs
        fields = ('__all__')
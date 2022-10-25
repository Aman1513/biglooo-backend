from .models import *
from rest_framework import serializers

class PrivateJobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrivateJobs
        fields = ('__all__')
from .models import *
from rest_framework import serializers

class LoginDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginDetail
        fields = ('__all__')
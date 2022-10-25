from .models import *
from rest_framework import serializers

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('__all__')
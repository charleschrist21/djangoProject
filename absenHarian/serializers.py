from rest_framework import serializers
from .models import absenHarian

class absenHarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = absenHarian
        fields = '__all__'

from rest_framework import serializers
from .models import absenTanggal

class absenTanggalSerializer(serializers.ModelSerializer):
    class Meta:
        model = absenTanggal
        fields = '__all__'

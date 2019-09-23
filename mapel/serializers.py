from rest_framework import serializers
from .models import mapel

class mapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mapel
        fields = '__all__'

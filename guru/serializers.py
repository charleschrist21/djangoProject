from rest_framework import serializers
from .models import guru

class guruSerializer(serializers.ModelSerializer):
    class Meta:
        model = guru
        fields = '__all__'

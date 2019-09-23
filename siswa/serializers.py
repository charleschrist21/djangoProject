from rest_framework import serializers
from .models import siswa

class siswaSerializers(serializers.ModelSerializer):
    class Meta:
        model = siswa
        fields = '__all__'

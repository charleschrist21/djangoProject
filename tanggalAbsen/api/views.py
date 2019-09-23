from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from ..models import absenTanggal
from ..serializers import absenTanggalSerializer

class absenTanggalCreate(generics.ListCreateAPIView):
    queryset = absenTanggal.objects.all()
    serializer_class = absenTanggalSerializer

    parser_class = (FileUploadParser)

class absenTanggalEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = absenTanggal.objects.all()
    serializer_class = absenTanggalSerializer

    parser_class = (FileUploadParser)

from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from ..models import absenHarian
from ..serializers import absenHarianSerializer

class absenHarianCreate(generics.ListCreateAPIView):
    queryset = absenHarian.objects.all()
    serializer_class = absenHarianSerializer

    parser_class = (FileUploadParser)

class absenHarianEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = absenHarian.objects.all()
    serializer_class = absenHarianSerializer

    parser_class = (FileUploadParser)

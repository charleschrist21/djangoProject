from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from ..models import mapel
from ..serializers import mapelSerializer

class mapelCreate(generics.ListCreateAPIView):
    queryset = mapel.objects.all()
    serializer_class = mapelSerializer

    parser_class = (FileUploadParser)

class mapelEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = mapel.objects.all()
    serializer_class = mapelSerializer

    parser_class = (FileUploadParser)

from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from ..models import guru
from ..serializers import guruSerializer

class guruCreate(generics.ListCreateAPIView):
    queryset = guru.objects.all()
    serializer_class = guruSerializer

    parser_class = (FileUploadParser)

class guruEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = guru.objects.all()
    serializer_class = guruSerializer

    parser_class = (FileUploadParser)

from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from ..models import siswa
from ..serializers import siswaSerializers

class siswaCreate(generics.ListCreateAPIView):
    queryset = siswa.objects.all()
    serializer_class = siswaSerializers

    parser_class = (FileUploadParser)

class siswaEditAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = siswa.objects.all()
    serializer_class = siswaSerializers

    parser_class = (FileUploadParser)

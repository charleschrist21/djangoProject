from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import absenTanggalCreate,absenTanggalEdit

urlpatterns={
    path('', absenTanggalCreate.as_view(), name='absenTanggalCreate'),
    url(r'^detail/(?P<pk>[0-9+])/$', absenTanggalCreate.as_view(), name='absenTanggalEdit')
}

urlpatterns = format_suffix_patterns(urlpatterns)

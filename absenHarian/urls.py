from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import absenHarianCreate,absenHarianEdit

urlpatterns={
    path('', absenHarianCreate.as_view(), name='absenHarianCreate'),
    url(r'^detail/(?P<pk>[0-9+])/$', absenHarianEdit.as_view(), name='absenHarianEdit')
}
urlpatterns = format_suffix_patterns(urlpatterns)

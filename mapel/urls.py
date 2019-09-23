from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import mapelCreate,mapelEdit

urlpatterns={
    path('', mapelCreate.as_view(), name='mapelCreate'),
    url(r'^detail/(?P<pk>[0-9+])/$', mapelEdit.as_view(), name='mapelEdit')
}
urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import guruCreate,guruEdit

urlpatterns={
    path('', guruCreate.as_view(), name='guruCreate'),
    url(r'^detail/(?P<pk>[0-9+])/$', guruEdit.as_view(), name='guruEdit')
}
urlpatterns = format_suffix_patterns(urlpatterns)

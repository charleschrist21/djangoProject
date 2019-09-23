from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import siswaCreate,siswaEditAndDelete

urlpatterns={
    path('', siswaCreate.as_view(), name='siswaCreate'),
    url(r'^detail/(?P<pk>[0-9+])/$', siswaEditAndDelete.as_view(), name='siswaEdit'),
}
urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url

from .views import (
    StatusAPIView, 
    StatusAPIDetailView,
    )

urlpatterns = [
    url(r'^$', StatusAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
]

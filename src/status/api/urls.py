from django.conf.urls import url

from .views import (
    StatusAPIView, 
    #StatusCreateAPIView,
    StatusDetailAPIView,
   # StatusUpdateAPIView,
    #StatusDeleteAPIView
    )

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
    
]


#Start with
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update/ -> Update
# /api/status/12/delete/ -> Delete


# End With

# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD


# Final

# /api/status/ -> CRUD & LS
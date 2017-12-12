from django.conf.urls import url


urlpatterns = [
    url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    url(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
    
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
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from accounts.api.permissions import AnonPermissionOnly


from status.api.serializers import StatusInlineUserSerializer
from status.models import Status

from .serializers import UserDetailSerializer


User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    #permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    queryset            = User.objects.filter(is_active=True)
    serializer_class    = UserDetailSerializer
    lookup_field        = 'username' # id

    def get_serializer_context(self):
        return {'request': self.request}





class UserStatusAPIView(generics.ListAPIView):
    serializer_class    = StatusInlineUserSerializer
    #pagination_class    = CFEAPIPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)






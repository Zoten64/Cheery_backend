from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer


# Create your views here.

class NotificationList(generics.ListAPIView):
    '''List all notifications for the authenticated user.'''
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a notification.'''
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

from rest_framework import generics, permissions
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Follow
from .serializers import FollowSerializer

# Create your views here.

class FollowList(generics.ListCreateAPIView):
    '''View for listing and creating likes'''
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowDetail(generics.RetrieveDestroyAPIView):
    '''View for retrieving, updating and deleting likes'''
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsOwnerOrReadOnly]

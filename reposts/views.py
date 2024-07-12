from rest_framework import generics, permissions
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Repost
from .serializers import LikeSerializer

# Create your views here.

class RepostList(generics.ListCreateAPIView):
    '''View for listing and creating likes'''
    queryset = Repost.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RepostDetail(generics.RetrieveDestroyAPIView):
    '''View for retrieving, updating and deleting likes'''
    queryset = Repost.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

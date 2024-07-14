from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.


class CommentList(generics.ListCreateAPIView):
    '''View for listing and creating comments'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''View for retrieving, updating and deleting comments'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

from django.db.models import Prefetch, Count
from django.shortcuts import render
from rest_framework import generics, permissions
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Post, Attachment
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    '''Lists all posts'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves a specific post
    Allows for updating and deletion of the user owns the post
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
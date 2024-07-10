from django.shortcuts import render
from rest_framework import generics
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    '''Lists all posts'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves a specific post
    Allows for updating and deletion of the user owns the post
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
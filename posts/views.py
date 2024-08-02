from django.http import HttpResponseNotFound, HttpResponseBadRequest
from rest_framework import generics, permissions, filters
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Post, Attachment
from .serializers import PostSerializer, AttachmentSerializer
from rest_framework.exceptions import PermissionDenied
from cheeryapi.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    '''Lists all posts'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'owner__username', 'tags__name']

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


class AttachmentList(generics.ListCreateAPIView):
    '''Lists all attachments'''
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['post']

    def perform_create(self, serializer):
        '''
        Overrides the perform_create method to ensure that
        the user owns the post
        '''
        post_id = self.request.data.get('post')
        # If there is no post ID specidied raise error
        if not post_id:
            raise HttpResponseBadRequest("Post ID must be provided.")

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise HttpResponseNotFound("Post does not exist.")

        if post.owner != self.request.user:
            raise PermissionDenied("You do not own this post.")

        serializer.save(owner=self.request.user)


class AttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Displays a specific attachment'''
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsOwnerOrReadOnly]

class TagList(generics.ListAPIView):
    '''
    View for searching for and retrieving posts based on tags
    Other searchable views will return posts matching any param
    This view only returns posts macthing a tag.
    Syntax: {url}/posts/tags/?search={tagname}
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__name']

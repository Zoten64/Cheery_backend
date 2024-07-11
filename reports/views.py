from rest_framework import generics, permissions
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import UserReport, PostReport
from .serializers import UserReportSerializer, PostReportSerializer

# Create your views here.

class UserReportList(generics.ListCreateAPIView):
    '''List all user reports'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserReport.objects.all()
    serializer_class = UserReportSerializer

class UserReportDetail(generics.RetrieveUpdateAPIView):
    '''
    Retrieve a specific user report and allow the user to update it
    Only admins can delete reports
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserReport.objects.all()
    serializer_class = UserReportSerializer

class PostReportList(generics.ListCreateAPIView):
    '''List all post reports'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer

class PostReportDetail(generics.RetrieveUpdateAPIView):
    '''
    Retrieve a specific post report and allow the user to update it
    Only admins can delete reports
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer
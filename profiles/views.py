from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
class ProfileList(generics.ListAPIView):
    '''List all profiles'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    '''Retrieve a specific profile'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
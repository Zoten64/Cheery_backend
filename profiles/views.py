from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from cheeryapi.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class ProfileList(generics.ListAPIView):
    '''List all profiles'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''Retrieve a specific profile'''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileOwner(generics.RetrieveDestroyAPIView):
    '''
    Retrieve the user associated with a profile
    Allows for deletion of account
    '''
    serializer_class = UserSerializer 

    def get_object(self):
        """
        Returns the user associated with the given profile's pk.
        """
        profile_pk = self.kwargs.get('pk')
        profile = Profile.objects.get(pk=profile_pk)
        return profile.owner
    
    def delete(self, request, *args, **kwargs):
        """
        Deletes the user associated with the given profile's pk.
        """
        user = self.get_object()
        if user == request.user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

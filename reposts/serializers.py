from django.db import IntegrityError
from rest_framework import serializers
from .models import Repost

class LikeSerializer(serializers.ModelSerializer):
    '''Serializer for the Like model'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Repost
        fields = '__all__'
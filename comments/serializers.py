from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    '''Serializer for the Comment model'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'

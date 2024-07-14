from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    '''Serializer for the Notification model'''
    recipient = serializers.ReadOnlyField(source='recipient.username')
    sender = serializers.ReadOnlyField(source='sender.username')
    post = serializers.ReadOnlyField(source='post.title')
    category_message = serializers.ReadOnlyField()

    class Meta:
        model = Notification
        fields = '__all__'

from rest_framework import serializers
from .models import Post, Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.id')
    def validate_attachment(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Whoops! Seems like your image exceeds 2MB. '
                'Please reduce the file size and try again.')
        if value.image.height > 4096 or value.image.width > 4096:
            raise serializers.ValidationError(
                'Whoops! Seems like your image is too large. '
                'Image dimensions cannot exceed 4096x4096 pixels.'
                'Please reduce the image size and try again.')
        return value

    class Meta:
        model = Attachment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attachments = serializers.SerializerMethodField()
    
    def get_attachments(self, obj):
        attachments = Attachment.objects.filter(post=obj)
        return AttachmentSerializer(attachments, many=True).data

    class Meta:
        model = Post
        fields = '__all__'
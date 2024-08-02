from rest_framework import serializers
from .models import Post, Attachment
from likes.models import Like
from reposts.models import Repost
from comments.models import Comment
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class AttachmentSerializer(serializers.ModelSerializer):
    '''Serializes an attachment object'''
    owner = serializers.ReadOnlyField(source='owner.username')

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


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    '''Serializes a post object'''
    owner = serializers.ReadOnlyField(source='owner.username')
    attachments = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    reposts_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    engagement_count = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    def get_attachments(self, obj):
        '''Gets all attachments associated with a post'''
        attachments = Attachment.objects.filter(post=obj)
        return AttachmentSerializer(attachments, many=True).data

    def get_likes_count(self, obj):
        '''Gets the number of likes associated with a post'''
        likes_count = Like.objects.filter(post=obj).count()
        return likes_count

    def get_reposts_count(self, obj):
        '''Gets the number of reposts associated with a post'''
        repost_count = Repost.objects.filter(post=obj).count()
        return repost_count

    def get_comments_count(self, obj):
        '''Gets the number of comments associated with a post'''
        comments_count = Comment.objects.filter(post=obj).count()
        return comments_count

    def get_engagement_count(self, obj):
        '''
        The total of likes, comments and reposts associated with a post
        Used to sort by trending
        '''
        repost_count = Repost.objects.filter(post=obj).count()
        likes_count = Like.objects.filter(post=obj).count()
        comments_count = Comment.objects.filter(post=obj).count()
        engagement_count = repost_count + likes_count + comments_count
        return engagement_count

    class Meta:
        model = Post
        fields = '__all__'

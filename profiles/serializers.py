from rest_framework import serializers
from django.contrib.auth.models import User
from follows.models import Follow
from posts.models import Post
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follower_id = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_follower_id(self, obj):
        '''Gets the id of the currently authenticated users follows'''
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follow.objects.filter(
                owner=user, followed_user=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_posts_count(self, obj):
        '''Gets the number of posts associated with a profile'''
        post_count = Post.objects.filter(owner=obj.owner).count()
        return post_count

    def get_followers_count(self, obj):
        '''Gets the number of followers associated with a profile'''
        followers_count = Follow.objects.filter(
            followed_user=obj.owner).count()
        return followers_count

    def get_following_count(self, obj):
        '''Gets the number of users a profile follows'''
        following_count = Follow.objects.filter(owner=obj.owner).count()
        return following_count

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

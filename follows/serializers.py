from django.db import IntegrityError
from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    '''Serializer for the Like model'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Follow
        fields = '__all__'


    def create(self, validated_data):
        if self.context['request'].user != validated_data['followed_user']:
            try:
                return super().create(validated_data)
            except IntegrityError:
                raise serializers.ValidationError({
                    'detail': 'can\'t follow the same user twice.'
                })
        else:
            raise serializers.ValidationError({
                'detail': 'can\'t follow yourself.'
            })
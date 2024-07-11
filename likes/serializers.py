from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like

class LikeSerializer(serializers.ModelSerializer):
    '''Serializer for the Like model'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = '__all__'


    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'can\'t like the same post twice.'
            })
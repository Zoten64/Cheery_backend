from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from notifications.models import Notification

# Create your models here.


class Follow(models.Model):
    '''Follow model. A user can only follow a person once'''
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers')
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed_users')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed_user']

    def __str__(self):
        return f'{self.owner.username} follows {self.followed_user.username}'


def create_notification(sender, instance, created, **kwargs):
    '''Create a notification when a user is followed.'''
    if created:
        Notification.objects.create(
            sender=instance.owner,
            recipient=instance.post.owner,
            category_message='REPOST',
            post=instance.post
        )


post_save.connect(create_notification, sender=Follow)

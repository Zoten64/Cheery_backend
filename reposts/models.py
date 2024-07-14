from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.db.models.signals import post_save
from notifications.models import Notification


# Create your models here.

class Repost(models.Model):
    '''Repost model. A post can be reposted multiple times by the same user.'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} reposted {self.post.title}'


def create_notification(sender, instance, created, **kwargs):
    '''Create a notification when a post is reposted.'''
    if created:
        Notification.objects.create(
            sender=instance.owner,
            recipient=instance.post.owner,
            category_message='REPOST',
            post=instance.post
        )


post_save.connect(create_notification, sender=Repost)

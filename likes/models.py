from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.db.models.signals import post_save
from notifications.models import Notification

# Create your models here.

class Like(models.Model):
    '''Like model. Makes sure a post can't be liked twice by the same user.'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'post')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'

def create_notification(sender, instance, created, **kwargs):
    '''Create a notification when a post is liked.'''
    if created:
        Notification.objects.create(
            sender=instance.owner,
            recipient=instance.post.owner,
            category_message='LIKED',
            post=instance.post
        )

post_save.connect(create_notification, sender=Like)

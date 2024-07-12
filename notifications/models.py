from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_MESSAGE = (('FOLLOW', 'followed you'), 
                    ('LIKED', 'liked your post'),
                    ('COMMENT', 'commented on your post'), 
                    ('REPOST', 'reposted your post'))


class Notification(models.Model):
    '''Notification model. Owner if the recipient of the notification.'''
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name='notification_recipient')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='notification_sender')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, 
                             blank=True, null=True)
    category_message = models.CharField(max_length=10, choices=CATEGORY_MESSAGE)
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.recipient} : {self.sender} {self.category_message}'
    
    class Meta:
        ordering = ['-created']
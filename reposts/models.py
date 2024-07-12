from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

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

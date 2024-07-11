from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    '''Model for comments on posts'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                             related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner.username}\'s comment on {self.post.title}'

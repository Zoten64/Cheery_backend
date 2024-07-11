from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

USER_CATEGORY = (("SPAM", "Spamming, scamming or fraudulent behaviour"),
                 ("HATE", "Hate speech and/or abusive behaviour"),
                 ("ILLEGAL", "Illegal activities"),
                 ("OTHER", "Other"))

POST_CATEGORY = (("SPAM", "Spam, scam or fraudulent post"),
                 ("HATE", "Hate speech and/or abusive content"),
                 ("ILLEGAL", "Illegal content"),
                 ("OTHER", "Other"))


class UserReport(models.Model):
    '''Model allowing users to report other users'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name="reporting_user_user")
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name="reported_user")
    category = models.CharField(max_length=100, choices=USER_CATEGORY)
    reason = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.owner.username} report on {self.reported_user.username}'
    

class PostReport(models.Model):
    '''Model allowing users to report posts and comments'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name="reporting_user_post")
    reported_post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                      related_name="reported_post")
    category = models.CharField(max_length=100, choices=POST_CATEGORY)
    reason = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username} report on {self.reported_post.title}'

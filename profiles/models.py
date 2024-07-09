from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=255, blank=True)
    #Placeholder image, will be updated later with a custom default
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ddx8gv')
    pronouns = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
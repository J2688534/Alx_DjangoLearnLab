from django.db import models

# Create your models here.

# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

def profile_upload_path(instance, filename):
    return f'profiles/user_{instance.id}/{filename}'

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=profile_upload_path, blank=True, null=True)
    # followers = users who follow THIS user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

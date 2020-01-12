from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Profile(models.Model):
    """
    Profile Model
    proxy model that extends base data with other information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE )
    website = models.URLField(blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(
        upload_to='users/pictures', 
        blank=True, 
        null=True) 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Return username"""
        return self.user.username
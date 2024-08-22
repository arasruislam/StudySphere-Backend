from django.db import models
from django.contrib.auth.models import User


# All Models
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="account/images/", null=True, blank=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name_plural = 'User Account'


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    social_links = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Profile'

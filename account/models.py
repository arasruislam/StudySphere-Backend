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


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}"
    
    class Meta:
        verbose_name_plural = 'User Address'


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    social_links = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Profile'
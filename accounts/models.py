from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="accounts/images/")
    mobile_no = models.CharField(max_length=12)

from django.db import models
from accounts.models import CustomUser
from tuitions.models import Tuition


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    applied_tuitions = models.ManyToManyField(Tuition, through="TuitionApplication")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

from django.db import models
from accounts.models import CustomUser
from tuitions.models import TuitionApplication, Tuition


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name="profile", on_delete=models.CASCADE
    )
    applied_tuitions = models.ManyToManyField(
        Tuition, through="tuitions.TuitionApplication"
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

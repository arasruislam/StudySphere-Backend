from django.db import models
from accounts.models import CustomUser
from constants import APPLICATION_STATUS, STAR_CHOICES


class Tuition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to="tuitions/images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class TuitionApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS,
        default="pending",
    )

    def __str__(self):
        return f"{self.user.username}, apply for - {self.tuition.title}"


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.tuition.title}"

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
LEVEL_CHOICES = [
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
]
STAR_CHOICES = [
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
]


# Tuition model
class Tuition(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    level = models.CharField(choices=LEVEL_CHOICES, max_length=20)
    subject = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to="tuition/images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


# Tuition application
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}, applied for - {self.tuition.title}"


# Reviewer by an user
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"Review by {self.reviewer.username} on '{self.tuition.title}'"

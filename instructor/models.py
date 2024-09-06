from django.db import models
from django.contrib.auth.models import User


# Constant value
MEDIUM_OF_INSTRUCTION_CHOICES = [
    ("Both", "Both"),
    ("Bangla", "Bangla Medium"),
    ("English", "English Medium"),
]
TUTORING_STATUS_CHOICES = [
    ("Available", "Available"),
    ("Not_Available", "Not Available"),
]
GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
]


# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.URLField()
    instructor = models.CharField(max_length=20, default="instructor")
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    tuition_area = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=TUTORING_STATUS_CHOICES, default="Available"
    )
    days_per_week = models.IntegerField(default=5)
    experience = models.CharField(max_length=20)
    extra_facilities = models.CharField(max_length=200)
    medium_of_instruction = models.CharField(
        max_length=20, choices=MEDIUM_OF_INSTRUCTION_CHOICES
    )

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

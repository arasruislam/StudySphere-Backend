from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tuition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tuition_class = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
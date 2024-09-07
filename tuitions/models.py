from django.db import models
from student.models import Student
from instructor.models import Instructor

# constant values
STAR_CHOICES = [
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
]
CLASS_CHOICES = [
    ("Class 1", "Class_1"),
    ("Class 2", "Class_2"),
    ("Class 3", "Class_3"),
    ("Class 4", "Class_4"),
    ("Class 5", "Class_5"),
    ("Class 6", "Class_6"),
    ("Class 7", "Class_7"),
    ("Class 8", "Class_8"),
    ("Class 9", "Class_9"),
    ("Class 10", "Class_10"),
    ("HSC 1", "HSC_1st_Year"),
    ("HSC 2", "HSC_2nd_Year"),
]
MEDIUM_OF_INSTRUCTION_CHOICES = [
    ("Both", "Both"),
    ("Bangla", "Bangla"),
    ("English", "English"),
]
GENDER_CHOICES = [
    ("Both", "Both"),
    ("Male", "Male"),
    ("Female", "Female"),
]
TIME_CHOICES = [
    ("Morning", "Morning"),
    ("Afternoon", "Afternoon"),
    ("Evening", "Evening"),
]


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# tuition model
class Tuition(models.Model):
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="tuitions"
    )
    title = models.CharField(max_length=300)
    image = models.URLField()
    description = models.TextField()
    subject = models.ManyToManyField(Subject, related_name="tuitions")
    tuition_class = models.CharField(max_length=50, choices=CLASS_CHOICES)
    medium = models.CharField(max_length=50, choices=MEDIUM_OF_INSTRUCTION_CHOICES)
    student_gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    instructor_gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    tuition_time = models.CharField(max_length=20, choices=TIME_CHOICES)
    number_of_students = models.PositiveIntegerField(default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    availability = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

# application model
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username}, applied for - '{self.tuition.title}'"

# Reviewer by an user
class Review(models.Model):
    reviewer = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="reviews"
    )
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, related_name="reviews"
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return (
            f"Review by {self.reviewer.user.username} on '{self.tuition.title}'"
        )

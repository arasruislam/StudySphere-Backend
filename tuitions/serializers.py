from rest_framework import serializers
from .models import Review, Tuition, Application, Subject
from django.contrib.auth.models import User
from student.serializers import UserSerializer, StudentSerializer
from student.models import Student


# all serializers
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all()
    )  # change here
    # tuition = TuitionSerializer()
    tuition = serializers.PrimaryKeyRelatedField(queryset=Tuition.objects.all())

    class Meta:
        model = Application
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    # reviewer = StudentSerializer()
    reviewer = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    tuition = serializers.PrimaryKeyRelatedField(queryset=Tuition.objects.all())

    class Meta:
        model = Review
        fields = "__all__"

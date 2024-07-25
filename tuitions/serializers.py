from rest_framework import serializers
from .models import Tuition, Application, Review


# Serializers
class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = [
            "id",
            "title",
            "description",
            "level",
            "subject",
            "availability",
            "image",
            "created_at",
            "updated_at",
        ]


class TuitionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = ["title", "description", "level", "subject", "availability", "image"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "user", "tuition", "applied_at", "is_accepted"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "reviewer", "tuition", "body", "created", "rating"]

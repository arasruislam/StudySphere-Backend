from rest_framework import serializers
from .models import Tuition, Application, Review
from account.serializers import UserSerializer


class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tuition = TuitionSerializer(read_only=True)

    class Meta:
        model = Application
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

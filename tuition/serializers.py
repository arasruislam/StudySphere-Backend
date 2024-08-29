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

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        tuition_id = request.data.get("tuition")

        tuition = Tuition.objects.get(id=tuition_id)

        application = Application.objects.create(user=user, tuition=tuition)
        return application


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)
    tuition = TuitionSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

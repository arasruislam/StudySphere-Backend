from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    email = serializers.charfield(required=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

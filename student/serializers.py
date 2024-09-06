from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ["id", "mobile_no", "profile_img", "user"]


class StudentRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    mobile_no = serializers.CharField(max_length=15)
    profile_img = serializers.URLField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "mobile_no",
            "profile_img",
            "confirm_password",
        ]

    def save(self):
        username = self.validated_data["username"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        email = self.validated_data["email"]
        mobile_no = self.validated_data["mobile_no"]
        profile_img = self.validated_data["profile_img"]
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError({"error": "Password doesn't match!"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already exists!"})

        account = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        account.set_password(password)
        account.is_active = False
        account.save()

        # Create a Student associated with the new user
        Student.objects.create(
            user=account, mobile_no=mobile_no, profile_img=profile_img)
        return account


class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")

        if new_password != confirm_password:
            raise serializers.ValidationError(
                "New password and Confirm password does'ot match"
            )

        return data

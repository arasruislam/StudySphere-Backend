from rest_framework import serializers
from .models import Instructor
from student.serializers import UserSerializer
from django.contrib.auth.models import User

# Serializers
class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = "__all__"


class InstructorRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    profile_img = serializers.URLField(required=True)
    gender = serializers.CharField(max_length=50, required=True)
    phone = serializers.CharField(max_length=15, required=True)
    address = serializers.CharField(max_length=100, required=True)
    tuition_area = serializers.CharField(max_length=100, required=True)
    fee = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, allow_null=True
    )
    status = serializers.CharField(max_length=20, required=False, allow_blank=True)
    days_per_week = serializers.IntegerField(default=5)
    experience = serializers.CharField(max_length=20, required=True)
    extra_facilities = serializers.CharField(
        max_length=200, required=False, allow_blank=True
    )
    medium_of_instruction = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "profile_img",
            "gender",
            "phone",
            "address",
            "tuition_area",
            "fee",
            "status",
            "days_per_week",
            "experience",
            "extra_facilities",
            "medium_of_instruction",
        ]

    def save(self):
        username = self.validated_data["username"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        # Checking password match
        if password != confirm_password:
            raise serializers.ValidationError({"error": "Password Doesn't Match"})

        # Checking if email exists
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "The email you entered already exits"})

        # Creating the User account
        account = User(
            username=username, first_name=first_name, last_name=last_name, email=email
        )
        account.set_password(password)
        account.is_active = False  # User needs verification
        account.save()

        # Creating the associated TutorModel
        Instructor.objects.create(
            user=account,
            profile_img=self.validated_data["profile_img"],
            gender=self.validated_data["gender"],
            phone=self.validated_data["phone"],
            address=self.validated_data["address"],
            tuition_area=self.validated_data["tuition_area"],
            fee=self.validated_data.get("fee"),
            status=self.validated_data.get("status", "Available"),
            experience=self.validated_data["experience"],
            extra_facilities=self.validated_data.get("extra_facilities", ""),
            medium_of_instruction=self.validated_data["medium_of_instruction"],
        )

        return account


class InstructorLoginSerializer(serializers.Serializer):
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
                "New password and Confirm password does not match"
            )

        return data

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Account


# class UserSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(many=False)

#     class Meta:
#         model = Account
#         fields = "__all__"


# class AccountSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Account
#         fields = ["user", "image", "mobile_no"]


# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password",
#             "confirm_password",
#         ]
#         extra_kwargs = {"password": {"write_only": True}}

#     def save(self):
#         username = self.validated_data["username"]
#         first_name = self.validated_data["first_name"]
#         last_name = self.validated_data["last_name"]
#         email = self.validated_data["email"]
#         password = self.validated_data["password"]
#         password2 = self.validated_data["confirm_password"]

#         if password != password2:
#             raise serializers.ValidationError({"error": "Password Doesn't Matched"})
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({"error": "Email Already exists"})
#         account = User(
#             username=username, email=email, first_name=first_name, last_name=last_name
#         )

#         account.set_password(password)
#         account.is_active = False
#         account.save()
#         return account


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)


# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ["user", "image", "mobile_no"]


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        password = validated_data["password"]
        confirm_password = validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError({"error": "Passwords do not match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already exists"})

        user = User(
            username=username, email=email, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.is_active = False
        user.save()

        Account.objects.create(user=user)

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

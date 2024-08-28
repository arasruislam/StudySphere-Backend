from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .serializers import (
    UserProfileSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    ChangePasswordSerializer,
)
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import UserProfile
from django.contrib import messages

# for email sending
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.permissions import IsAdminUser, IsAuthenticated


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    # only superuser can see this api data
    permission_classes = [IsAuthenticated]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def perform_create(self, serializer):
        if UserProfile.objects.filter(user=self.request.user).exists():
            raise ValidationError("A profile for this user already exists.")

        serializer.save(user=self.request.user)


# user registration systemj
class UserRegistrationApiView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            print("token: ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid: ", uid)
            confirm_link = (
                f"https://studysphere-dnn6.onrender.com/accounts/active/{uid}/{token}"
            )
            email_subject = "Confirm your email"
            email_body = render_to_string(
                "confirm_email.html", {"confirm_link": confirm_link}
            )
            from_email = "StudySphere Team <noreply@studysphere.com>"
            email = EmailMultiAlternatives(
                email_subject, "", from_email, to=[user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response(
                {
                    "message": "A confirmation link has been sent to your email. Please check and confirm your email to activate your account."
                }
            )

        return Response(serializer.errors)


# activated user
def Activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated successfully!")
        return redirect("http://localhost:5173/profile")
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect("register")


# User login api view
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({"token": token.key, "user_id": user.id})
            else:
                return Response({"error": "Invalid Credential"})

        return Response({"error": serializer.errors})


# Logout view
class UserLogoutApiView(APIView):
    # def get(self, request):
    #     request.user.auth_token.delete()
    #     logout(request)
    #     return redirect("login")
    def get(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response(
                {"detail": "Already logged out or token does not exist."},
                status=status.HTTP_200_OK,
            )

        logout(request)
        return redirect("login")


# password change view set
class ChangePasswordView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]

            if not user.check_password(old_password):
                return Response(
                    {"error": "Old password is incorrect"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(new_password)
            user.save()
            return Response(
                {"success": "Password has been changed successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

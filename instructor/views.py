from .models import Instructor
from .serializers import (
    InstructorLoginSerializer,
    InstructorRegistrationSerializer,
    ChangePasswordSerializer,
    InstructorSerializer,
)
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
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
class InstructorApiView(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)


class InstructorRegistrationApiView(APIView):
    serializer_class = InstructorRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            instructor = serializer.save()
            token = default_token_generator.make_token(instructor)
            uid = urlsafe_base64_encode(force_bytes(instructor.pk))

            confirm_link = f"http://127.0.0.1:8000/api/instructor/active/{uid}/{token}"
            email_subject = "Confirm your email"
            email_body = render_to_string(
                "confirm_email.html", {"confirm_link": confirm_link}
            )
            email = EmailMultiAlternatives(email_subject, "", to=[instructor.email])
            email.attach_alternative(email_body, "text/html")
            # email.send()
            try:
                email.send()
            except Exception as e:
                return Response({"error": "Failed to send confirmation email. Please try again later."})

            return Response(
                {
                    "message": "A confirmation link has been sent to your email. Please check and confirm your email to activate your account."
                }
            )
        return Response(serializer.errors)


def Activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        instructor = User._default_manager.get(pk=uid)

    except User.DoesNotExist:
        instructor = None

    if instructor is not None and default_token_generator.check_token(
        instructor, token
    ):
        instructor.is_active = True
        instructor.save()
        messages.success(request, "Your account has been activated successfully!")
        return redirect("http://localhost:5173")
    else:
        return redirect("instructor_register")


class InstructorLoginApiView(APIView):
    def post(self, request):
        serializer = InstructorLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            instructor = authenticate(username=username, password=password)

            if instructor:
                try:
                    instructor_data = Instructor.objects.get(user=instructor)
                    instructor_id = instructor_data.id

                    token, _ = Token.objects.get_or_create(user=instructor)
                    login(request, instructor)
                    return Response(
                        {"token": token.key, "instructor_id": instructor_id}
                    )
                except:
                    return Response({"error": "instructor data not found"})
            else:
                return Response({"error": "Invalid Credential"})

        return Response({"error": serializer.errors})


class InstructorLogoutApiView(APIView):
    def get(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response(
                {"message": "Logged out successfully."}, status=status.HTTP_200_OK
            )

        logout(request)
        return redirect("login")


class ChangePasswordView(APIView):

    def post(self, request, *args, **kwargs):
        instructor = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]

            if not instructor.check_password(old_password):
                return Response(
                    {"error": "Old password is incorrect"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            instructor.set_password(new_password)
            instructor.save()
            return Response(
                {"success": "Password has been changed successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .serializers import (
    UserSerializer,
    StudentLoginSerializer,
    StudentRegistrationSerializer,
    StudentSerializer,
    ChangePasswordSerializer,
)
from .models import Student
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
class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)


class StudentRegistrationApiView(APIView):
    serializer_class = StudentRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            student = serializer.save()
            token = default_token_generator.make_token(student) 
            uid = urlsafe_base64_encode(force_bytes(student.pk))

            confirm_link = f"http://127.0.0.1:8000/api/student/active/{uid}/{token}"
            email_subject = "Confirm your email"
            email_body = render_to_string(
                "confirm_email.html", {"confirm_link": confirm_link}
            )
            from_email = "StudySphere Team <noreply@studysphere.com>"
            email = EmailMultiAlternatives(
                email_subject, "", from_email, to=[student.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(
                {
                    "message": "A confirmation link has been sent to your email. Please check and confirm your email to activate your account."
                }
            )

        return Response(serializer.errors)


def Activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        student = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        student = None

    if student is not None and default_token_generator.check_token(student, token):
        student.is_active = True
        student.save()
        messages.success(request, "Your account has been activated successfully!")
        return redirect("http://localhost:5173")
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect("register")


class StudentLoginApiView(APIView):
    def post(self, request):
        print(request.data)
        serializer = StudentLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            student = authenticate(username=username, password=password)

            if student:
                try:
                    student_data = Student.objects.get(user=student)
                    student_id = student_data.id

                    token, _ = Token.objects.get_or_create(user=student)
                    login(request, student)
                    return Response({"token": token.key, "student_id": student_id})
                except:
                    return Response({"error": "student data not found"})
            else:
                return Response({"error": "Invalid Credential"})

        return Response({"error": serializer.errors})


class StudentLogoutApiView(APIView):
    def get(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response(
                {"message": "Your are not logged in."},
                status=status.HTTP_200_OK,
            )

        logout(request)
        return redirect("login")


class ChangePasswordView(APIView):

    def post(self, request, *args, **kwargs):
        student = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]

            if not student.check_password(old_password):
                return Response(
                    {"error": "Old password is incorrect"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            student.set_password(new_password)
            student.save()
            return Response(
                {"success": "Password has been changed successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

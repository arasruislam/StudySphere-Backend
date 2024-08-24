from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .serializers import UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import UserProfile

# for email sending
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # this is not an good practice to get a data fro an single user.
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


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
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject = "Confirm your email"
            email_body = render_to_string(
                "confirm_email.html", {"confirm_link": confirm_link}
            )
            print(confirm_link)
            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response(
                {
                    "message": "A confirmation link has been sent to your email. Please check and confirm your email to activate your account."
                }
            )

        return Response(serializer.errors)

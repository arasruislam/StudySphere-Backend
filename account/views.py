from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .serializers import UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import UserProfile
from django.contrib import messages

# for email sending
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
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


# user registration system
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
            confirm_link = f"http://127.0.0.1:8000/accounts/active/{uid}/{token}"
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
        return redirect("register")
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect("register")


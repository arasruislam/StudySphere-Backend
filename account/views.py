from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


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

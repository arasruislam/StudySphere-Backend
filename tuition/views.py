from .serializers import TuitionSerializer, ApplicationSerializer, ReviewSerializer
from .models import Tuition, Application, Review
from rest_framework import viewsets, status, pagination
from rest_framework.permissions import IsAdminUser


# Create your views here.
class TuitionPagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = page_size
    max_page_size = 100


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer
    pagination_class = TuitionPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get("id")

        if id:
            queryset = queryset.filter(id=id)

        return queryset


# only superuser can see this api data
class ApplicationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


# only superuser can see this api data
class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        reviewer_id = self.request.query_params.get("reviewer_id")

        if reviewer_id:
            queryset = queryset.filter(reviewer_id=reviewer_id)

        return queryset

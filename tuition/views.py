from .serializers import TuitionSerializer, ApplicationSerializer, ReviewSerializer
from .models import Tuition, Application, Review
from rest_framework import viewsets


# Create your views here.
class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        reviewer_id = self.request.query_params.get("reviewer_id")

        if reviewer_id:
            queryset = queryset.filter(reviewer_id=reviewer_id)

        return queryset

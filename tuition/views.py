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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

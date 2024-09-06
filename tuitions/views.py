from rest_framework import viewsets, status, pagination
from .models import Tuition, Review, Application, Subject
from django.http import Http404
from .serializers import (
    TuitionSerializer,
    ReviewSerializer,
    ApplicationSerializer,
    SubjectSerializer,
)
from rest_framework.response import Response


# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TuitionPagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = page_size
    max_page_size = 100


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer
    pagination_class = TuitionPagination

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get("id")

        if id:
            queryset = queryset.filter(id=id)

        return queryset


class AllTuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get("id")
        instructor = self.request.query_params.get("instructor")
        tuition_class = self.request.query_params.get("tuition_class")
        medium = self.request.query_params.get("medium")
        student_gender = self.request.query_params.get("student_gender")
        instructor_gender = self.request.query_params.get("instructor_gender")
        tuition_time = self.request.query_params.get("tuition_time")
        subject_id = self.request.query_params.get("subject_id")

        if id:
            queryset = queryset.filter(id=id)
        if instructor:
            queryset = queryset.filter(instructor=instructor)
        if tuition_class:
            queryset = queryset.filter(tuition_class__icontains=tuition_class)
        if medium:
            queryset = queryset.filter(medium__icontains=medium)
        if student_gender:
            queryset = queryset.filter(student_gender__icontains=student_gender)
        if instructor_gender:
            queryset = queryset.filter(instructor_gender__icontains=instructor_gender)
        if tuition_time:
            queryset = queryset.filter(tuition_time__icontains=tuition_time)
        if subject_id:
            queryset = queryset.filter(subject=subject_id)

        return queryset


# only superuser can see this api data
class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        student = self.request.query_params.get("student")
        tuition = self.request.query_params.get("tuition")

        if student:
            queryset = queryset.filter(student=student)

        if tuition:
            queryset = queryset.filter(tuition=tuition)

        return queryset


# only superuser can see this api data
class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        reviewer_id = self.request.query_params.get("reviewer_id")
        tuition = self.request.query_params.get("tuition")

        if reviewer_id:
            queryset = queryset.filter(reviewer_id=reviewer_id)

        if tuition:
            queryset = queryset.filter(tuition=tuition)

        return queryset

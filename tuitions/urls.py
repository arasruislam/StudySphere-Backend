from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"list", views.TuitionViewSet)
router.register(r"all", views.AllTuitionViewSet, basename="all")
router.register(r"subjects", views.SubjectViewSet, basename="subjects")
router.register(r"applications", views.ApplicationViewSet, basename="applications")
router.register(r"reviews", views.ReviewViewSet, basename="reviews")


urlpatterns = [
    path("", include(router.urls)),
]

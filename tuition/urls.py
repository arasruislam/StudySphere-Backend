from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"tuitions", views.TuitionViewSet)
router.register(r"applications", views.ApplicationViewSet)
router.register(r"reviews", views.ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

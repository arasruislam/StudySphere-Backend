from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.InstructorApiView)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "register/",
        views.InstructorRegistrationApiView.as_view(),
        name="instructor_register",
    ),
    path("login/", views.InstructorLoginApiView.as_view(), name="instructor_login"),
    path("logout/", views.InstructorLogoutApiView.as_view(), name="instructor_logout"),
    path(
        "change_password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path("active/<uid64>/<token>/", views.Activate, name="activate"),
]

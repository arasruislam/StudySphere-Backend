from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.StudentApiView)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.StudentRegistrationApiView.as_view(), name="register"),
    path("login/", views.StudentLoginApiView.as_view(), name="login"),
    path("logout/", views.StudentLogoutApiView.as_view(), name="logout"),
    path(
        "change_password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path("active/<uid64>/<token>/", views.Activate, name="activate"),
]

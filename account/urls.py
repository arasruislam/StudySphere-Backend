from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "new_user/register/", views.UserRegistrationApiView.as_view(), name="register"
    ),
    path("user/login/", views.UserLoginApiView.as_view(), name="login"),
    path("user/logout/", views.UserLogoutApiView.as_view(), name="logout"),
    path(
        "user/change_password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path("active/<uid64>/<token>/", views.Activate, name="active"),
]

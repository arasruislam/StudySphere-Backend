from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api/student/", include("student.urls")),
    path("api/instructor/", include("instructor.urls")),
    path("api/tuitions/", include("tuitions.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

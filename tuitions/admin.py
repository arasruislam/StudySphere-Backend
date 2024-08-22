from django.contrib import admin
from .models import Tuition, TuitionApplication, Review


@admin.register(Tuition)
class TuitionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "level",
        "subject",
        "availability",
        "created_at",
        "updated_at",
    )
    list_filter = ("level", "subject", "availability")
    search_fields = ("title", "description")


@admin.register(TuitionApplication)
class TuitionApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "tuition", "applied_at", "status")
    list_filter = ("status",)
    search_fields = ("user__username", "tuition__title")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "tuition", "rating", "created_at")
    list_filter = ("rating",)
    search_fields = ("user__username", "tuition__title")

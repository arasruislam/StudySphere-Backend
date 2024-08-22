from django.contrib import admin
from .models import Tuition, Application, Review


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
    list_filter = ("level", "availability")
    search_fields = ("title", "description", "subject")
    list_editable = ("availability",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "tuition", "applied_at", "is_approved")
    list_filter = ("is_approved", "applied_at")
    search_fields = ("user__username", "tuition__title")
    list_editable = ("is_approved",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer", "tuition", "created", "rating")
    list_filter = ("rating", "created")
    search_fields = ("reviewer__username", "tuition__title", "body")
    readonly_fields = ("created",)

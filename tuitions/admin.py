from django.contrib import admin
from .models import Tuition


# Register your models here.
class TuitionAdmin(admin.ModelAdmin):
    list_display = ["title", "availability", "created_at"]


admin.site.register(Tuition, TuitionAdmin)

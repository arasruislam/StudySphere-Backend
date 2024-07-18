from django.contrib import admin
from .models import Tuition


# Register your models here.
class TuitionAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "level", "subject", "availability"]


admin.site.register(Tuition, TuitionAdmin)

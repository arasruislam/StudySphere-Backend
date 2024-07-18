from django.contrib import admin
from .models import Tuition, Application, Review


# Register your models here.
class TuitionAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "level", "subject", "availability"]


admin.site.register(Tuition, TuitionAdmin)
admin.site.register(Application)
admin.site.register(Review)

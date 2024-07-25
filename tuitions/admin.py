from django.contrib import admin
from .models import Tuition, Application, Review


# Register your models here.
class TuitionAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "level", "subject", "availability"]


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["user_id", "user", "tuition", "applied_at", "is_accepted"]

    def user_id(self, obj):
        return obj.user.id


admin.site.register(Tuition, TuitionAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Review)

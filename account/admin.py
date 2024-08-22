from django.contrib import admin
from .models import UserProfile


# Register your models here
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["_Id", "full_name", "city", "state", "phone", "profile_image"]

    def full_name(self, obj):
        return obj.user.get_full_name()

    def _Id(self, obj):
        return obj.user.id


admin.site.register(UserProfile, UserProfileAdmin)

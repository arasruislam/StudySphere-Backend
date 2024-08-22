from django.contrib import admin
from .models import Account, UserProfile


# Register your models here
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["_Id", "full_name", "city", "state", "social_links"]

    def full_name(self, obj):
        return obj.user.user.get_full_name()

    def _Id(self, obj):
        return obj.user.id


admin.site.register(UserProfile, UserProfileAdmin)

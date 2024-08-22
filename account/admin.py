from django.contrib import admin
from .models import Account, UserProfile


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ["profile_image", "phone"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["bio", "social_links"]


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

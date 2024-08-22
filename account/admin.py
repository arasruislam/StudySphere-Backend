from django.contrib import admin
from .models import Account, Address, UserProfile

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['profile_image', 'phone']
    
class AddressAdmin(admin.ModelAdmin):
    list_display =['street', 'city', 'state', 'zip_code']

class UserProfileAdmin(admin.ModelAdmin):
    list_display =['bio', 'address', 'social_links']
    
admin.site.register(Account, AccountAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
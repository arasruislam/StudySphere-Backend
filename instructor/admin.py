from django.contrib import admin
from .models import Instructor


# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["id","user", "gender", "phone", "address", "status"]
    list_filter = ["gender", "status"]
    search_fields = ["user__username", "phone", "address"]


admin.site.register(Instructor, InstructorAdmin)

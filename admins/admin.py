from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_disabled']

admin.site.register(CustomUser, CustomUserAdmin)
    
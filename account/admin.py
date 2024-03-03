from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomAdmin


@admin.register(CustomAdmin)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_display_links = ('username',)
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 15
    fieldsets = UserAdmin.fieldsets + (
        ('Other Fields', {'fields': ('phone', 'date_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Other Fields', {'fields': ('email',)}),
    )

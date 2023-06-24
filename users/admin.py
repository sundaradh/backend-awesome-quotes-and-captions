from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = []
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name', 'is_staff', 'is_subscriber')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'is_staff']


# admin.site.register(Users)
# class UsersAdmin(admin.ModelAdmin):
#           pass


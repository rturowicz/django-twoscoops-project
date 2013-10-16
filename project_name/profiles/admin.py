from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserChangeForm, AppUserCreationForm
from .models import AppUser


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('email', 'is_staff', 'name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name')
    ordering = ('email', )
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('name', )
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'name', 'password1', 'password2')
        }),
    )

admin.site.register(AppUser, AppUserAdmin)

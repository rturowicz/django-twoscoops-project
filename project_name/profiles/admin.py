from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from sorl.thumbnail.admin import AdminImageMixin

from .forms import AppUserChangeForm, AppUserCreationForm
from .models import AppUser


class AppUserAdmin(AdminImageMixin, UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('email', 'is_staff', 'username', 'avatar_thumb')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username')
    ordering = ('email', )
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('username', 'image')
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
            'fields': ('email', 'username', 'password1', 'password2')
        }),
    )

admin.site.register(AppUser, AppUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as t

from dbo import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """Register user management screen to admin panel"""
    ordering = ['-username']

    list_display = ['username', 'email', 'name', 'surname', 'is_apiuser',
                    'is_staff', 'is_superuser', 'is_active']

    fieldsets = (
        (t('Personal Info'), {
            'fields': ('username', 'email', 'name', 'surname')
        }),
        (t('Permissions'), {
            'fields': ('is_apiuser', 'is_staff', 'is_superuser', 'is_active')
        }),
        (None, {'fields': ('password',)}),
        (None, {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (t('Personal Info'), {
            'fields': ('username', 'email', 'name', 'surname')
        }),
        (t('Password'), {
            'fields': ('password1', 'password2')
        }),
        (t('Permissions'), {
            'fields': ('is_apiuser', 'is_staff', 'is_superuser')
        }),
    )

    readonly_fields = ['last_login']

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'location', 'number']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('location','number')}),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('location','number')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
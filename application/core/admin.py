from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ("name", "email")
    model = User
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    fieldsets = (
        (None, {
            "fields": (
                "email", "password",
            ),
        }),
        (_("Personal"),{
            "fields": (
                "name","created",
            ),
        }),
        (_("Permissions"),{
            "fields": (
                "is_active", "is_staff", "is_superuser", "user_permissions", "groups"
            ),
        })
    )
    
    

admin.site.register(User, UserAdmin)



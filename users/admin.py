from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_student", "is_author", "is_staff")
    list_filter = ("is_student", "is_author", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Роли", {"fields": ("is_student", "is_author")}),
    )

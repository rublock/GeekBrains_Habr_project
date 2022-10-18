from django.contrib import admin

from .models import Skills, User


@admin.register(Skills)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    readonly_fields = ("password",)
    fields = (
        "username",
        "password",
        "email",
        "first_name",
        "last_name",
        "middle_name",
        "avatar",
        "birthday",
        "phone_number",
        "gender",
        "comments",
        "skills_id",
        "is_active",
        "delete",
    )

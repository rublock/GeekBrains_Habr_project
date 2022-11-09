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
        "id",
        "is_staff",
        "is_moderator",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    readonly_fields = ("password",)
    ordering = ("id",)
    fieldsets = (
        (
            "Роль и права",
            {
                "fields": (
                    "is_staff",
                    "groups",
                )
            },
        ),
        (
            "Профиль",
            {
                "fields": (
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
                )
            },
        ),
        (
            "Статус аккаунта",
            {
                "fields": (
                    "is_active",
                    "delete",
                )
            },
        ),
    )

    @admin.display(description="Модератор", boolean=True)
    def is_moderator(self, obj):
        return obj.groups.filter(name="moderator").exists()

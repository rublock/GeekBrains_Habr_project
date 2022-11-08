from django.contrib import admin
from django.utils.safestring import mark_safe

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
        "get_html_photo",
        "first_name",
        "last_name",
        "is_active",
    )
    readonly_fields = ("password", "get_html_photo",)
    ordering = ("id",)
    list_display_links = ('username', 'email',)
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
                    "get_html_photo",
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

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_html_photo.short_description = "Фото"


admin.site.site_header = "Code Busters admin module"

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import DevAuthor


@admin.register(DevAuthor)
class DevAuthorModelAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name", 'get_html_photo']

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_html_photo.short_description = "Фото"

    class Meta:
        verbose_name = "Авторы проекта"

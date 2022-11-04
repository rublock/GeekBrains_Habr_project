from django.contrib import admin
from .models import DevAuthor


@admin.register(DevAuthor)
class DevAuthorModelAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name"]

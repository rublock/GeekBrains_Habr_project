from django.contrib import admin
from .models import Skills, UserProfile


@admin.register(Skills)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', )

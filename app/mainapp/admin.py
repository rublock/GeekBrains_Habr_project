from django.contrib import admin
from .models import Category, Post, Comment, Status


@admin.register(Category)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user_id']


@admin.register(Comment)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'post_id']


@admin.register(Status)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

from django import forms
from django.contrib import admin
from django.db.models import Manager as DefaultManager

from ckeditor.widgets import CKEditorWidget

from .models import Category, Post, Comment, Status, PostLikes, CommentLikes


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user_id", "active"]
    list_display_links = ('id', 'title',)
    form = PostAdminForm

    def get_queryset(self, request):
        return self.model.objects_all.all()


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "post_id"]

    def get_queryset(self, request):
        return self.model.objects_all.all()


@admin.register(Status)
class StatusModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(PostLikes)
class PostLikesModelAdmin(admin.ModelAdmin):
    list_display = ["id", "post_id", "user_id", "like_count", "active"]


@admin.register(CommentLikes)
class CommentLikesModelAdmin(admin.ModelAdmin):
    list_display = ["id", "comment_id", "user_id", "like_count", "active"]

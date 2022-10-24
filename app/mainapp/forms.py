from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = [
            "active",
            "is_deleted",
            "created_at",
            "updated_at",
            "objects",
        ]

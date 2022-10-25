from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class PostForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),)
    category.widget.attrs.update({'class': 'form-control'})
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
          
    class Meta:
        model = Post
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),

        }
        fields = "__all__"
        exclude = [
            "active",
            "is_deleted",
            "created_at",
            "updated_at",
            "objects",
        ]

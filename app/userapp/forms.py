from django.contrib.auth import get_user_model
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)


User = get_user_model()


class MyUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("username", "password")


class MyUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(UserChangeForm):
    avatar = forms.FileField()
    avatar.widget.attrs.update({"class": "form-control"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "middle_name": forms.TextInput(attrs={"class": "form-control"}),
            "birthday": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(
                choices=model.GENDER_CHOICES, attrs={"class": "form-control input"}
            ),
            "comments": forms.TextInput(attrs={"class": "form-control"}),
        }
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "birthday",
            "avatar",
            "phone_number",
            "gender",
            "comments",
        )

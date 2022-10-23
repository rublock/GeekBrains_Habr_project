from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("username", 
                  "email", 
                  "first_name", 
                  "last_name", 
                  "middle_name", 
                  "birthday",
                  "avatar",
                  "phone_number",
                  "gender", 
                  "comments",
                  "skills_id",)

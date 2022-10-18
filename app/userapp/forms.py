from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


User = get_user_model()



class MyUserLoginForm(AuthenticationForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)


    class Meta:
        model = User
        fields = ("username", "password")


class MyUserRegisterForm(UserCreationForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
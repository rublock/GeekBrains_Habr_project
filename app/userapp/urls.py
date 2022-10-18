from django.urls import path, include
import userapp.views as userapp

app_name = "userapp"

urlpatterns = [
    path(
        "activate-user/<str:uidb64>/<str:token>", userapp.activate_user, name="activate"
    ),
    path("login/", userapp.login, name="login"),
    path("logout/", userapp.logout, name="logout"),
    path("register/", userapp.register, name="register"),
]

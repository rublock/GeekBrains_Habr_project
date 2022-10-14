from django.urls import path, include

from userapp.views import Register, activate_user


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", Register.as_view(), name="register"),
    path("activate-user/<str:uidb64>/<str:token>", activate_user, name="activate"),
]

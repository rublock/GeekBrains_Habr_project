from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import userapp.views as userapp


app_name = "userapp"

urlpatterns = [
    path(
        "activate-user/<str:uidb64>/<str:token>", userapp.activate_user, name="activate"
    ),
    path("login/", userapp.login, name="login"),
    path("logout/", userapp.logout, name="logout"),
    path("register/", userapp.register, name="register"),
    path("account/", userapp.account, name="users-account"),
    path("profile/", userapp.profile, name="users-profile"),
    path("password/", userapp.change_password, name="change_password"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

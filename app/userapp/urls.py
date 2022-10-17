from django.urls import path, include
#from .views import Register, activate_user
import userapp.views as userapp

app_name = 'userapp'

urlpatterns = [
    #path("", include("django.contrib.auth.urls")),
    #path("register/", Register.as_view(), name="register"),
    #path("activate-user/<str:uidb64>/<str:token>", activate_user, name="activate"),
    path('login/', userapp.login, name='login'),
    path('logout/', userapp.logout, name='logout'),
    path('register/', userapp.register, name='register'),
]

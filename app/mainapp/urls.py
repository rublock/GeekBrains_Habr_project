from django.urls import path

from .apps import MainappConfig
from . import views

app_name = MainappConfig.name

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]

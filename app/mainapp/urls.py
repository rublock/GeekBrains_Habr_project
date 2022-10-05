from django.urls import path

from .apps import MainappConfig
from . import views

app_name = MainappConfig.name

urlpatterns = [
    path('', views.main_view, name='main'),
]

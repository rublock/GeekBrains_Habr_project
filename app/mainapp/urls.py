from django.urls import path

from .apps import MainappConfig
from . import views

app_name = MainappConfig.name

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service')
]

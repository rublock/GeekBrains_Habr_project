from django.urls import path

from .apps import ApiConfig
from . import views

app_name = ApiConfig.name

urlpatterns = [
    path('search-post/', views.SearchPostApiView.as_view()),
]

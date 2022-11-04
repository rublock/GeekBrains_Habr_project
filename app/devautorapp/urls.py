from django.urls import path

from .apps import DevautorappConfig
from . import views

app_name = DevautorappConfig.name

urlpatterns = [
    path("authors", views.dev_authors, name="dev_authors"),
]

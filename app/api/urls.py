from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .apps import ApiConfig
from .views import PostViewSet

app_name = ApiConfig.name

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
]

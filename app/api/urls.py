from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .apps import ApiConfig
from .views import PostViewSet

app_name = ApiConfig.name

router = DefaultRouter()
router.register("posts", PostViewSet, basename="Post")

urlpatterns = [
    path("v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("v1/", include(router.urls)),
]

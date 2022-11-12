from django.urls import path, include, re_path
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .apps import ApiConfig
from .views import PostViewSet, PostLikeAPIView, CommentLikeAPIView
from .schema import schema_view

app_name = ApiConfig.name

router = DefaultRouter()
router.register("posts", PostViewSet, basename="Post")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("post_like/<int:post_id>/", PostLikeAPIView.as_view(), name="post_like"),
    path(
        "comment_like/<int:comment_id>/",
        CommentLikeAPIView.as_view(),
        name="comment_like",
    ),
    # Авторизация по JWT токену
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Документация Swagger
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swaggerui/swaggerui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]

from rest_framework.pagination import PageNumberPagination

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework import filters

from .serializers import (
    PostListSerializer,
    PostRetrieveSerializer,
    PostCreateSerializer,
)
from .permissons import IsOwner
from mainapp.models import Post


class PostViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 10


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    pagination_class = PostViewSetPagination

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = (
        "title",
        "description",
        "content",
    )
    ordering_fields = ("created_at",)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostRetrieveSerializer
        if self.action == "create":
            return PostCreateSerializer
        return PostListSerializer

    def get_permissions(self):
        if self.action == "create":
            # Создавать посты могут только авторизованные пользователи
            self.permission_classes = [IsAuthenticated]
        elif self.action in ("destroy", "update", "partial_update"):
            # Удалять и редактировать посты могут только авторы и админы
            self.permission_classes = [IsOwner | IsAdminUser]
        else:
            # Читать посты могут все
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(self.__class__, self).get_permissions()

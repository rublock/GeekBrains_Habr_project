from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework import views, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
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
    PostLikesSerializer,
    CommentLikesSerializer,
)
from .permissons import IsOwner
from mainapp.models import Post, PostLikes, Comment, CommentLikes


class PostViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 10


class PostViewSet(ModelViewSet):
    pagination_class = PostViewSetPagination

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = (
        "title",
        "description",
        "content",
    )
    ordering_fields = ("created_at",)

    def get_queryset(self):
        # Модератор и суперюзер видят все посты, а пользователи-только активные
        user = self.request.user
        if user.is_authenticated and (user.is_superuser or user.is_moderator):
            return Post.objects.all()
        return Post.objects.filter(active=True)

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


class PostLikeAPIView(views.APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            post_id = self.kwargs["post_id"]
        except Exception:
            raise ValueError
        post: Post = get_object_or_404(Post, pk=post_id)
        instance, created = PostLikes.objects.get_or_create(
            user=request.user, post=post
        )
        if created:
            like_status = True
        else:
            like_status = not instance.status
        data = {"user": request.user.id, "post": post_id, "status": like_status}
        serializer = PostLikesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance.status = like_status
        instance.save()
        post.refresh_from_db()
        response_data = {"likes": post.likes_count}
        return Response(data=response_data, status=status.HTTP_200_OK)


class CommentLikeAPIView(views.APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            comment_id = self.kwargs["comment_id"]
        except Exception:
            raise ValueError
        comment: Comment = get_object_or_404(Comment, pk=comment_id)
        instance, created = CommentLikes.objects.get_or_create(
            user=request.user, comment=comment
        )
        if created:
            like_status = True
        else:
            like_status = not instance.status
        data = {"user": request.user.id, "comment": comment_id, "status": like_status}
        serializer = CommentLikesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance.status = like_status
        instance.save()
        comment.refresh_from_db()
        response_data = {"likes": comment.likes_count}
        return Response(data=response_data, status=status.HTTP_200_OK)

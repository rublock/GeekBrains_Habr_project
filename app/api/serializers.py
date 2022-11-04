from rest_framework import serializers
from mainapp.models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    """Список превью статей"""

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
            "user",
            "title",
            "description",
            "image",
            "created_at",
            "updated_at",
        )


class CommentListSerializer(serializers.ModelSerializer):
    """Список комментариев к статье"""

    class Meta:
        model = Comment
        fields = ("id", "user", "parent", "text", "created_at", "updated_at")


class PostRetrieveSerializer(serializers.ModelSerializer):
    """Детальное представление статьи с комментариями"""

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
            "user",
            "title",
            "description",
            "content",
            "image",
            "created_at",
            "updated_at",
            "comments",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    """Создание новой статьи с указанием ID автора"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
            "user",
            "title",
            "description",
            "content",
            "image",
            "created_at",
            "updated_at",
        )

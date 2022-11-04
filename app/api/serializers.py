from rest_framework import serializers
from mainapp.models import Post, Comment


class PostModelSerializer(serializers.ModelSerializer):
    # TODO: выводить список комменатриев или нет?
    # TODO: active
    class Meta:
        model = Post
        fields = ("id", "category", "user", "created_at", "updated_at", "title", "description", "content", "image")


class PostCreateModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ("id", "category", "user", "created_at", "updated_at", "title", "description", "content", "image")

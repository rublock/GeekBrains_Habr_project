from rest_framework.serializers import ModelSerializer
from mainapp.models import Post, Comment


class PostModelSerializer(ModelSerializer):
    # TODO: выводить список комменатриев или нет?
    # TODO: active
    class Meta:
        model = Post
        fields = ("id", "category", "user", "created_at", "updated_at", "status", "title", "description", "content", "image")

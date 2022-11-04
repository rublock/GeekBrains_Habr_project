from rest_framework.viewsets import ModelViewSet

from .serializers import PostModelSerializer
from mainapp.models import Post, Comment


class PostViewSet(ModelViewSet):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

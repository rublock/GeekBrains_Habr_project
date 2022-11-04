from rest_framework.viewsets import ModelViewSet

from .serializers import PostModelSerializer, PostCreateModelSerializer
from mainapp.models import Post, Comment


class PostViewSet(ModelViewSet):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateModelSerializer
        return PostModelSerializer

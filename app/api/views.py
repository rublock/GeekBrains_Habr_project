from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, DjangoModelPermissions

from .serializers import PostModelSerializer, PostCreateModelSerializer
from .permissons import IsOwner
from mainapp.models import Post, Comment


class PostViewSet(ModelViewSet):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateModelSerializer
        return PostModelSerializer

    def get_permissions(self):

        if self.action == 'create':
            # Создавать посты могут только авторизованные пользователи
            self.permission_classes = [IsAuthenticated]
        elif self.action in ('destroy', 'update', 'partial_update'):
            # Удалять и редактировать посты могут только авторы и админы
            self.permission_classes = [IsOwner|IsAdminUser]
        else:
            # Читать посты могут все
            self.permission_classes = [IsAuthenticatedOrReadOnly]

        return super(self.__class__, self).get_permissions()

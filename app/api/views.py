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
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner|IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]

        return super(self.__class__, self).get_permissions()

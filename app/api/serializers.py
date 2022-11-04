from rest_framework.serializers import ModelSerializer
from mainapp.models import Post, Comment


class PostModelSerializer(ModelSerializer):
    # TODO: выводить список комменатриев или нет?
    class Meta:
        model = Post
        fields = '__all__'

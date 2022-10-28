from django.urls import reverse
from rest_framework import serializers

from mainapp.models import Post


class SearchPostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=70)
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse("mainapp:detail", kwargs={"post_id": obj.id})

    class Meta:
        model = Post
        fields = ("id", "name")

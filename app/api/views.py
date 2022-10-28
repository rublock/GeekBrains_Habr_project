from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SearchPostSerializer

from mainapp.models import Post


class SearchPostApiView(APIView):
    def get(self, request, format=None):
        search = request.GET.get('search', '')

        if not search:
            return Response(Post.objects.none())

        posts = Post.objects.filter(
            Q(title__icontains=search)
        ).order_by("-created_at")

        serializer = SearchPostSerializer(posts[:10], many=True)

        return Response(serializer.data)

from django.http import HttpRequest
from instagram.serializers import PostSerializer
from instagram.models import Post
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        print("request.body:", request.body)
        print("request.post:", request.POST)
        return super().dispatch(request, *args, **kwargs)

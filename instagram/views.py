from django.http import HttpRequest
from instagram.serializers import PostSerializer
from instagram.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PublicPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer


class PublicPostListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


# public_post_list = PublicPostListAPIView.as_view()


@api_view()
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        print("request.body:", request.body)
        print("request.post:", request.POST)
        return super().dispatch(request, *args, **kwargs)

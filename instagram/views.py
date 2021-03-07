from django.http import HttpRequest
from instagram import serializers
from instagram.serializers import PostSerializer
from instagram.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
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

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # http PATCH localhost:8000/post/1/ is_public=True
    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

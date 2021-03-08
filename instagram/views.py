from instagram.permissions import IsAuthorOrReadonly
from instagram.serializers import PostSerializer
from instagram.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter


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


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "instagram/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({"post": post})  # PostSerializer(post).data,


# http localhost:8000/public/ Accept:text/html
@api_view(
    # ["GET"]
)
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]
    # authentication_classes = []
    search_fields = ["^message"]
    filter_backends = [SearchFilter, OrderingFilter]
    

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

    def perform_create(self, serializer):
        serializer.save(ip=self.request.META["REMOTE_ADDR"], author=self.request.user)
        return super().perform_create(serializer)

from instagram.models import Post
from rest_framework import serializers
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            "pk",
            "message",
            "created_at",
            "updated_at",
            "author",
            "author_username",
        ]

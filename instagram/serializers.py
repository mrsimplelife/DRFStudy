from instagram.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "pk",
            "message",
            "created_at",
            "updated_at",
        ]
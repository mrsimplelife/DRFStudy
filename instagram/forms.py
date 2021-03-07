from instagram.models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            # "pk",
            "message",
            # "created_at",
            # "updated_at",
        ]

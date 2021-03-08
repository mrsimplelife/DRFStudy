from instagram.models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            # "pk",
            "message",
            "is_public",
            # "created_at",
            # "updated_at",
        ]


# form = PostForm(request.POST)
# if form.is_valid():
#     post = form.save(commit=False)
#     post.author = request.user
#     post.ip = request.META['REMOTE_ADDR']
#     post.save()

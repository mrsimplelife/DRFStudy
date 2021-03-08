from posix import listdir
from instagram.models import Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["pk", "message", "author"]
    search_fields = ["message"]

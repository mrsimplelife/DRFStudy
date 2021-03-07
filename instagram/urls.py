from django.urls import include, path
from instagram import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("post", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("public/", views.public_post_list),
]
